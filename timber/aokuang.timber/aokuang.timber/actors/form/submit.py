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

from ....DemoPanelActor import Actor as base
class Actor(base):

    title='Two forms, each with a submit button'
    description = [
        "Please pay special attention on how the form data is passed to the handler method",
        ]


    def createDemoPanel(self, **kwds):
        container = luban.e.document()
        
        # form 1
        form1 = container.form(title='login')
        username = form1.text(label='username', name='username')
        submit = form1.submitbutton(label="Submit")
        # "kwds" is a magic word, the data will be passed to handler method as **kwds
        # usually, we should use this convention.
        form1.onsubmit = luban.a.load(
            actor = self.name, routine = 'onsubmit', 
            kwds = luban.event.data,
            )
        
        # form 2
        form2 = container.form(title='login')
        username = form2.text(label='username', name='username')
        submit = form2.submitbutton(label="Submit")
        # if "kwds" is not used, raw string format json representation
        # of form data will be passed to the handler method.
        # use this one when you need more control of parsing input data.
        form2.onsubmit = luban.a.load(
            actor = self.name, routine = 'onsubmit', 
            data = luban.event.data,
            )
        
        return container


    def onsubmit(self, data=None, **kwds):
        s = "data: %s, kwds: %s" % (data, kwds)
        return luban.a.alert(s)


# End of file 
