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


from UIApp import UIApp as Base, Activity


class WebApplication(Base):


    class Inventory(Base.Inventory):
        
        import pyre.inventory
        stream = pyre.inventory.outputFile("stream")
        stream.meta['tip'] = "where to place the generated text"

        content = pyre.inventory.str(
            name="content", default="auto",
            validator=pyre.inventory.choice(
                ["auto", "html", "attachment", "json", "text"])
            )
        content.meta['tip'] = "the target browser behaviour"

        run_from_console = pyre.inventory.bool('run-from-console')


    def main(self, *args, **kwds):
        # the web application could be hard to debug from the interface
        # sometimes, it is easier to just run from the console the application
        # and then debug it from there.
        # so we overload UIApp.main and see if the flag "run_from_console"
        # is set and just raise the exception instead of packing it up
        try:
            self._main(*args, **kwds)
        except:
            if self.inventory.run_from_console: 
                raise
            return self._reportBug()
        else:
            if self.debug:
                debug_info = self._getDebugInfo()
                self._saveDebugInfo(debug_info, 'debug')
        return


    def redirect(self, actor, routine, **kwds):
        '''redirect to the specified actor and routine

        The keyword arguments are passed to the specified actor.

        Common keyword arguments:

          - include_credential: this is valid for all actors inherited
            from AuthorizedActor. If true, a credential will be
            included in the returned luban action or document.
            By default, this is true.
        '''
        self.inventory.routine = routine
        self.actor = self.retrieveActor(actor)
        
        if self.actor is not None:
            self.configureComponent(self.actor)
            for k,v in kwds.iteritems():
                setattr(self.actor.inventory, k, v)

        try:
            page = self.actor.perform(self, routine=self.inventory.routine, debug=self.debug)
        except Exception, err:
            import traceback
            msg = "redirect to actor %r, routine %r, with kwds %r failed. %s" % (
                actor, routine, kwds, traceback.format_exc())
            self._debug.log(msg)
            raise RuntimeError, msg
        return page


    def render(self, page=None):
        contenttype = self.inventory.content
        if contenttype == 'auto':
            return self._render_auto(page)
        
        # get the headers out asap
        self._printHeaders()
        
        if isinstance(page, basestring):
            print page
            return

        raise NotImplementedError, 'content type: %s, page: %s' % (
            contenttype, page)


    # override this method to collect cgi input
    def collectUserInput(self, registry):

        # first extract standard commandline arguments
        help, argv = self.processCommandline(registry)

        # argv now contains the left over, unprocessed arguments
        # look through them for GET input
        collectCGIInput = self._createCGIInputCollector()
        argv = collectCGIInput(registry, argv)

        # for debug
        self._cgi_input = collectCGIInput.getCGIInput()
        self._uploads = collectCGIInput.getUploads()

        return help, argv


    def getUploads(self): return self._uploads

    
    def _render_auto(self, target):
        from luban.content.File import File
        if isinstance(target, File):
            return self._render_file(target)

        self.inventory.type = 'html'
        self._printHeaders()
        
        if isinstance(target, basestring) or isinstance(target, types.IntType) or isinstance(target, dict):
            # XXX
            # list type is not here since a list of actions 
            # may be the target to render.
            # in case of list,
            # should have a better implementation to check
            # if the target is a simple list that can be rendered
            # by json, or a list of actions.
            # 
            print jsonEncode(target)
        elif target is None:
            # an empty json object
            print "{}"
        elif isinstance(target, AttributeContainer):
            self.weaver.resetRenderer()
            self.weaver.weave(document=target, stream=self.stream)
        else:
            try:
                self.weaver.resetRenderer()
                self.weaver.weave(document=target, stream=self.stream)
            except:
                import traceback
                self._debug.log(traceback.format_exc())
                print jsonEncode(target)
        return

    
    def _render_file(self, file):
        print "Content-Type: application/octet-stream\r\n",
        print 'Content-Disposition: attachment; filename=%s\r\n' % file.filename,
        print
        import sys
        sys.stdout.write(file.content)
        return

    
    def _getDebugInfo(self):
        d = super(WebApplication, self)._getDebugInfo()

        from configurationSaver import toPml
        import cStringIO
        stream = cStringIO.StringIO()
        toPml(self, stream=stream)
        d['pml'] = stream.getvalue()
        stream.close()

        text = ['%s=%s' % (k,v) for k,v in self._cgi_input.iteritems()]
        d['cgi-input'] = '\n'.join(text)

        return d


    def _recordActivity(self):
        if not self.actor: return
        
        activity = Activity(
            id = self.getGUID(),
            actor = self.actor.name,
            username = self.sentry.username,
            routine = self.inventory.routine,
            remote_address = self._cgi_input.get('REMOTE_ADDR') or 'local',
            )
        return self.activity_logger.log(activity)


    def _printHeaders(self):
        if self.content == "html":
            print 'Content-type: text/html'
            print ''
        elif self.content == "attachment":
            # header output to be done by the process at a later time
            pass
        elif self.content == "json":
            print 'Content-type: application/json'
            print ''
        elif self.content == "text":
            print 'Content-type: text/plain'
            print ''
        elif self.content == 'auto':
            print 'Content-type: text/html'
            print ''

        # just in case further output is done by a subprocess
        import sys
        sys.stdout.flush()

        return


    def _defaults(self):
        super(WebApplication, self)._defaults()
        from luban.components.weaver.web import weaver
        self.inventory.weaver = weaver()
        return


    def _configure(self):
        super(WebApplication, self)._configure()
        self.stream = self.inventory.stream
        self.content = self.inventory.content
        return


    def _init(self):
        super(WebApplication, self)._init()
        if self.content == 'html':
            # take care of exception output
            self._initializeTraceback()
        return


    def _initializeTraceback(self):
        # pipe stderr to stdout
        import sys
        sys.stderr = sys.stdout
        
        # decorate exceptions
        import cgitb
        cgitb.enable()
        return


    def _createCGIInputCollector(self, **kwds):
        from CGIInputCollector import CGIInputCollector
        return CGIInputCollector(**kwds)



import types
from luban.weaver.web._utils import jsonEncode
from luban.content.AttributeContainer import AttributeContainer


if __name__=='__main__':
    w=WebApplication(name='test')
    print w
    

# version
__id__ = "$Id$"

# End of file 
