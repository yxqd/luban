# -*- Python -*-
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


from .Inspector import Inspector

class Writer(Inspector):


    def render(self, entry, rootpath='.', overwrite=False):
        self._currentpath = rootpath
        self._overwrite = overwrite
        return entry.identify(self)


    def onDirectory(self, directory):

        path = os.path.join(self._currentpath, directory.name)

        debug.log('onDirectory: path=%s' % path)
        
        if os.path.exists(path):
            if not self._overwrite:
                raise RuntimeError("%s already exists" % path)
        else:
            os.makedirs(path)
            
        for entry in directory.entries.values():
            self._currentpath = path
            entry.identify(self)
            continue
        return


    def onFile(self, file):
        content = file.content or ''
        path = os.path.join(self._currentpath, file.name)

        if os.path.exists(path):
            if not self._overwrite:
                raise RuntimeError("%s already exists" % path)

        open(path, 'w').write(content)

        if file.executable:
            os.system('chmod +x %s' % os.path.abspath(path))
        return


    def onSymLink(self, link):
        path = os.path.join(self._currentpath, link.name)
        if os.path.exists(path):
            if not self._overwrite:
                raise RuntimeError("%s already exists" % path)
            os.remove(path)

        try:
            os.symlink(link.target, path)
        except:
            import traceback; tb = traceback.format_exc()
            msg = 'Failed to make symlink %r to %r.  Original traceback:\n%s'
            msg = msg % (path, link.target, tb)
            raise RuntimeError(msg)
        return


import os

import journal
debug = journal.debug('luban._filesystem.Writer')

# version
__id__ = "$Id$"

# End of file 
