#!/usr/bin/env python3

import sys, os
sys.path.insert(0, '/home/imaginlabs/imaginlabs/releaser/EXPORT/packages')
sys.stdout = sys.stderr

import atexit, threading, cherrypy
cherrypy.config.update({'environment': 'embedded'})

stylesheets = [
    'common.css',
    'frontpage.css',
    ]

import luban.timber

# imaginlabs uses luban.timber
from luban.timber.controller.CherrypyController import CherrypyController
class Root(CherrypyController):

    def __init__(self):
        super().__init__(
            url = 'http://www.imaginlabs.com/index.cgi',
            html_base = 'http://www.imaginlabs.com/',
            static_html_base = 'static',
            actor_package = 'imaginlabs.ui.actors',
            stylesheets = stylesheets,
            )
        return

application = cherrypy.Application(Root(), script_name=None, config=None)

