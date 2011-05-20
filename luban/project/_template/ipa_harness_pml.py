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

    component = tag('component', {'name': 'ipa-harness'})
    inventory.content.append(component)

    property = tag('property', {'name': 'home'}, '../config')
    component.content.append(property)

    return inventory


# version
__id__ = "$Id$"

# End of file 
