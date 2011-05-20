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


from pyre.applications.Script import Script

class ProjectScriptBase(Script):

    class Inventory(Script.Inventory):

        import pyre.inventory
        project = pyre.inventory.str('project', default='')
        

    def __init__(self, name):
        super(ProjectScriptBase, self).__init__(name)
        self._getProjectNameFromSysArgv()
        return


    def _configure(self):
        super(ProjectScriptBase, self)._configure()
        self.project = self.inventory.project
        return


    def _getProjectNameFromSysArgv(self):
        """
support 
    <script> <projectname>
and also
    <script> --project=<projectname>

problem: not work if project name starts with '-'.
        """
        import sys
        argv = sys.argv
        if len(argv) > 1:
            last = argv[-1]
            if not last.startswith('-'):
                # assume it is the project name argument
                argv[-1] = '--project=%s' % last
        return

        
# version
__id__ = "$Id$"

# End of file 
