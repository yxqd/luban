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

base = workflow.actor
class Actor(base):

    expose = 1

    @luban.decorators.frameHandler
    def default(self):
        frame = luban.e.frame(title='test')
        
        context = 'main-login'
        luban.session['context'] = {
            'onsuccess': luban.a.alert("login succeed")
            }
        form = workflow.form_factory(context)
        
        frame.append(form)
        return frame

    pass


# End of file 
