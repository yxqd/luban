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

    component = tag('component', {'name': 'journal'})
    inventory.content.append(component)

    device = tag('facility', {'name': 'device'}, 'remote')
    component.content.append(device)

    info = tag('component', {'name': 'info'})
    info.content.append(
        tag('property', {'name': 'ipa'}, 'on')
        )
    component.content.append(info)
    
    debug = tag('component', {'name': 'debug'})
    debug.content.append(
        tag('property', {'name': 'ipa'}, 'on')
        )
    component.content.append(debug)
    
    return inventory


# version
__id__ = "$Id$"

# End of file 
