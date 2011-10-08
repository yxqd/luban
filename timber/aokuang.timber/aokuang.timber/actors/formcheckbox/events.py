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

    title='A form with a check box'
    description = [
        'The check box is attached with event hanlders for ',
        '"change", "focus", and "blur" events.',
        ]
    def createDemoPanel(self, **kwds):
        doc = luban.e.document()
        form = doc.form(title='form')
        check1 = form.checkbox(name='check1', label='check box 1')
        log = doc.document(id='log', Class='log', title='log')
        
        check1.onchange = luban.a.load(
            actor=self.name, routine='onchange',
            old = luban.event.old, new = luban.event.new
            )
        check1.onfocus = luban.a.select(element=log).append(
            newelement=luban.e.paragraph(text="focused")
            )
        check1.onblur = luban.a.select(element=log).append(
            newelement=luban.e.paragraph(text="blured")
            )
        return doc


    def onchange(self, old=None, new=None, **kwds):
        msg = "value changed from %r to %r" % (old, new)
        newelement = luban.e.paragraph(text = msg)
        return luban.a.select(id='log').append(newelement=newelement)


# End of file 
