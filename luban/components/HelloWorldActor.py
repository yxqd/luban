# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from Actor import Actor

class HelloWorld(Actor):

    def default(self, director):
        from luban.content import Page
        page = Page.Page(title='Hello world!')
        doc = page.document(title='Hello world!')
        return page


    def __init__(self):
        Actor.__init__(self, 'helloworld')
        return


# version
__id__ = "$Id$"

# End of file 
