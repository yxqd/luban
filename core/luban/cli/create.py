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


import os

def run(name, outdir = None, **kwds):
    outdir = outdir or '.'
    projdir = os.path.join(outdir, name)
    
    if os.path.exists(projdir):
        import shutil
        shutil.rmtree(projdir)

    from ..project import createProjectSkeleton
    createProjectSkeleton(name, outdir)
    return
    


# End of file 

