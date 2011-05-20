# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# component handle pid store/retrieval


from pyre.components.Component import Component
class PIDStore(Component):

    class Inventory(Component.Inventory):

        import pyre.inventory


    def setPath(self, path):
        import os
        self.path = os.path.abspath(path)
        return


    def dump(self, pid):
        path = self.path
        stream = open(path, 'w')
        stream.write(str(pid))
        stream.close()
        return


    def load(self):
        path = self.path
        if not os.path.exists(path): return
        pid = int(open(path).read())
        return pid


    def __init__(self, name='pidstore', facility='pidstore'):
        super(PIDStore, self).__init__(name, facility)
        return


    def _configure(self):
        super(PIDStore, self)._configure()
        return


import os


# version
__id__ = "$Id$"

# End of file 
