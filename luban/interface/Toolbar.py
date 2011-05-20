#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from ElementContainer import ElementContainer, elementfactory


class Toolbar(ElementContainer):


    simple_description = 'A simple container of buttons'
    full_description = (
        "A toolbar is a simple, horizontal container. "
        "Mostly it contains buttons. "
        )
    examples = [
        '''
    import luban.content
    toolbar = luban.content.toolbar()
    b1 = toolbar.button(label='button1')
    b2 = toolbar.button(label='button2')
    toolbar.spacer()
    b3 = toolbar.button(label='button3')
    ''',
        ]

    abstract = False

    @elementfactory
    def button(self, *args, **kwds):
        from Button import Button
        b = Button(*args, **kwds)
        self.add(b)
        return b

    @elementfactory
    def spacer(self):
        ts = ToolbarSpacer()
        self.add(ts)
        return ts


    def identify(self, inspector):
        return inspector.onToolbar(self)



from Element import Element
class ToolbarSpacer(Element):

    def identify(self, inspector):
        return inspector.onToolbarSpacer(self)
    

# version
__id__ = "$Id$"

# End of file 
