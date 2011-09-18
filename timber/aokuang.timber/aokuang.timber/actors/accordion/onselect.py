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

    title='"onselect" event'
    description = [
        ]
    def createDemoPanel(self, **kwds):
        acc = luban.e.accordion()
    
        sec1 = acc.section(label='section1', id='section1')
        sec1.paragraph(text='paragraph in section1')
        
        sec2 = acc.section(label='section2', id='section2', selected=1)
        doc2 = sec2.document(title='doc in section2')
        doc2.paragraph(text='section 2 test')
    
        show_change = luban.a.load(
            actor=self.name, routine='onchange',
            old = luban.event.oldsection,
            new = luban.event.newsection,
            )
        sec1.onselect = sec2.onselect = show_change
        
        return acc


    def onchange(self, old=None, new=None, **kwds):
        msg = "accordion switched from %r to %r" % (old, new)
        return luban.a.alert(msg)


# End of file 
