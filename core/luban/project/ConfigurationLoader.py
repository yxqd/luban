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


class ConfigurationLoader:

    def load(self, filename):
        import os, sys
        filename = os.path.abspath(filename)
        dir = os.path.dirname(filename)
        sys.path.insert(0, dir)
        print (sys.path)
        import conf
        from .Project import Project
        p = Project('p')
        for k in conf.__dict__:
            if k.startswith('_'):
                continue
            setattr(p, k, getattr(conf, k))
            continue
        return p


# End of file 

