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

def require(requirement, onsuccess):
    """
    requirement: Requirement instance
    onsuccess: if requirement was succesfully fullfilled, take this action
    """
    def convert(f):
        def newhandler(self, *args, **kwds):
            if not requirement.check_requirement():
                frame = f(self, *args, **kwds)
                if 'replaceinterface' in kwds and kwds['replaceinterface']:
                    return luban.a.select(id='').replaceBy(newelement=frame)
                else:
                    return luban.a.establishInterface(frame)
            
            luban.session['onsuccess'] = onsuccess
            frame = requirement.fullfill_requirement()
            return luban.a.establishInterface(frame)
        return newhandler
    return convert

from luban import decorators
decorators.Requirement = Requirement
decorators.require = require

# End of file 

