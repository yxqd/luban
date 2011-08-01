#!/usr/bin/env python3

import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy, luban.ui.elements as lue

class Root:

    def __init__(self):
        from luban.weaver.web import create as createWeaver
        self.weaver = createWeaver(
            controller_url = 'helloworld',
            statichtmlbase='static')
        return

    @cherrypy.expose
    def welcome(self):
        # the overall frame
        frame = lue.frame(title='my application')
        # a document in the frame
        doc = frame.document(title='Hello world!', name='doc1')
        # weave to produce html
        return self.weaver.weave(frame)

    @cherrypy.expose
    def index(self):
        return "Hello"
    index.exposed = True

# cherrypy.quickstart(HelloWorld())

