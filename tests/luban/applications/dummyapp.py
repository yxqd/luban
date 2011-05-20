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


from pyre.applications.Script import Script
class App(Script):

    class Inventory(Script.Inventory):

        import pyre.inventory
        greeting = pyre.inventory.str('greeting', default="Hello")

    def main(self, *args, **kwds):
        print self.inventory.greeting


def main():
    from luban.applications.SuperApp import SuperApp
    superapp = SuperApp('dummysuperapp', App)
    superapp.run()
    return


if __name__ == '__main__': main()            


# version
__id__ = "$Id$"

# End of file 
