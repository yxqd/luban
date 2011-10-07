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

    title='A form with one selector field'
    description = [
        'The selector field is attached with event hanlders for ',
        '"change", "focus", and "blur" events',
        ]
    def createDemoPanel(self, **kwds):
        doc = luban.e.document()
        form = doc.form(title='login')
        entries = [
            ('male', 'Male'),
            ('female', 'Female'),
            ]
        gender = form.selector(label='gender', entries = entries, selection='female')
        log = doc.document(id='log', Class='log', title='log')
        
        gender.onchange = luban.a.load(
            actor=self.name, routine='onchange',
            old = luban.event.old, new = luban.event.new
            )
        gender.onfocus = luban.a.select(element=log).append(
            newelement=luban.e.paragraph(text="focused")
            )
        gender.onblur = luban.a.select(element=log).append(
            newelement=luban.e.paragraph(text="blured")
            )
        
        return doc


    def onchange(self, old=None, new=None, **kwds):
        msg = "value changed from %r to %r" % (old, new)
        newelement = luban.e.paragraph(text = msg)
        return luban.a.select(id='log').append(newelement=newelement)


# End of file 
