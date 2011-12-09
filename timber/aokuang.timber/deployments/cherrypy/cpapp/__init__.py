#!/usr/bin/env python3

import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

# aokuang.timber relies on luban.timber
from luban.timber.controller.CherrypyController import CherrypyController
class Root(CherrypyController):

    def __init__(self):
        super().__init__(
            url = '/',
            static_html_base = '/static',
            actor_packages = ['aokuang.timber.actors', 'aokuang.core.actors'],
            stylesheets = ['aokuang.core.css', 'aokuang.timber.css'],
            )
        return

