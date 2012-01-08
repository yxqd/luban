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
        frame = luban.e.frame(title='test')
        
        context = 'main-gate'
        
        onsuccess = luban.a.load(actor = self.name, routine = 'onsuccess')
        luban.session[context] = {
            'onsuccess': onsuccess,
            }
        form = workflow.visuals.form(context=context)
        
        frame.append(form)
        return frame


    def onsuccess(self, **kwds):
        welcome = luban.e.document(title='Welcome')
        return luban.a.select(id='').replaceContent(newcontent=welcome)

    pass


# End of file 
