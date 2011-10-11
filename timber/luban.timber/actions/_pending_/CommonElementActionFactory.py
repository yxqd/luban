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


    def before(self, newelement):
        '''
insert the give new element just in front of me.
The new element will be one of my siblings.
'''
        from .InsertBeforeElement import InsertBeforeElement
        return InsertBeforeElement(element=self, newelement=newelement)


    def destroy(self):
        '''destroy me'''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='destroy')
    

    def getAttr(self, name):
        '''get value of my attribute. name is the name of the attribute'''
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(element=self, actionname='getAttribute', name=name)


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

