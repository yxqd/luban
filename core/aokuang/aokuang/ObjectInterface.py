# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""interface factory base class for luban UI object types

decorations to inspect:
* experimental

"""


import luban


class Factory:


    object_type = None # target object type this factory will build interface for
    actor = None # name of the actor for this interface
    demo_panels = None # a list of demo panels, each an instance of DemoPanel
    api_categories = ['properties', 'events']
    

    def create(self):
        container = luban.e.document()

        object_type = self.object_type
        if hasattr(object_type, 'experimental') and object_type.experimental:
            p = container.paragraph(text='This is still experimental', Class='warning')

        # the demo document
        doc = self._createDemoDocument()
        doc.title = 'Demos'
        doc.Class = 'demo-document'
        container.append(doc)

        # the api document
        doc = self._createAPIDocument()
        doc.title = 'API'
        doc.Class = 'api-document'
        container.append(doc)
        return container


    def _createDemoDocument(self):
        """create demo document 
        """
        # container
        container = luban.e.document(name='demo-document')
        tabs = container.tabs(id="demo-document-tabs")

        for i,panel in enumerate(self.demo_panels):
            # use inner document's title as tab's label
            label = panel.title
            # create tab 
            tab = tabs.tab(label=label, id='demo-tab-%s' % i)
            # 
            actor = panel.actor_name
            routine = "createInterface"
            # add the first document
            if i == 0:
                inner = self.controller.call(actor=actor, routine=routine)
                tab.append(inner)
                
            tab.onselect = luban.a.select(element=tab).replaceContent(
                newcontent=luban.a.load(actor=actor, routine=routine)
                )
            continue

        return container


    def _createAPIDocument(self):
        object_type = self.object_type
        descriptors = object_type.iterDescriptors()
        descriptors = self._categorizeDescriptors(descriptors)
        
        doc = luban.e.document(name='api-document')
        tabs = luban.e.tabs(); doc.append(tabs)
        #
        tab1 = tabs.tab(label='Introduction')
        d = self._createIntroductionDocument(descriptors); tab1.append(d)
        #
        categories = self.api_categories
        for cat in categories:
            if cat in descriptors and descriptors[cat]:
                tab2 = tabs.tab(label=cat.capitalize())
                handler = '_create%sDocument' % (cat.capitalize(),)
                handler = getattr(self, handler)
                d = handler(descriptors[cat])
                tab2.append(d)
            continue
        #
        return doc
    

    def _createIntroductionDocument(self, descriptors):
        d = luban.e.restructuredtextdocument()
        object_type = self.object_type
        title = "%s: %s" % (object_type.__name__, object_type.simple_description)
        title = '%s\n%s\n' % (title, '-'*len(title))
        description = object_type.full_description
        if not isinstance(description, str):
            raise ValueError("full_description of a luban type must be a str, not %r" % (description, ))

        ctordoctitle = 'signature::'
        if '__init__' in object_type.__dict__:
            ctordocstr = object_type.__init__.__doc__
        else:
            ctordocstr = ''
        if not ctordocstr:
            # props = descriptors['properties']
            ctordocstr = object_type.getCtorDocStr() # descriptors=props
        
        text = [title, description, '', ctordoctitle, '', ' '+ctordocstr]
        d.text = '\n'.join(text)
        return d


    def _createPropertiesDocument(self, props):
        container = luban.e.document()

        # explanation
        descdoc = luban.e.restructuredtextdocument(); container.append(descdoc)
        descdoc.Class = 'demo-description'
        # descdoc.text = 'expand an item for details'
        
        for d in props:
            if hasattr(d, 'tip'): tip = d.tip
            else: tip = 'Please give a tip of property %s' % d.name

            # the document
            doc = container.document()
            doc.Class = 'api-item'

            # title
            title = d.name
            if hasattr(d, 'experimental') and d.experimental:
                title += '(experimental)'
            doc.title = title

            # subdocument
            subdoc = luban.e.restructuredtextdocument(); doc.append(subdoc)
            subdoc.Class = 'description'
            subdoc_text = []
            
            # tip
            subdoc_text += tip.splitlines()
            
            # type
            subdoc_text.append('')
            subdoc_text.append('* type: %s' % d.type.__name__)
            
            # validator
            try:
                validator = d.validator
            except AttributeError:
                validator = None
            if validator:
                # choices
                if validator.__class__.__name__ == 'Choice':
                    subdoc_text.append('* allowed values: %s' % validator.value)
            subdoc.text = '\n'.join(subdoc_text)
                    
            continue
        return container


    def _createEventsDocument(self, events):
        container = luban.e.document()
        
        descriptiontext = """You can specify what actions to take when an event happens to a luban element. The event handlers listed below are attributes of the luban element. If you set an event handler to be an action, then that action will be performed whenever the event occurs. """
        description = container.restructuredtextdocument()
        description.Class = 'demo-description'
        description.text = descriptiontext

        for d in events:
            if hasattr(d, 'tip'): tip = d.tip
            else: tip = 'Please give a tip of property %s' % d.name
            
            title = d.name
            if hasattr(d, 'experimental') and d.experimental:
                title += '(experimental)'
            doc = container.document(title=title)
            doc.Class = 'api-item'

            instancename = self.object_type.__name__.lower()
            examplecode = instancename + '.' + d.name + ' = some_action'
            ex = doc.paragraph(text=examplecode)
            ex.Class = 'signature'
            
            p = doc.paragraph()
            p.text = tip
            p.Class = 'description' 
            continue
        return container


    skip_descriptors = []
    def _categorizeDescriptors(self, descriptors):
        'put descriptors into different categories such as properties, eventhandlers'
        r = {
            'properties': [],
            'events': [],
            }

        # contents is not really directly settable
        skip = self.skip_descriptors

        #
        from luban.ui.descriptors.EventHandler import EventHandler
        #
        for d in descriptors:
            if d.name in skip: continue
            if isinstance(d, EventHandler):
                r['events'].append(d)
            else:
                r['properties'].append(d)
            continue

        return r
    
    
    
    class DemoPanel:

        title = None # title of the panel
        actor_name = None # name of the actor. a demo actor needs to subclass .DemoPanelActor



# End of file 
