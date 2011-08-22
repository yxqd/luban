#!/usr/bin/env python3

import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy, luban.ui as lui

from luban.controller.CherrypyController import CherrypyController
class Root(CherrypyController):

    def __init__(self):
        super().__init__(
            url = '/',
            static_html_base = 'static',
            actor_package = 'aokuang.actors',
            )
        return

    

