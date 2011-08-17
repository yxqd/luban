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

doc = lu.e.document(title="hello", id="mydoc")
doc.onclick = lu.a.select(element=doc).replaceContent(
    newcontent = lu.e.paragraph(text='world'))

"""


TODO = """
* implement the idea of "template". 
  should allow to define "facility" in a subclass of an elementcontainer type,
  and call it a template. those template classes should have 
  a normal "template" attribute that is True.
  instances of a template is a element hierarchy
* think about creating a proxy to actions
"""


# proxy to elements
class ElementClassProxy:


    def __getattr__(self, name):
        from .elements._registry import element_types
        e = element_types.getElementClass(name)
        if e is None:
            raise AttributeError(name)
        return e


e = ElementClassProxy()
del ElementClassProxy


# actions
from . import elements, actions
a = actions



# version
__id__ = "$Id$"

# End of file 
