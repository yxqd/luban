# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import luban

class Requirement:
    
    check_requirement = None # function to check whether a requirement is satisfied. return True if requirement is not fullfilled.
    fullfill_requirement = None # factory method to return a UI frame that solicit answers from user to fullfill the requirement

def require(requirement, actorname=None, onsuccess=None):
    """
    requirement: Requirement instance
    onsuccess: if requirement was succesfully fullfilled, take this action
    """
    onsuccess_action = onsuccess
    import inspect
    def convert(f):
        def newhandler(self, *args, **kwds):
            if not requirement.check_requirement():
                frame = f(self, *args, **kwds)
                if 'replaceinterface' in kwds and kwds['replaceinterface']:
                    return luban.a.select(id='').replaceBy(newelement=frame)
                else:
                    return luban.a.establishInterface(frame)
            
            # this is the action to load the real functionality.
            # it always need to be a load action.
            # "actor" should be the name of the actor
            # "routine" should be the name of this routine
            # "replaceinterface" is required to replace the requirement solicitation inteface with the actual interface
            onsuccess = onsuccess_action or luban.a.load(
                actor = actorname or getactorname(
                    inspect.getmodule(f).__name__, self.controller.actor_packages),
                routine= f.__name__,
                replaceinterface=1
                )
            luban.session['onsuccess'] = onsuccess
            frame = requirement.fullfill_requirement()
            return luban.a.establishInterface(frame)
        return newhandler
    return convert


def getactorname(modulename, packages):
    """getactorname("myui.actors.hello", ['myui.actors']) -> 'hello'
    """
    for pkg in packages:
        if modulename.startswith(pkg):
            return modulename[len(pkg)+1:]
        continue
    return


from luban import decorators
decorators.Requirement = Requirement
decorators.require = require

# End of file 

