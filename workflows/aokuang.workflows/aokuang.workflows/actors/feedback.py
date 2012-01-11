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
http://example.com/feedback?email=a@b.com
"""


import luban

from ..workflows.feedback import workflow; workflow=workflow()
class Actor(workflow.Actor):

    expose = 1

    @luban.decorators.frameHandler
    def default(self, email, **kwds):

        # Store user email in session. Later it will be used
        # in constructing the feedback email.
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # The implementation here is a hack for demo purpose.
        # For a real app, this should not come from arguments;
        # it should be obtained from database, for example.
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        luban.session['email'] = email
        
        # give this context a name
        context = 'feedback-demo'
        # build the action in case of successful sending the feedback
        onsuccess = luban.a.load(actor = self.name, routine = 'onsuccess')
        # and save the context in the session
        luban.session[context] = {'onsuccess': onsuccess}

        # create the feedback button
        button = workflow.visuals.button(context=context)
        
        # test frame
        frame = luban.e.frame(title='test')
        frame.append(button)
        return frame
    
    
    def onsuccess(self, **kwds):
        return
    
    pass


# End of file 
