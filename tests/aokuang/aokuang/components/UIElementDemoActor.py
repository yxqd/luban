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

from DemoActor import Actor as base, panel, example, quickpanel

class Actor(base):


    element = None
    

    def createDemoDocument(self, director):
        container = lc.document()

        element = self.element
        if hasattr(element, 'experimental') and element.experimental:
            p = container.paragraph(text='This is still experimental')

        # the demo panel
        doc = self._createSwitcher(director)
        doc.title = 'Demos'
        doc.collapsable = True
        doc.Class = 'demo-document'
        container.add(doc)

        # the api panel
        doc = self._createAPIDocument(director)
        doc.title = 'API'
        doc.collapsable = True
        container.add(doc)
        return container


    def _createAPIDocument(self, director):
        element = self.element
        descriptors = element.getDescriptors()
        descriptors = self._categorizeDescriptors(descriptors)
        
        doc = lc.document()
        tabs = lc.tabs(); doc.add(tabs)
        #
        tab1 = tabs.tab(label='Introduction')
        d = self._createIntroductionDocument(descriptors); tab1.add(d)
        #
        tab2 = tabs.tab(label='Properties')
        d = self._createPropertiesDocument(descriptors['properties']); tab2.add(d)
        #
        return doc
    

    def _createIntroductionDocument(self, descriptors):
        d = lc.restructuredtextdocument()
        element = self.element
        title = "%s: %s" % (element.__name__, element.simple_description)
        title = '%s\n%s\n' % (title, '-'*len(title))
        description = element.full_description

        ctordoctitle = 'signature'
        ctordoctitle = '%s\n%s\n' % (ctordoctitle, '^'*len(ctordoctitle))
        lines = element.__init__.__doc__
        lines = lines and lines.splitlines()
        if not lines:
            props = descriptors['properties']
            lines = self._getElementCtorDocString(element, props).splitlines()
        ctordoc = [' '+line for line in lines]
        ctordoc = ['::\n'] + ctordoc
        
        d.text = [title, description, '', ctordoctitle]+ ctordoc
        return d


    def _createPropertiesDocument(self, props):
        container = lc.document()

        # explanation
        descdoc = lc.restructuredtextdocument(); container.add(descdoc)
        descdoc.Class = 'demo-description'
        descdoc.text = ['expand an item for details']
        
        for d in props:
            if hasattr(d, 'tip'): tip = d.tip
            else: tip = 'Please give a tip of property %s' % d.name

            # the document
            doc = container.document(collapsable=True, collapsed=True)
            doc.Class = 'api-item'

            # title
            title = d.name
            if hasattr(d, 'experimental') and d.experimental:
                title += '(experimental)'
            doc.title = title

            # subdocument
            subdoc = lc.restructuredtextdocument(); doc.add(subdoc)
            subdoc.Class = 'description'
            subdoc.text = []

            # tip
            subdoc.text += tip.splitlines()

            # type
            subdoc.text.append('')
            subdoc.text.append('* type: %s' % d.type)

            # validator
            validator = d.validator
            if validator:
                # choices
                if validator.__class__.__name__ == 'Choice':
                    subdoc.text.append('* allowed values: %s' % validator.value)
                    
            continue
        return container


    def _categorizeDescriptors(self, descriptors):
        'put descriptors into different categories such as properties, eventhandlers'
        r = {
            'properties': [],
            }

        # contents is not really directly settable
        skip = []

        for d in descriptors:
            if d.name in skip: continue
            r['properties'].append(d)
            continue

        return r



    def _getElementCtorDocString(self, element, descriptors):
        return element.getCtorDocStr(descriptors)
    


#version
__id__ = "$Id$"

# End of file 
