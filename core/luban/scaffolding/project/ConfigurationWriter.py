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
see also .ConfigurationLoader
"""


class ConfigurationWriter:

    
    from .Project import relpaths

    def dump(self, project):
        import os, sys
        root = os.path.abspath(project.root)
        filename = os.path.join(root, 'conf.py')
        content = self._createContent(project)
        open(filename, 'w').write(content)
        return filename


    def _createContent(self, project):
        import os
        pairs = {}

        # get data from project object
        rootlen = len(project.root)+1
        for k in project.__dict__:
            if k.startswith('_'): continue
            v = getattr(project, k)
            # convert absolute paths to relative paths
            if k in self.relpaths:
                v = os.path.abspath(v)
                if v.startswith(project.root):
                    v = os.path.abspath(v)[rootlen:]
            pairs[k] = v
            continue
        
        return '\n'.join( "%s=%r" % (k,v) for k,v in pairs.items() )


# End of file 

