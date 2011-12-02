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
    
    # simple requirement that only checking is done
    # if check fails, simple no more action will be perform, or error thrown
    
    check_requirement = None # function to check whether a requirement is satisfied. return True if requirement is not fullfilled.

class PortalRequirement(Requirement):
    
    # requirement of a portal
    # if check of reqiuriement failed, an interface will show up
    # to challenge the user to fullfill the requirement
    
    check_requirement = None # function to check whether a requirement is satisfied. return True if requirement is not fullfilled.
    fullfill_requirement = None # factory method to return a UI frame that solicit answers from user to fullfill the requirement


def require(requirement, **kwds):
    if isinstance(requirement, PortalRequirement):
        return require_portal(requirement, **kwds)

    def convert(f):
        def newhandler(self, *args, **kwds):
            if requirement.check_requirement():
                return "access denied"
            return f(self, *args, **kwds)
        return newhandler
    return convert    


def require_portal(requirement, actorname=None, onsuccess=None):
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
            
            # this is to build the action to load the real functionality.
            # we need it after user successfully fullfill the requirement
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
    def handle_error(conversion_errors, _func_=None):
        
        # by default, assume each arg annotated in the handler function
        # is about one form input.
        input_name_list = input_names or _func_.__annotations__.keys()
            
        actions = [luban.a.select(id=formid, type='form').clearErrors()]
        for name, error in conversion_errors:
            # if it is not an input error, we should raise it
            if name not in input_name_list:
                raise error
            # otherwise need new action
            action = luban.a.select(id=formid)\
                .find(name=name, type="formfield")\
                .showError(message = str(error))
            actions.append(action)
            continue
        return actions
    return handle_error


# shortcut
def formprocesser(formid, *input_names):
    from luban.decorators import typeconversion
    return typeconversion(generateforminputerror(formid, *input_names))


__all__ = [
    'Requirement', 'PortalRequirement', 'require', 
    'generateforminputerror', 'formprocesser',
    ]
from luban import decorators
for name in __all__: setattr(decorators, name, eval(name))

# End of file 

