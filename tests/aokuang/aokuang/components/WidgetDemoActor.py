# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



import luban.content as lc
from luban.content import load, select, alert

from UIElementDemoActor import Actor as base, panel, example, quickpanel

class Actor(base):

    widget = None # override this with the widget type this actor is about
    
    def _createAPIDocument(self, director):
        w = self.widget
        descriptors = w.getDescriptors()
        descriptors = self._categorizeDescriptors(descriptors)
        
        doc = lc.document()
        tabs = lc.tabs(); doc.add(tabs)
        #
        tab1 = tabs.tab(label='Introduction')
        d = self._createIntroductionDocument(descriptors); tab1.add(d)
        #
        tab2 = tabs.tab(label='Properties')
        tab2.onselect = select(element=tab2).replaceContent(
            load(actor=self.name, routine='propertiesDocument'))
        #
        tab3 = tabs.tab(label='Events')
        tab3.onselect = select(element=tab3).replaceContent(
            load(actor=self.name, routine='eventsDocument'))
        #
        tab4 = tabs.tab(label='Actions')
        tab4.onselect = select(element=tab4).replaceContent(
            load(actor=self.name, routine='actionsDocument'))
        #
        return doc


    def propertiesDocument(self, director):
        w = self.widget
        descriptors = w.getDescriptors()
        descriptors = self._categorizeDescriptors(descriptors)
        properties = descriptors['properties']
        return self._createPropertiesDocument(properties)
    

    def eventsDocument(self, director):
        w = self.widget
        descriptors = w.getDescriptors()
        descriptors = self._categorizeDescriptors(descriptors)
        events = descriptors['eventhandlers']
        return self._createEventsDocument(events)


    def actionsDocument(self, director):
        w = self.widget
        actions = findActions(w)
        return self._createActionsDocument(actions)
    

    def _createEventsDocument(self, events):
        container = lc.document()
        
        descriptiontext = """You can specify what actions occur when an event happens in a luban element. The event handlers listed below are attributes of the luban element. If you set an event handler to be an action(or a list of actions), then that action(s) will be performed whenever the event occurs. """
        description = lc.restructuredtextdocument(); container.add(description)
        description.Class = 'demo-description'
        description.text = [descriptiontext]

        for d in events:
            if hasattr(d, 'tip'): tip = d.tip
            else: tip = 'Please give a tip of property %s' % d.name
            
            title = d.name
            if hasattr(d, 'experimental') and d.experimental:
                title += '(experimental)'
            doc = container.document(title=title, collapsable=True, collapsed=True)
            doc.Class = 'api-item'

            examplecode = self.name + 'instance' + '.' + d.name + ' = some_action'
            ex = doc.paragraph(text=[examplecode])
            ex.Class = 'signature'
            
            p = doc.paragraph()
            p.text = tip.splitlines()
            p.Class = 'description' 
            continue
        return container


    def _createActionsDocument(self, actions):
        container = lc.document()

        descriptions = [
            'The following are methods to create actions for a widget.',
            'Any of these methods has to be called by a selector that selects the widget.',
            'For example the method "destroy" below can be used to create an',
            'action to destroy a button widget by ::',
            '',
            '  select(id="buttonid").destroy()',
            '',
            'Pleaset note that the above method returns an action, and the action',
            'can be assigned to an event handler.',
            '',
            'Expand any section below for details of each action.',
            ]
        descdoc = lc.restructuredtextdocument(); container.add(descdoc)
        descdoc.Class = 'demo-description'
        descdoc.text = descriptions

        for name, method in actions:
            sig, content = getMethodInfo(method)

            title = name
            if hasattr(method, 'experimental') and method.experimental:
                title += '(experimental)'
            doc = container.document(title=title, collapsable=True, collapsed=True)
            doc.Class = 'api-item'
            
            sigp = doc.paragraph(text=[sig])
            sigp.Class = 'signature'
            p = doc.paragraph()
            p.text = content.splitlines()
            p.Class = 'description'
            continue
        return container


    def _categorizeDescriptors(self, descriptors):
        'put descriptors into different categories such as properties, eventhandlers'
        r = {
            'properties': [],
            'eventhandlers': [],
            }

        # contents is not really directly settable
        skip = ['contents']

        from luban.content.descriptors import EventHandler
        for d in descriptors:
            if d.name in skip: continue
            if isinstance(d, EventHandler):
                r['eventhandlers'].append(d)
                continue
            r['properties'].append(d)
            continue

        return r


    def __init__(self, *args, **kwds):
        super(Actor, self).__init__(*args, **kwds)
        self.element = self.widget
        return


from DemoActor import getSourceLines
def getMethodInfo(method):
    source = getSourceLines(method)
    lineno, line1 = source[0]
    define = line1.strip()[3:].strip()[:-1]
    # define = define.replace('*', r'\*')
    # define is now like "enable(self)", change it to "selector.enable()"
    define = 'selector.' + define.replace('self,', '').replace('self', '')
    doc = method.__doc__
    return define, doc


def iterCommonActions():
    import inspect
    from luban.content.ElementActions import ElementActions
    for k,v in ElementActions.__dict__.iteritems():
        if k.startswith('_'): continue
        if inspect.ismethod(v) or inspect.isfunction(v): yield k, v
        continue
    return


def findActions(widget):
    return list(iterCommonActions())


#version
__id__ = "$Id$"

# End of file 
