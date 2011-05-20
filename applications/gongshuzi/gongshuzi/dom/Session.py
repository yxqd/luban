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


from luban.project.Project import Project
import orm
Project = orm.AttributeContainer2Table(Project)


from OwnedObject import OwnedObject as base


# the session to edit a project
class Session(base):

    name = 'sessions'
    
    import dsaw.db
    
    project = dsaw.db.reference(name='project', table=Project)

    categoryselection = dsaw.db.varchar(name='categoryselection', default='visuals', length=16)
    
    current_visual = dsaw.db.versatileReference(name='current_visual')
    current_actor = dsaw.db.versatileReference(name='current_actor')

    current_document = dsaw.db.versatileReference(name='current_document')
    current_action = dsaw.db.versatileReference(name='current_action')

    

# version
__id__ = "$Id$"

# End of file 
