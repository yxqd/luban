#!/usr/bin/env python

import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

from luban.controller.CherrypyController import CherrypyController
class Root(CherrypyController):

    def __init__(self):
        from luban import py_major_ver
        if py_major_ver == 2:
            superme = super(Root, self)
        elif py_major_ver == 3:
            superme = super()
            
        superme.__init__(
            url = '/',
            static_html_base = '/static',
            actor_package = 'aokuang.core.actors',
            stylesheets = ['aokuang.core.css'],
            )
        return

