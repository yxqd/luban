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


from luban import ui as lui


class Factory:


    object_type = None # target object type this factory will build interface for
    actor = None # name of the actor for this interface
    demo_panels = None # a list of demo panels, each an instance of DemoPanel
    

    def create(self):
        container = lui.e.document()

        object_type = self.object_type
        if hasattr(object_type, 'experimental') and object_type.experimental:
            p = container.paragraph(text='This is still experimental')

        # the demo document
        doc = self._createDemoDocument()
        doc.title = 'Demos'
        doc.Class = 'demo-document'
        container.append(doc)

        # the api document
        doc = self._createAPIDocument()
        doc.title = 'API'
        container.append(doc)
        return container


    def _createDemoDocument(self):
        """create demo document 
        """
        # container
        container = lui.e.document(name='demo-document')
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
                
            tab.onselect = lui.a.select(element=tab).replaceContent(
                newcontent=lui.a.load(actor=actor, routine=routine)
                )
            continue

        return container


    def _createAPIDocument(self):
        object_type = self.object_type
        descriptors = object_type.iterDescriptors()
        descriptors = self._categorizeDescriptors(descriptors)
        
        doc = lui.e.document(name='api-document')
        tabs = lui.e.tabs(); doc.append(tabs)
        #
        tab1 = tabs.tab(label='Introduction')
        d = self._createIntroductionDocument(descriptors); tab1.append(d)
        #
        tab2 = tabs.tab(label='Properties')
        d = self._createPropertiesDocument(descriptors['properties']); tab2.append(d)
        #
        return doc
    

    def _createIntroductionDocument(self, descriptors):
        d = lui.e.restructuredtextdocument()
        object_type = self.object_type
        title = "%s: %s" % (object_type.__name__, object_type.simple_description)
        title = '%s\n%s\n' % (title, '-'*len(title))
        description = object_type.full_description

        ctordoctitle = 'signature'
        ctordoctitle = '%s\n%s\n' % (ctordoctitle, '^'*len(ctordoctitle))
        lines = object_type.__init__.__doc__
        lines = lines and lines.splitlines()
        if not lines:
            props = descriptors['properties']
            lines = self._getCtorDocString(object_type, props).splitlines()
        ctordoc = [' '+line for line in lines]
        ctordoc = ['::\n'] + ctordoc
        
        text = [title, description, '', ctordoctitle]+ ctordoc
        d.text = '\n'.join(text)
        return d


    def _createPropertiesDocument(self, props):
        container = lui.e.document()

        # explanation
        descdoc = lui.e.restructuredtextdocument(); container.append(descdoc)
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
            subdoc = lui.e.restructuredtextdocument(); doc.append(subdoc)
            subdoc.Class = 'description'
            subdoc_text = []

            # tip
            subdoc_text += tip.splitlines()

            # type
            subdoc_text.append('')
            subdoc_text.append('* type: %s' % d.type)

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


    skip_descriptors = []
    def _categorizeDescriptors(self, descriptors):
        'put descriptors into different categories such as properties, eventhandlers'
        r = {
            'properties': [],
            }

        # contents is not really directly settable
        skip = self.skip_descriptors

        for d in descriptors:
            if d.name in skip: continue
            r['properties'].append(d)
            continue

        return r



    def _getCtorDocString(self, object_type, descriptors):
        return object_type.getCtorDocStr(descriptors)
    


    class DemoPanel:

        title = None # title of the panel
        actor_name = None # name of the actor. a demo actor needs to subclass .DemoPanelActor



# End of file 
