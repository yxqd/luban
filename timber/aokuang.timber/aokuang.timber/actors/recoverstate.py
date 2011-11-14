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
from luban.timber.controller import state


from luban.controller.Actor import Actor as base
class Actor(base):

    expose = 1

    
    def default(self, **kwds):
        frame = self.frame()
        return luban.a.establishInterface(frame)
    

    def frame(self, **kwds):
        frame = skeleton()
        container = frame.find(id='recover-state-demo-container')
        b1 = container.button(label='button1', id="b1")
        # action when button is clicked
        # intentionally, we leave the button in the interface (did not destroy it)
        # this is different from the UI generated in method
        # "b1". this is intentional so we can see difference
        # of directly applying the action versus a new interface
        # generated to supposedly be the same interface
        # result from the action. so we can catch bugs
        # if the implementation of renderer mistakenly 
        # invoke the new interface building in method "b1"
        b1clicked = [
            luban.a.select(id='display').replaceContent(
                newcontent = b1doc()
                ),
            luban.a.setrecoverer(actor=self.name, routine='b1',)
            ]
        b1.onclick = b1clicked

        b2 = container.button(label='button2', id="b2")
        b2clicked = [
            luban.a.select(id='display').replaceContent(
                newcontent = b2doc()
                ),
            luban.a.setrecoverer(actor=self.name, routine='b2',)
            ]
        b2.onclick = b2clicked

        return frame

    @state.stateHandler
    def b1(self, **kwds):
        frame = skeleton()
        display = frame.find(id='display')
        display.append(b1doc())
        return frame


    @state.stateHandler
    def b2(self, **kwds):
        frame = skeleton()
        display = frame.find(id='display')
        display.append(b2doc())
        return frame


def skeleton():
    frame = luban.e.frame(title="aokuang: state recover demo")
    container = frame.document(Class='white-bg', id='recover-state-demo-container')
    doc = container.document(title="display", id='display')
    return frame


def b1doc():
    d = luban.e.document(title='title 1')
    d.append('luban: a user interface specification "language"')
    return d


def b2doc():
    d = luban.e.document(title='title 2')
    d.append('pyre: an integration framework for high-performance computing')
    return d


# End of file 

