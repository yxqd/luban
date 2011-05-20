#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.applications.Script import Script as base


class App(base):


    class Inventory(base.Inventory):

        import pyre.inventory

        import gongshuzi.components
        clerk = pyre.inventory.facility(name='clerk', factory=gongshuzi.components.clerk)


    def main(self):
        clerk = self.clerk
        orm = clerk.orm

        from luban.project.Project import Project
        ProjectTable = orm.getTable(Project)
        project = ProjectTable()
        project.id = 'fortest'
        try:
            clerk.insertNewRecord(project)
        except:
            pass

        from gongshuzi.dom.Session import Session
        session = Session()
        session.id = 'fortest'
        try:
            clerk.insertNewRecord(session)
        except:
            pass
        return        


    def _configure(self):
        super(App, self)._configure()
        
        self.clerk = self.inventory.clerk
        return        


    def _init(self):
        super(App, self)._init()
        return


import journal
journal.error('pyre.inventory').deactivate()


if __name__=='__main__':
    app=App(name='initdb')
    app.run()

# version
__id__ = "$Id$"

# End of file 
