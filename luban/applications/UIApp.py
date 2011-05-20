# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from pyre.components.Component import Component
class Extension(Component):

    def __init__(self, name='luban-uiapp-extension', facility='extension'):
        super(Extension, self).__init__(name=name, facility=facility)
        return



from pyre.applications.Script import Script as Base


class UIApp(Base):


    class Inventory(Base.Inventory):
        
        import pyre.inventory
        import luban.inventory
        import luban.components

        # actor.routine
        # actor
        # actor = luban.inventory.actor()
        actor = luban.inventory.actor(default=luban.components.notImplementedActor())
        actor.meta['tip'] = "the component that defines the application behavior"
        #
        # routine
        routine = pyre.inventory.str("routine", default=None)
        routine.meta['tip'] = "the action to be performed by the actor"
        
        
        # painter
        from luban.components.Painter import Painter as DummyPainter
        painter = pyre.inventory.facility('painter', factory=DummyPainter)

        
        # db access
        from luban.components.Clerk import Clerk
        clerk = pyre.inventory.facility('clerk', factory=Clerk)


        # authentication client
        sentry = pyre.inventory.facility("sentry", factory=luban.components.sentry)
        sentry.meta['tip'] = "the ipa session manager"


        # guid generator
        guid = pyre.inventory.facility('guid', factory=luban.components.guid)
        guid.meta['tip'] = "the guid generator"

        # activity logging
        activity_logger = pyre.inventory.facility(
            'activity-logger', factory = luban.components.activityLogger)

        # extension
        extension = pyre.inventory.facility('extension', factory=Extension)

        #
        debug = pyre.inventory.bool(name="debug", default=True)
        debug.meta['tip'] = "suppress some html output for debugging purposes"

        #
        logdir = pyre.inventory.str('log-dir', default='../log')
        

    def main(self, *args, **kwds):
        rt = None
        try:
            rt = self._main(*args, **kwds)
        except:
            return self._reportBug()
        else:
            if self.debug:
                debug_info = self._getDebugInfo()
                self._saveDebugInfo(debug_info, 'debug')
        return rt
        

    # redirect to a different actor
    def redirect(self, actor, routine, **kwds):
        raise NotImplementedError


    # retrievers
    def retrieveActor(self, name):
        actor = self.retrieveComponent(name, factory='actor', vault=['actors'])
        if actor is None:
            curator_dump = self._dumpCurator()
            raise ActorNotFound, "could not locate actor %r. curator dump: %s" % (
                name, curator_dump)
        return actor


    def retrieveVisual(self, name, *args, **kwds):
        if kwds.has_key('factory'):
            factory = kwds['factory']
            del kwds['factory']
        else:
            factory = 'visual'
        if not args and not kwds: args=[self]
        visual = self.retrieveComponent(name, factory=factory, args=args, kwds=kwds, vault=['visuals'])
        if visual:
            if 'visual_injsondict' in visual.__dict__:
                visual = visual.visual_injsondict
                visual = self.jsondict2uielement.render(visual)
            return visual

        curator_dump = self._dumpCurator()
        raise VisualNotFound, "could not locate visual %r. curator dump: %s" % (
            name, curator_dump)


    # user authentication
    def userIsActive(self):
        activeUsers = self.clerk.indexActiveUsers()
        return self.sentry.username in activeUsers


    def userIsAuthorized(self):
        if not self.userIsActive(): return False
        ticket = self.sentry.authenticate()
        self._debug.log('ticket: %s' % ticket)
        return ticket is not None


    # render a visual. to be implemented by subclasses
    def render(self, visual=None):
        raise NotImplementedError


    # guid generator
    def getGUID(self):
        return self.guid.generate()
    

    def __init__(self, name):
        super(UIApp, self).__init__(name)

        # turn on the info channel
        self._info.activate()

        return

    # implementation details
    def _main(self, *args, **kwds):

        self._info.log('recording activity ...')
        self._recordActivity()

        # make sure actor is good
        actor = self.actor
        if actor is None:
            curator_dump = self._dumpCurator()
            raise ActorNotFound, "actor not loaded. curator dump: %s" % (
                curator_dump,)
                
        # perform
        self._info.log('actor %s running ...' % self.actor.name)
        visual = self.actor.perform(self, routine=self.inventory.routine, debug=self.debug)

        # render
        self._info.log('rendering visual %s...' % (visual,))
        return self.render(visual)


    def _reportBug(self):
        debug_info = self._getDebugInfo()
        bugid = self.getGUID()
        self._saveDebugInfo(debug_info, bugid)

        import luban.content as lc
        try:
            visual = self.retrieveVisual('bug-report-dialog', id=bugid, info=debug_info)
        except VisualNotFound:
            visual = lc.dialog(title='bug #%s' % bugid, autoopen=1)
            body = lc.htmldocument(text=['<pre>'+debug_info['traceback']+'</pre>'])
            visual.add(body)
            okbutton = lc.button(label='ok', onclick=lc.select(element=visual).destroy())
            visual.add(okbutton)

        action = lc.select(id='').append(visual)
        self.render(action)

        return
    

    def _saveDebugInfo(self, info, identifier):
        import os
        dir = os.path.abspath(self.inventory.logdir)

        for k, v in info.iteritems():
            p = os.path.join(dir, '.'.join([identifier, k]))
            open(p, 'w').write(v)
            continue

        return


    def _getDebugInfo(self):
        info = {}
        
        import traceback
        info['traceback'] = traceback.format_exc()

        return info


    def _recordActivity(self):
        if not self.actor: return
        
        activity = Activity(
            id = self.getGUID(),
            actor = self.actor.name,
            username = self.sentry.username,
            routine = self.inventory.routine,
            )
        return self.activity_logger.log(activity)


    def _dumpCurator(self):
        import cStringIO
        stream = cStringIO.StringIO()
        # self.getCurator().dump(stream=stream)
        curator = self.getCurator()
        dumpCurator(curator, stream)
        curator_dump = stream.getvalue()
        stream.close()
        return curator_dump
    

    def _defaults(self):
        super(UIApp, self)._defaults()
        self.inventory.typos = 'relaxed'
        return


    def _configure(self):
        super(UIApp, self)._configure()

        # the authenticator
        self.sentry = self.inventory.sentry

        # the behavior
        self.actor = self.inventory.actor
        self.routine = self.inventory.routine

        # the painter
        self.painter = self.inventory.painter
        self.painter.director = self

        # the db accessor
        self.clerk = self.inventory.clerk
        self.clerk.director = self

        # the guid client
        self.guid = self.inventory.guid

        #
        self.activity_logger = self.inventory.activity_logger

        #
        self.extension = self.inventory.extension
        self.extension.director = self
        
        #
        self.debug = self.inventory.debug
        
        return


    def _init(self):
        super(UIApp, self)._init()
        def _(obj):
            return self.getGUID()
        from luban.content import GUID
        GUID.GUID = _

        from luban.weaver.JsonDict2UIElement import JsonDict2UIElement
        self.jsondict2uielement = JsonDict2UIElement()

        from utils import redirectWarningsToJournal 
        redirectWarningsToJournal('warning')
        import warnings; warnings.warn('This is the first warning for this run of application showing up in journal:warning:UserWarning')
        return


    def _fini(self):
        import warnings; warnings.warn('This is the last warning for this run of application showing up in journal:warning:UserWarning')
        super(UIApp, self)._fini()
        return


class Activity:

    def __init__(
        self,
        id=None, actor=None, routine=None, username=None, remote_address=None):
        
        self.id = id
        self.actor = actor
        self.routine = routine
        self.username = username
        self.remote_address = remote_address

    def __str__(self):
        return "Activity #%s from %s@%s: %s.%s" % (
            self.id, self.username, self.remote_address,
            self.actor, self.routine)


# Exceptions
class ActorNotFound(Exception): pass
class VisualNotFound(Exception): pass


# modified from pyre.inventory.odb.Curator.Curator.dump
# the original dump contains too much information, while most
# of them are just file-not-found errors for pyre components.
def dumpCurator(curator, stream):
    print >>stream, "curator info:"
    print >>stream, "    depositories:", [d.name for d in curator.depositories]

    if curator._componentRequests:
        print >>stream, "    component requests:"
        for trait, record in curator._componentRequests.iteritems():
            print >>stream, "        component='%s'" % trait
            for entry in record:
                file, e = entry
                if str(e).find('No such file or director') == -1:
                    print >>stream, "            %s: %s" % entry

    return




import journal
journal.error('pyre.inventory').deactivate()


if __name__=='__main__':
    w=UIApp(name='test')
    print w

# version
__id__ = "$Id$"

# End of file 
