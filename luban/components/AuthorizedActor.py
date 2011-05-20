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


from Actor import Actor as base


'''
base class for actors for which each routine needs authentication.
If user is not authorized yet, the login page will be brought up.
'''

class AuthorizedActor(base):


    class Inventory(base.Inventory):

        import luban.inventory
        include_credential = luban.inventory.bool(name='include_credential', default=True)
    

    def perform(self, director, routine=None, debug=False):
        # if the routine is special (no need to authorize), 
        # we can just perform it
        method = getattr(self, routine)
        if hasattr(method, 'open_to_public') and method.open_to_public:
            return super(AuthorizedActor, self).perform(
                director, routine=routine, debug=debug)
            
        # make sure this action is authrized
        if not director.userIsAuthorized():
            return self.notauthorizedyet(director)

        # perform action as usual
        ret = super(AuthorizedActor, self).perform(
            director, routine=routine, debug=debug)

        # if no need to include credential, just return
        include_credential = self.inventory.include_credential
        if not include_credential:
            return ret
        
        # add credential update to the actions
        credential_update = updateCredential(
            username=director.sentry.username,
            ticket=director.sentry.ticket,
            )
        
        # XXX this is a bad implementation
        # XXX should remove the support of a list of actions
        # XXX instead, support ActionContainer type
        if isaction(ret):
            return [credential_update, ret]
        elif isiterable(ret):
            # nothing in the list
            if len(ret)==0: return ret
            # list of actions, add credential_update
            if isaction(ret[0]):
                return [credential_update] + ret
            # othwise, just return
            return ret
        elif ret is None:
            return credential_update
        elif isinstance(ret, basestring):
            return ret
        else:
            ret.credential(
                username=director.sentry.username,
                ticket=director.sentry.ticket,
                )
        return ret


    def notauthorizedyet(self, director):
        return alert('You are not authorized to access this page')
    
    pass


from Actor import AcceptArbitraryInput
class AuthorizedReceptionist(AcceptArbitraryInput, AuthorizedActor):

    pass


from luban.content import updateCredential, alert

from luban.content.Action import Action
def isaction(candidate):
    return isinstance(candidate, Action)

def isiterable(candidate):
    return '__iter__' in dir(candidate)

# version
__id__ = "$Id$"

# End of file 
