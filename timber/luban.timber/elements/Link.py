#!/usr/bin/env python
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


from .SimpleElement import SimpleElement as base


class Link(base):

    simple_description = 'A clickable element'
    full_description = (
        'Link is clickable. When clicked, an action will be triggered. '
        )

    abstract = False


    def identify(self, inspector):
        return inspector.onLink(self)


    label = descriptors.str()
    label.tip = 'label of the link'

    # if there is url, then there should probably be
    # no onclick action. how do we enforce that?
    url = descriptors.str()
    url.tip = 'url of the link will bring us to'
    
    tip = descriptors.str()
    tip.tip = 'tip for the link that shows up when hovered'
    tip.experimental = True
    
    
# version
__id__ = "$Id$"

# End of file 