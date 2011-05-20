# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def sentry(*args):
    from Sentry import Sentry
    return Sentry(*args)


def guid(*args):
    from GUID import GUID
    return GUID(*args)


def guidfromidddaemon(*args):
    from GUIDfromIDDDaemon import GUID
    return GUID(*args)


def activityLogger(*args):
    from ActivityLogger import ActivityLogger
    return ActivityLogger(*args)


def helloworld():
    from HelloWorldActor import HelloWorld
    return HelloWorld()


def notImplementedActor():
    from NotImplementedActor import Actor
    return Actor()


# version
__id__ = "$Id$"

# End of file 
