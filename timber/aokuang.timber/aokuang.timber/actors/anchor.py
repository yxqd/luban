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


from luban.controller.Actor import Actor as base
class Actor(base):

    expose = 1

    
    def default(self, **kwds):
        return self.frame()
    

    def frame(self, **kwds):
        frame = skeleton()
        container = frame.find(id='container')
        b1 = container.button(label='button1', id="b1")
        b1clicked = [
            luban.a.select(id='display').replaceContent(
                newcontent = b1doc()
                ),
            # luban.a.select(element=b1).destroy(),
            luban.a.setanchor(actor=self.name, routine='b1',)
            ]
        b1.onclick = b1clicked
        return frame


    def b1(self, **kwds):
        frame = skeleton()
        display = frame.find(id='display')
        display.append(b1doc())
        return luban.a.select(id='').replaceBy(newelement=frame)


def skeleton():
    frame = luban.e.frame(title="aokuang: anchor demo")
    container = frame.document(Class='white-bg', id='container')
    doc = container.document(title="display", id='display')
    return frame


def b1doc():
    d = luban.e.document(title='title 1')
    d.append('absdslj ajsld fjajsdf sdf')
    return d


# End of file 

