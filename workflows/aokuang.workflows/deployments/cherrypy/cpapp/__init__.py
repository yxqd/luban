#!/usr/bin/env python

from luban import py_major_ver


import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy
from aokuang_workflows_config import dburi
cherrypy.config.update({
    'tools.SATransaction.on': True,
    'tools.SATransaction.dburi': dburi,
    'tools.SATransaction.echo': False,
    'tools.SATransaction.convert_unicode': True,
    })


from aokuang.workflows.controller.CherrypyController import CherrypyController
class Root(CherrypyController):

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

