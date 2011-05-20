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


def generate(project):
    from _xmlrep import Tag
    from _tag2xml import tag2xmltxt
    return tag2xmltxt(inventory(Tag))


def inventory(tagfactory):
    tag = tagfactory

    inventory = tag('inventory')

    component = tag('component', {'name': 'librarian'})
    inventory.content.append(component)

    props = [
        tag('property', {'name': 'cssbase'}, 'css'),
        tag('property', {'name': 'jsbase'}, 'javascripts'),
        ]
    component.content += props

    return inventory


# version
__id__ = "$Id$"

# End of file 
