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


from .decorators import experimental

class CommonElementActionFactory:

    def find(self, name=None, type=None):
        '''find descendents by name and/or type and select them '''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='find', name=name, type=type)
    

    def empty(self):
        '''empty me (remove all my children) '''
        from .RemoveContent import RemoveContent
        return RemoveContent(element=self)

    @experimental
    def findDescendentIDs(self, type):
        '''find ids of my descendents given the type '''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='findDescendentIDs', type=type)


    def replaceContent(self, newcontent):
        '''replace my content with the given new content '''
        from .ReplaceContent import ReplaceContent
        return ReplaceContent(element=self, newcontent=newcontent)


    def before(self, newelement):
        '''
insert the give new element just in front of me.
The new element will be one of my siblings.
'''
        from .InsertBeforeElement import InsertBeforeElement
        return InsertBeforeElement(element=self, newelement=newelement)


    def replaceBy(self, newelement):
        '''replace me by the new element '''
        from .ReplaceElement import ReplaceElement
        return ReplaceElement(element=self, newelement=newelement)


    def append(self, newelement):
        '''append the new element to the end of my children '''
        from .AppendElement import AppendElement
        return AppendElement(element=newelement, container=self)


    def destroy(self):
        '''destroy me'''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='destroy')
    

    def notify(self, event, actor, routine=None, **params):
        '''notify the controller that the given event happened.
The controller will invoke the given actor at the given routine
with data associated with the event.
Additional data are specified as keyword arguments.
'''
        from .Notification import Notification
        return Notification(self, event, actor, routine=routine, **params)


    def setAttr(self, **params):
        '''set my attributes. Eg. setAttr(key1=val1, key2=val2,...)'''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='setAttribute', **params)


    def getAttr(self, name):
        '''get value of my attribute. name is the name of the attribute'''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='getAttribute', name=name)


    def addClass(self, Class):
        '''add a Class to me'''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='addClass', Class=Class)


    def removeClass(self, Class):
        '''remove a Class from me'''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='removeClass', Class=Class)


    def show(self):
        '''show me. If a widget was hidden originally, this action makes it show up'''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='show')
    

    def hide(self):
        '''hide me. If a widget was hidden originally, this action makes it show up'''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='hide')
    

    def enable(self):
        '''enable me'''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='enable')
    

    def disable(self):
        '''disable me'''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='disable')


    def focus(self):
        '''focus on me'''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='focus')
    

    def __getattr__(self, name):
        # for unimplemented element-specific actions, use a default
        # handler
        return self._elementSpecificAction


    def _elementSpecificAction(self, actionname, **kwds):
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(self, actionname, **kwds)
    
    pass


# End of file 

