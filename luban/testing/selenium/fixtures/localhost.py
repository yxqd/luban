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


# this module defines the test fixtures in localhost. generally speaking,
# it should work for anyone who installed selenium server on localhost
# and has a firefox browser on localhost


from _ import Fixture, Computer, Server


aokuang_site = 'http://localhost:8002'
aokuang_appmap = {
    'aokuang' : '/cgi-bin/main.py',
    }
aokuang_server = Server(host=aokuang_site, appmap=aokuang_appmap)


import os
localhost_computer = Computer(
    ip = 'localhost', port = 4444,
    os = os.uname()[0],
    )


aokuang_fixture = Fixture(
    computer = localhost_computer,
    browsers = [
      '*firefox',
      #'*iexplore',
      #'*googlechrome',
      #'*safari',
      ],
    server = aokuang_server,
    )

#
fixtures = [
    aokuang_fixture,
    ]


# version
__id__ = "$Id$"

# End of file 

