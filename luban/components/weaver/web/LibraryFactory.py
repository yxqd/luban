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


def create(categories):
    from pyre.components.Component import Component

    class Library(Component):

        class Inventory(Component.Inventory):

            import pyre.inventory

            from Category import Category
            for category in categories:
                code = '%(name)s = pyre.inventory.facility(name=%(name)r, factory=Category, args=[%(name)r])' % {'name': category}
                exec code in locals()
                continue


        def __init__(self):
            super(Library, self).__init__('web-weaver-library', 'luban-web-weaver-library')
            return


        def _configure(self):
            super(Library, self)._configure()
            # transfer from inventory to self
            for category in categories:
                v = getattr(self.inventory, category)
                setattr(self, category, v)
                continue
            return

    Library.categories = categories
    return Library


def getCategories(providers=None):
    if not providers:
        from luban.content._accountant import element_providers as providers
        
    categories = ['base', 'application']
    from luban.content._accountant import getElementClassesRecursivley

    import warnings
    warnings.simplefilter('ignore')
    elementtypes = getElementClassesRecursivley(packages=providers)
    warnings.simplefilter('default')

    elementtypes = [t.__name__ for t in elementtypes]
    categories += [t.lower() for t in elementtypes]
    return categories
    

# version
__id__ = "$Id$"

# End of file 
