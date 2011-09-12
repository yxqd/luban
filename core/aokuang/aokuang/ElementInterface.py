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


from .ObjectInterface import Factory as base
class Factory(base):


    object_type = None # target object type this factory will build interface for
    actor = None # name of the actor for this interface
    demo_panels = None # a list of demo panels, each an instance of DemoPanel
    skip_descriptors = ['lubanelement']
    api_categories = ['properties', 'events', 'actions']
    

    def _createActionsDocument(self, actions):
        container = lui.e.document()

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
        descdoc = lui.e.restructuredtextdocument(); container.append(descdoc)
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


    def _categorizeDescriptors(self, descriptors):
        'put descriptors into different categories such as properties, eventhandlers'
        r = super()._categorizeDescriptors(descriptors)

        # actions are not really descriptors
        r['actions'] = findActions(self.object_type)
        return r


def getActionFactorySignature(action):
    from luban.ui.descriptors.EventHandler import EventHandler
    descriptors = []
    skip = 'lubanaction', 'element'
    for descriptor in action.iterDescriptors():
        # XXXXXXXXXXXXXXXXXXXX
        # skip event handlers for now
        if isinstance(descriptor, EventHandler):
            continue
        if descriptor.name in skip:
            continue
        descriptors.append(descriptor)
        continue
    return action.getCtorDocStr(
        ctor_name = action.factory_method,
        descriptors = descriptors,
        )



def findActions(type):
    ret = []
    from luban.ui.actions._element_action_registry import all_action_classes
    for (element_type, factory), action in all_action_classes.items():
        if element_type is None or element_type is type:
            ret.append(action)
        continue
    return ret
    

# End of file 
