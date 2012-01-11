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


"""
see also .ConfigurationWriter
"""


class ConfigurationLoader:


    from .Project import relpaths
    
    
    def load(self, filename):
        import os, sys
        filename = os.path.abspath(filename)
        dir = os.path.dirname(filename)
        sys.path.insert(0, dir)
        import conf
        from .Project import Project
        project = Project(conf.name)
        # get data from conf file
        for k in conf.__dict__:
            if k.startswith('_'):
                continue
            setattr(project, k, getattr(conf, k))
            continue

        # update relative paths to absolute paths
        for p in self.relpaths:
            v = getattr(project, p)
            v = os.path.join(dir, v)
            setattr(project, p, v)
            continue

        project.root = dir
        
        return project


# End of file 

