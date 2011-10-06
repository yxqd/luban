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

    title='A form with one text field'
    description = [
        'The text field is attached with event hanlders for ',
        '"change", "focus", and "blur" events',
        ]
    def createDemoPanel(self, **kwds):
        doc = luban.e.document()
        form = doc.form(title='login')
        username = form.text(label='username')
        log = doc.document(id='log', Class='log', title='log')
        
        username.onchange = luban.a.load(
            actor=self.name, routine='onchange',
            old = luban.event.old, new = luban.event.new
            )
        username.onfocus = luban.a.select(element=log).append(
            newelement=luban.e.paragraph(text="focused")
            )
        username.onblur = luban.a.select(element=log).append(
            newelement=luban.e.paragraph(text="blured")
            )
        
        return doc


    def onchange(self, old=None, new=None, **kwds):
        msg = "value changed from %r to %r" % (old, new)
        newelement = luban.e.paragraph(text = msg)
        return luban.a.select(id='log').append(newelement=newelement)


# End of file 
