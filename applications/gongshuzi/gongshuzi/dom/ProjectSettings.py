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


from Session import Project


from OwnedObject import OwnedObject as base

class ProjectSettings(base):

    name = 'projectsettings'
    
    import dsaw.db
    
    project = dsaw.db.reference(name='project', table=Project, backref='settings')

    port = dsaw.db.integer(name='port', default=8500)
    

    

# version
__id__ = "$Id$"

# End of file 
