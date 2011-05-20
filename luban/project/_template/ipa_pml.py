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

    component = tag('component', {'name': 'ipa'})
    inventory.content.append(component)

    props = [
        tag('property', {'name': 'port'}, '50001'),
        tag('property', {'name': 'ticketOnce'}, 'no'),
        tag('property', {'name': 'ticketDuration'}, '240*hour'),
        ]

    component.content += props

    return inventory


# version
__id__ = "$Id$"

# End of file 
