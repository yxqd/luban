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

    title='A form with one radio box'
    description = [
        'The radio box is attached with event hanlder for ',
        '"change" event.',
        'Please note that the "focus" and "blur" events are not yet implemented for radiobox',
        ]
    def createDemoPanel(self, **kwds):
        doc = luban.e.document()
        form = doc.form(title='form')
        answers = [
            ('a', 'black hole'),
            ('b', 'dark matter'),
            ('c', 'white dwarf'),
            ]
        selector = form.radio(
            label='your favorite object in space',
            entries = answers,
            selection='b',
            )
        log = doc.document(id='log', Class='log', title='log')
        
        selector.onchange = luban.a.load(
            actor=self.name, routine='onchange',
            old = luban.event.old, new = luban.event.new
            )        
        return doc


    def onchange(self, old=None, new=None, **kwds):
        msg = "value changed from %r to %r" % (old, new)
        newelement = luban.e.paragraph(text = msg)
        return luban.a.select(id='log').append(newelement=newelement)


# End of file 
