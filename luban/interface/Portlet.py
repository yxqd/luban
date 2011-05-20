#!/usr/bin/env python
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


from SimpleContainer import SimpleContainer as base


class Portlet(base):

    simple_description = 'provides users access to dynamic content'
    full_description = (
        'A portlet usually is a small window. It contains items that, '
        'when clicked, lead to loading of dynamic content of UI. '
        'A portlet has a title which can be empty, and its children '
        'are of type PortletItem.'
        )
    
    
    abstract = False

    def item(self, **kwds):
        from PortletItem import PortletItem
        pi = PortletItem(**kwds)
        self.add(pi)
        return pi


    def identify(self, inspector):
        return inspector.onPortlet(self)


    title = base.descriptors.str(name='title')
    title.tip = 'Title of the portlet'


# version
__id__ = "$Id$"

# End of file 
