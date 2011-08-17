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


"""
methods here create instances of action classes

Each action class describe one type of action.
Keep in mind that in luban.ui.actions we are using objects to 
hold information about actions, instead of actually
performing actions.
The desriptions in action objects will later be translated by renderers
to actual actions in different media.

Types of actions:

* selecting: select an element
* element actions: perform actions on selected element
* loading: load a luban object from controller. The object allowed -- see ..schema.Object
* misc actions: there is one such action -- alert

"""


#  for controller access
def load(*args, **kwds):
    from .Loading import Loading
    return Loading(*args, **kwds)


#  selector
def select(id=None, type=None, element=None):
    '''select(id=None, type=None, element=None) -> selector
    
This method returns an action to select a UI element.
The argument for this method would be either the unique id
of the element and optionaly its type, or the element itself.

The "element" parameter is preferred over other two inputs.

Examples::

  >>> select(id="okbuttonid")
  >>> select(id="okbuttonid", type="Button")
  >>> select(element=okbutton)

A selector can be used to further construct action on the
selected element. For example, the following code constructs
an action to destroy a document

  >>> select(element=doc).destroy()
  
'''
    if element is not None:
        id = element.id
        type=element.__class__.__unique_type_name__

    if id is None:
        m = "element %s does not have an id" % (element,)
        raise RuntimeError(m)

    from .SelectByIDandType import SelectByIDandType
    return SelectByIDandType(id=id, type=type)


#  alert
def alert(message):
    '''alert(message) -> action to pop up an alert window with the given message

Examples::

  >>> alert("please input your password")
  
'''
    from .SimpleAction import SimpleAction
    return SimpleAction(actionname='alert', message=message)


# common element actions
action_modules = [
    'ReplaceContent',
    ]
def importAllElementActions():
    modules = action_modules
    for name in modules:
        __import__(name, fromlist=['.'], globals=globals())
        continue
    return
importAllElementActions()


# version
__id__ = "$Id$"

# End of file 
