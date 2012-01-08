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


import luban

from ..workflows.login import workflow
class Actor(workflow.Actor):

    expose = 1

    @luban.decorators.frameHandler
    def default(self):
        # give this context a name
        context = 'main-gate'
        # build the action in case of successful authentication
        onsuccess = luban.a.load(actor = self.name, routine = 'onsuccess')
        # and save the context in the session
        luban.session[context] = {
            'onsuccess': onsuccess,
            }
        
        # when constructing the form, make sure
        # that it knows in which context this form is
        # so that after authentication, correct action will
        # be carried out
        form = workflow.visuals.form(context=context)

        #
        frame = luban.e.frame(title='test')
        frame.append(form)
        return frame
    
    
    def onsuccess(self, **kwds):
        welcome = luban.e.document(title='Welcome')
        return luban.a.select(id='').replaceContent(newcontent=welcome)
    
    pass


# End of file 
