# -*- Python -*-
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


__doc__ = """
"""


def createExtensionSkeleton(name, outdir):
    from .Extension import Extension
    extension = Extension(name=name)
    
    import os
    extensiondir = os.path.join(outdir, name)
    if os.path.exists(extensiondir):
        raise IOError(extensiondir + " already exists")
    
    from .CreateExtensionInFS import Renderer
    Renderer().render(extension, outdir)
    
    return
    
    

# End of file 

