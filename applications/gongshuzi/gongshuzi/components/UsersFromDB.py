# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.ipa.UserManager import UserManager as base
from pyre.components.Component import Component

class UsersFromDB(base):
    
    class Inventory(Component.Inventory):

        import pyre.inventory

        import gongshuzi.components
        clerk = pyre.inventory.facility(
            name="clerk", factory=gongshuzi.components.democlerk)
        pass # end of Inventory


    def __init__(self, name = 'usersFromDB'):
        base.__init__(self, name)
        return


    def load(self):
        clerk = self.clerk
        method = 'md5'

        records = clerk.indexActiveUsers().itervalues()
        users = {}
        for r in records:
            users[r.username] = r.password
            continue

        count = len(users)
        if count == 1:
            suffix = ''
        else:
            suffix = 's'
        self._info.log("found %d user record%s" % (count, suffix))

        self._users = users
        #self._reload = False

        self._encoder = self._encoders[method]
        self._decoder = self._decoders[method]
        return


    def save(self):
        from gongshuzi.dom.User import User
        for name, pw in self._users.iteritems():
            user = self.clerk.getUser(name)
            user.password = pw
            self.clerk.updateRecord(User)
            continue
        return


    def _configure(self):
        Component._configure(self)
        self.clerk = self.inventory.clerk
        self.clerk.director = None
        return
    

    def _init(self):
        Component._init(self)
        return


# version
__id__ = "$Id$"

# End of file 
