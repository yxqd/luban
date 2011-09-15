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


"""
helloworld: trivial test

example urls:

* http://localhost:8080/?actor=helloworld
* http://localhost:8080/?actor=helloworld&routine=str
* http://localhost:8080/?actor=helloworld&routine=frame
"""


from luban.controller.Actor import Actor as base

class Actor(base):

    expose = 1

    
    def default(self):
        return self.frame()
    

    def str(self):
        return "Hello world!"


    def frame(self):
        import luban
        frame = luban.e.frame(title="hello world")
        frame.document(title="hello world")
        return frame


    def button(self):
        frame = luban.e.frame(title="luban test: button")
        doc = frame.document(title="Click the following button")
        b = doc.button(
            label = 'button 1',
            onclick = luban.a.alert('clicked button 1'),
            )
        b2 = doc.button(
            label = 'button 2',
            onclick = luban.a.load(actor=self.name, routine='onb2'),
            )
        return frame


    def onb2(self, **kwds):
        return luban.a.alert("clicked button 2")


# End of file 

