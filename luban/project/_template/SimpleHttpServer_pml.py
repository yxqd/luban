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
    return tag2xmltxt(inventory(project, Tag))


def inventory(project, tagfactory):
    tag = tagfactory

    inventory = tag('inventory')

    component = tag('component', {'name': 'SimpleHttpServer'})
    inventory.content.append(component)

    port = 8801
    if hasattr(project, 'port'): port = project.port
    
    property = tag('property', {'name': 'port'}, '%s' % port)
    component.content.append(property)

    return inventory


# version
__id__ = "$Id$"

# End of file 
