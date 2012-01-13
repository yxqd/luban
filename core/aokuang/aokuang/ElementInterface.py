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


from .ObjectInterface import Factory as base
class Factory(base):


    object_type = None # target object type this factory will build interface for
    actor = None # name of the actor for this interface
    demo_panels = None # a list of demo panels, each an instance of DemoPanel
    skip_descriptors = ['lubanelement']
    api_categories = ['properties', 'subelements', 'events', 'actions']


    def create(self):
        from luban import py_major_ver
        if py_major_ver == 2:
            superme = super(Root, self)
        elif py_major_ver == 3:
            superme = super()
        container = superme.create()

        impldoc = self._createImplDocument()
        impldoc.Class = 'section-container'
        container.append(impldoc)
        return container
        
        
    def _createImplDocument(self):
        from luban.weaver.web.Library import Library
        name = self.object_type.__unique_type_name__
        try:
            lib = Library.get('luban.widgets.%s' % name)
        except KeyError:
            return luban.e.document()
        deps = lib.dependencies
        if not deps: return luban.e.document()

        impl = luban.e.document(title='Javascript widget library dependencies:')
        for dep in deps:
            dep = Library.get(dep)
            text = '<a class="ext" href="%s" target="_blank">%s</a>' % (
                dep.website, dep.name)
            impl.htmldocument(text=text)
            continue
        return impl
    
        
    def _createSubelementsDocument(self, subelements):
        # sort factories
        def get0(t): return t[0]
        subelements.sort(key=get0)
        
        # 
        container = luban.e.document()

        # 
        descriptions = [
            'The following are factory methods to create sub-elements. ',
            'A factory method to create a subelement usually has a signature ',
            "identical to that of the subelement's constructor. ",
            'Click on an factory method for its signature. ',
            ]
        descriptions = '\n'.join(descriptions)
        descdoc = container.restructuredtextdocument()
        descdoc.Class = 'demo-description'
        descdoc.text = descriptions
        
        instance = self.object_type() # instance to help create documentation
        
        # loop over sub element factories
        counter = 0; n = 4
        for name, type in subelements:
            b = container.button(label=name)
            b.Class = 'link'
            docstr = getattr(instance, name).__doc__
            helpdoc = luban.e.htmldocument(text = '<pre>'+docstr + '</pre>')
            b.onclick = luban.a.select(id='subelement-factory-help')\
                .replaceContent(newcontent = helpdoc)

            if counter == n-1: container.paragraph(); counter = 0
            else: counter+=1
            continue
        
        #
        container.document(id='subelement-factory-help').paragraph()
        
        return container
    

    def _createActionsDocument(self, actions):
        container = luban.e.document()

        descriptions = [
            'The following are methods to create actions for an element(widget).',
            'Any of these methods has to be called by a selector that selects the widget.',
            'For example the method "addClass" below can be used to create an',
            'action to add a class to a button widget by ::',
            '',
            '  select(id="buttonid").addClass(cls="big-button")',
            '',
            'Pleaset note that the above method returns an action, and the action',
            'can be assigned to an event handler.',
            '',
            # 'Expand any section below for details of each action.',
            ]
        descriptions = '\n'.join(descriptions)
        descdoc = luban.e.restructuredtextdocument(); container.append(descdoc)
        descdoc.Class = 'demo-description'
        descdoc.text = descriptions

        for action in actions:            
            title = action.factory_method
            if hasattr(action, 'experimental') and action.experimental:
                title += '(experimental)'
            doc = container.document(title=title)
            doc.Class = 'api-item'
            
            ctordoc = getActionFactorySignature(action)
            sig = "selector.%s" % ctordoc
            sigp = doc.paragraph(text=sig)
            sigp.Class = ['signature']
            
            p = doc.paragraph()
            p.text = action.__doc__
            p.Class = ['description']
            continue
        return container


    def _createSubelementsDescriptor(self):
        factories = self.object_type.elementfactories()
        # build a list of (name, type) tuples
        ret = []
        for name in factories:
            type = getattr(self.object_type(), name)().__class__
            ret.append( (name, type) )
            continue
        return ret


    def _categorizeDescriptors(self, descriptors):
        'put descriptors into different categories such as properties, eventhandlers'
        from luban import py_major_ver
        if py_major_ver == 2:
            r = super(Factory, self)._categorizeDescriptors(descriptors)
        elif py_major_ver == 3:
            r = super()._categorizeDescriptors(descriptors)

        # actions are not really descriptors
        r['actions'] = findActions(self.object_type)
        
        from luban.ui.elements.ElementContainer import isContainerType
        if isContainerType(self.object_type):
            r['subelements'] = self._createSubelementsDescriptor()
        return r


def getActionFactorySignature(action):
    return action.getCtorDocStr(ctor_name=action.factory_method)


def findActions(type):
    ret = []
    from luban.ui.actions._element_action_registry import all_action_classes
    for (element_type, factory), action in all_action_classes.items():
        if element_type is None or element_type is type:
            ret.append(action)
        continue
    return ret
    

# End of file 
