#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from luban import py_major_ver, setup_context
if py_major_ver == 2: setup_context(locals())


from luban.ui.elements.SimpleContainer import SimpleContainer


class Toolbar(SimpleContainer):

    # decorators
    simple_description = 'A simple container of buttons'
    full_description = (
        "A toolbar is a simple, horizontal container. "
        "Mostly it contains buttons. "
        )
    examples = [
        '''
    import luban
    toolbar = luban.e.toolbar()
    b1 = toolbar.button(label='button1')
    b2 = toolbar.button(label='button2')
    b3 = toolbar.button(label='button3')
    ''',
        ]
    

    # methods
    # .. for inspector
    def identify(self, inspector):
        return inspector.onToolbar(self)



# version
__id__ = "$Id$"

# End of file 
