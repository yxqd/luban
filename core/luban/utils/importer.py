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


# importlib and __import__ all have some mysterious problems
# this seems work best, although look quite un-elegant
# Note: only works for absolute import: pkg import be absolute
def import_module(name, pkg):
    code = 'from %s import %s as module' % (pkg, name)
    try:
        exec(code)
    except:
        raise RuntimeError("failed to run %s" % code)
    return locals()['module']



# End of file 
