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

# namespace for requirements
class requirements: pass

def check_email(*args, **kwds):
    "a simple test that check if user email is available"
    email = luban.session.get('email')
    return not email
requirements.email = luban.decorators.Requirement()
requirements.email.check_requirement = check_email


# End of file 
