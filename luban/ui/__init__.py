# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

__doc__ = """ luban.ui
"""

example1 = """
import luban.ui as lu

doc = lu.e.document(title="hello")
doc.onclick = lu.a.select(element=doc).replaceContent(
    newcontent = lu.e.paragraph(text='world'))

"""


class ElementClassProxy:


    def __getattr__(self, name):
        from .elements._registry import fundamental_elements
        e = fundamental_elements.getElementClass(name)
        if e is None:
            raise AttributeError(name)
        return e


e = ElementClassProxy()
del ElementClassProxy


from . import elements, actions
a = actions

registerElementProvider = elements.registerElementProvider


# version
__id__ = "$Id$"

# End of file 
