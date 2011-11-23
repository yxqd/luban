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
            actor = actorname or getactorname(
                inspect.getmodule(f).__name__, self.controller.actor_packages)
            routine= f.__name__
            args = (actor, routine) + args
            kwds = dict(kwds)
            kwds['replaceinterface'] = 1
            onsuccess = onsuccess_action or luban.a.load(*args, **kwds)
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


# default error handler for form
# this is used in combination with luban.controller.decorators.typeconversion
def generateforminputerror(formid, *input_names):
    """
    formid: id of the form
    input_names: a list of input names
    """
    import luban
    def handle_error(conversion_errors):
        actions = [luban.a.select(id=formid, type='form').clearErrors()]
        for name, error in conversion_errors:
            # if it is not an input error, we should raise it
            if name not in input_names:
                raise error
            # otherwise need new action
            action = luban.a.select(id=formid)\
                .find(name=name, type="formfield")\
                .showError(message = str(error))
            actions.append(action)
            continue
        return actions
    return handle_error



from luban import decorators
decorators.Requirement = Requirement
decorators.require = require
decorators.generateforminputerror = generateforminputerror

# End of file 

