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


default_parser = None

def parse(stream): 
    global default_parser
    if default_parser is None:
        from Parser import Parser
        default_parser = Parser()
    return default_parser.parse(stream)

def parse_file(filename): return parse(open(filename))

from . import ui
# XXX: do we need to keep backward compatibility?
content = ui

# version
__id__ = "$Id$"

# End of file 

