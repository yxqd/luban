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


"""
This is a special instance of 'super-app'. pls consult SuperAppBase for
more details of the general purpose of SuperAppBase.

The SuperApp here allows configuration of following properties:

  * config: paths of depositories for pyre application
"""


def toPathList(paths):
    return map(toPath, paths)


def toPath(path):
    import os
    return os.path.abspath(os.path.expanduser(path))



from SuperAppBase import SuperAppBase
class SuperApp(SuperAppBase):

    class Inventory(SuperAppBase.Inventory):

        import pyre.inventory
        config = pyre.inventory.list(name='config', default='', validator=toPathList)
        config.meta[SuperAppBase.inventory_item_signature] = True
        


    def __init__(self, appname, AppClass):
        '''SuperApp(appname, AppClass) -> a super application of the given application
        AppClass: application class. must be a subclass of pyre application
        appname: name of the app. str
        '''
        self.AppClass = AppClass
        self.appname = appname
        super(SuperApp, self).__init__('%s-superapp' % appname)
        return
    
    
    def runApp(self, config=None, **kwds):

        msg = 'config directories: %s' % (config,)
        self._info.log(msg)        
            
        App = self.AppClass
        class _(App):

            def _getPrivateDepositoryLocations(self):
                return config

        app = _(self.appname)
        return app.run()


    def _defaults(self):
        super(SuperApp, self)._defaults()
        self.inventory.typos = 'relaxed'
        return
    


def test():
    # please try the following commands:
    # python SuperApp.py
    # python SuperApp.py --config=a 
    # python SuperApp.py --greeting=aloha 
    # python SuperApp.py --config=a --- --greeting=aloha 
    # python SuperApp.py --help-properties ---
    # python SuperApp.py --- --help-properties
    # python SuperApp.py --config=a --help-properties ---
    # python SuperApp.py --- --greeting=aloha --help-properties

    from pyre.applications.Script import Script
    class App(Script):

        class Inventory(Script.Inventory):

            import pyre.inventory
            greeting = pyre.inventory.str('greeting', default="Hello")
            
        def main(self, *args, **kwds):
            print self.inventory.greeting

    superapp = SuperApp('test', App)
    superapp.run()
    return


def main():
    test()
    return


if __name__ == '__main__': main()            


# version
__id__ = "$Id$"

# End of file 
