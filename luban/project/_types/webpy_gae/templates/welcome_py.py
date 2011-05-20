# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


template = """#!/usr/bin/env python

import sys
sys.path.insert(0, 'lib')

import web

urls = (
    '/welcome', 'welcome',
    '/', 'index',
    )


class index:
    def GET(self): return web.seeother('/welcome')
    


import luban.content as lc


class welcome:


    def __init__(self):
        from luban.weaver.web import create as createWeaver
        self.weaver = createWeaver(
            controller_url = 'welcome',
            statichtmlbase='static')
        return


    def welcome(self):
        # the overall frame
        frame = lc.frame(title='my application')
        # a document in the frame
        doc = frame.document(title='Hello world!', id='doc1')
        return self.weaver.weave(frame)


    def GET(self):
        return self.welcome()


app = web.application(urls, globals())

app.cgirun()

"""


def generate(project):
    return template

# version
__id__ = "$Id$"

# End of file 
