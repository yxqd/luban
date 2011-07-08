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


import warnings
warnings.warn('''
  "page" is obsolete, please use "frame":

  >>> import luban.ui.elements
  >>> frame = luban.ui.elements.frame(...)
  ''')


from .Frame import Frame as Page
    

# version
__id__ = "$Id$"

# End of file
