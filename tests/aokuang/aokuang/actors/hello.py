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
hello: trivial test

example urls:

* http://localhost:8080/?actor=hello
* http://localhost:8080/?actor=hello&routine=str
* http://localhost:8080/?actor=hello&routine=frame
"""


from luban.controller.Actor import Actor as base

class Actor(base):

    
    def default(self):
        return self.frame()
    

    def str(self):
        return "Hello world!"


    def frame(self):
        import luban.ui as lui
        frame = lui.e.frame(title="hello world")
        frame.document(title="hello world")
        return frame


# End of file 

