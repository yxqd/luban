#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from luban.applications.UIApp import UIApp as base


class DbApp(base):


    class Inventory(base.Inventory):

        import pyre.inventory

        clerk = pyre.inventory.facility(name="clerk", default='democlerk')
        name = pyre.inventory.str(name='name')


    def help(self):
        print
        print
        print "create a db table"
        print " * typical usage:"
        print "   $ createtable.py --name=<tablename>"
        print
        print " * table name is the name of the table class in jazzclub.dom namespace. For example"
        print "   - News.News"
        print
        print


    def main(self, *args, **kwds):
        clerk = self.inventory.clerk
        name = self.inventory.name
        table = clerk._getTable(name)
        clerk.db.createTable(table)
        return


    def __init__(self):
        base.__init__(self, 'createtable')
        return


    def _getPrivateDepositoryLocations(self):
        return ['../config', '/tmp/luban-services']



def main():
    import journal
    journal.debug('db').activate()
    app = DbApp()
    return app.run()


# main
if __name__ == '__main__':
    # invoke the application shell
    main()


# version
__id__ = "$Id$"

# End of file 
