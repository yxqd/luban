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


from Parser import Parser
default_parser = Parser()

def parse(stream): return default_parser.parse(stream)

def parse_file(filename): return parse(open(filename))

import interface
# XXX: do we need to keep backward compatibility?
content = interface

# version
__id__ = "$Id$"

# End of file 

