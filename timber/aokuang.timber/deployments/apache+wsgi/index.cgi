#!/usr/bin/env python3

import sys, os
sys.stdout = sys.stderr

import atexit, threading, cherrypy
# comment this out to see error traceback
cherrypy.config.update({'environment': 'embedded'})

stylesheets = [
    'aokuang.core.css',
    'aokuang.timber.css',
    ]

actor_packages = [
    'aokuang.timber.actors',
    'aokuang.core.actors',
    ]

#
import luban.timber

from luban.timber.controller.CherrypyController import CherrypyController
class Root(CherrypyController):

    def __init__(self):
        super().__init__(
            url = 'http://aokuang.lubanui.org/',
            # url = 'http://127.0.0.1/',
            html_base = 'http://aokuang.lubanui.org/',
            # html_base = 'http://127.0.0.1/',
            static_html_base = 'static',
            actor_packages = actor_packages,
            stylesheets = stylesheets,
            )
        return

application = cherrypy.Application(
    Root(),
    script_name=None,
    config='prod.conf',
    )

