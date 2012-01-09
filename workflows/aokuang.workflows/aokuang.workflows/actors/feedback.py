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
http://localhost:22347/feedback?email=a@b.com
"""


import luban

from ..workflows.feedback import workflow
class Actor(workflow.Actor):

    expose = 1

    @luban.decorators.frameHandler
    def default(self, email, **kwds):

        # this is a hack. for real app, this should be
        # set somewhere else after user login, for example.
        luban.session['email'] = email
        
        # give this context a name
        context = 'feedback-demo'
        # build the action in case of successful sending the feedback
        onsuccess = luban.a.load(actor = self.name, routine = 'onsuccess')
        # and save the context in the session
        luban.session[context] = {
            'onsuccess': onsuccess,
            }
        
        dialog = workflow.visuals.dialog(context=context)

        #
        frame = luban.e.frame(title='test')

        #
        adddialog = luban.a.select(id='').append(newelement=dialog)
        button = frame.button(label='feedback', onclick=adddialog)

        return frame
    
    
    def onsuccess(self, **kwds):
        return
    
    pass


# End of file 
