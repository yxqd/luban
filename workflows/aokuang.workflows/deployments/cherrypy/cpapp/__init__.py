#!/usr/bin/env python

from luban import py_major_ver


import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

from luban.timber.controller.CherrypyFullController import CherrypyFullController
class Root(CherrypyFullController):

    def __init__(self):
        if py_major_ver == 2:
            superme = super(Root, self)
        elif py_major_ver == 3:
            superme = super()
            
        superme.__init__(
            url = '/',
            static_html_base = '/static',
            actor_packages = ['aokuang.workflows.actors'],
            stylesheets = ['aokuang.core.css', 'aokuang.workflows.css'],
            )
        return

