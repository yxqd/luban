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

    title='A basic accordion'
    description = [
        'It is easy to create a basic accordion: just create one',
        'and add sections to it.',
        ]
    def createDemoPanel(self, **kwds):
        acc = luban.ui.e.accordion()
    
        sec1 = acc.section(label='section1')
        sec1.paragraph(text='paragraph in section1')
        
        sec2 = acc.section(label='section2', selected=1)
        doc2 = sec2.document(title='doc in section2')
        doc2.paragraph(text='section 2 test')
    
        sec3 = acc.section(label='section3')
        sec3.paragraph(text='text text text')
    
        return acc


# End of file 
