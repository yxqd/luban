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


# this module defines the test fixtures in Jiao's laptop "blackwhite"


from _ import Fixture, Computer, Server


# the lan site of luban example/test applications
# this is the ip address of the laptop in the private network
# created by vmware
lansite = 'http://172.16.19.1'
appmap = {
    'aokuang' : '/~linjiao/cgi-bin/aokuang/main.cgi',
    }
server = Server(host=lansite, appmap=appmap)


# win xp vmware vm with selenium server
winxpvm = Computer(
    ip = '172.16.19.133', port = 4444,
    os = 'Windows XP',
    )


# win xp vm testing fixture
winxpfixture = Fixture(
    computer = winxpvm,
    browsers = [
      #'*iexplore',
      '*firefox',
      '*googlechrome',
      #'*safari',
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

