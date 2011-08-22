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

"""
meta classes
"""

from .SubclassDefinitionContextBuilder import SubclassDefinitionContextBuilder
from .DescriptorCollector import DescriptorCollector
from .TypeRegistryCurator import TypeRegistryCurator
class Meta(SubclassDefinitionContextBuilder, TypeRegistryCurator, DescriptorCollector):
    pass


# End of file 
