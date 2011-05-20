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


# this module defines the test fixtures in used by buildbot system on bagua


from _ import Fixture, Computer, Server


# the site of luban example/test applications that will be updated
# by buildbot slave
site = 'http://131.215.146.170'
appmap = {
    'aokuang' : '/cgi-bin/aokuang/main.cgi',
    }
server = Server(host=site, appmap=appmap)


# win xp vmware vm with selenium server
winxpvm = Computer(
    ip = '131.215.146.184', port = 4444,
    os = 'Windows XP',
    )


# win xp vm testing fixture
winxpfixture = Fixture(
    computer = winxpvm,
    browsers = [
      # '*iexplore',
      '*firefox',
      '*googlechrome',
      # '*safari',
      ],
    server = server,
    )

#
fixtures = [
    winxpfixture,
    ]


# version
__id__ = "$Id$"

# End of file 

