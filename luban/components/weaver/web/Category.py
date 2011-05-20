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


from pyre.inventory.Property import Property


class List(Property):

    '''different from the "official" List type in that it allows to splitlines

    by default, if there are new lines, split by lines
    there is no newline, split by comma
    '''


    def __init__(self, name, default=None, meta=None, validator=None):
        if default is None:
            default = []
        Property.__init__(self, name, "list", default, meta, validator)
        return


    def _cast(self, value):
        if isinstance(value, basestring):
            if value and value[0] in '[({':
                value = value[1:]
            if value and value[-1] in '])}':
                value = value[:-1]

            if not value:
                return []

            if value.find('\n') != -1:
                value = value.splitlines()
                value = [e.strip() for e in value if e.strip()]
                return value
            
            value = value.split(",")
            return value

        if isinstance(value, list):
            return value
            
        raise TypeError("property '%s': could not convert '%s' to a list" % (self.name, value))
    



from pyre.components.Component import Component

class Category(Component):

    class Inventory(Component.Inventory):

        import pyre.inventory
        stylesheets = List(name='stylesheets')
        javascripts = List(name='javascripts')


    def __init__(self, name):
        super(Category, self).__init__(name, 'luban-web-weaver-library-category')
        return


    def _configure(self):
        super(Category, self)._configure()
        self.stylesheets = self.inventory.stylesheets
        self.javascripts = self.inventory.javascripts
        return


# version
__id__ = "$Id$"

# End of file 
