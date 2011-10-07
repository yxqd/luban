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

    title='input fields and event handlers'
    description = [
        'The input fields are attached with event handlers for ',
        '"change", "focus", and "blur" events',
        ]


    logid = "form_withinputs-log"

    def createDemoPanel(self, **kwds):
        doc = luban.e.document()
        form = doc.form(title='login')
        username = form.text(label='username')
        password = form.password(label='password')
        comment = form.textarea(label='comment')
        log = doc.document(id=self.logid, Class='log', title='log')
        
        username.onchange = luban.a.load(
            actor=self.name, routine='onchange',
            old = luban.event.old, new = luban.event.new, 
            field='username'
            )
        username.onfocus = luban.a.select(element=log).append(
            newelement=luban.e.paragraph(text="username focused")
            )
        username.onblur = luban.a.select(element=log).append(
            newelement=luban.e.paragraph(text="username blured")
            )
        
        password.onchange = luban.a.load(
            actor=self.name, routine='onchange',
            old = luban.event.old, new = luban.event.new,
            field = 'password',
            )
        password.onfocus = luban.a.select(element=log).append(
            newelement=luban.e.paragraph(text="password focused")
            )
        password.onblur = luban.a.select(element=log).append(
            newelement=luban.e.paragraph(text="password blured")
            )

        comment.onchange = luban.a.load(
            actor=self.name, routine='onchange',
            old = luban.event.old, new = luban.event.new,
            field = 'comment',
            )
        comment.onfocus = luban.a.select(element=log).append(
            newelement=luban.e.paragraph(text="comment focused")
            )
        comment.onblur = luban.a.select(element=log).append(
            newelement=luban.e.paragraph(text="comment blured")
            )

        return doc


    def onchange(self, old=None, new=None, field=None, **kwds):
        msg = "field %r: value changed from %r to %r" % (field, old, new)
        newelement = luban.e.paragraph(text = msg)
        return luban.a.select(id=self.logid).append(newelement=newelement)


# End of file 
