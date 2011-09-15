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

from luban import ui as lui

from ....DemoPanelActor import Actor as base
class Actor(base):

    title='A html document'
    description = [
        ]
    def createDemoPanel(self, **kwds):
        text = '''
<h1>Title here</h1>

<p>
Some more items
</p>

<ul>
 <li> a </li>
 <li> b </li>
</ul>

<p>a paragraph with a <a href="http://a.b.com" target="_blank">link</a> </p>

<p>&copy</p>
        '''
        return lui.e.htmldocument(text=text)


# End of file 
