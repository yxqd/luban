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


# ***************************************************************************
# this is going to change. This is only good for the current
# SimpleHttpServer implementation.
# ***************************************************************************


content = '''
webapp = 'webmain.py'

import os

#The "request" object passed from simple http server
#convert it to a query string
query_string = '&'.join( '%s=%s' % (k, ','.join(v)) for k,v in request.iteritems() )
os.environ['QUERY_STRING'] = query_string


import tempfile
d = tempfile.mkdtemp()
out = os.path.join(d, 'out.html')
err = os.path.join(d, 'err.html')

cmd = "%s >%s  2>%s" % (webapp, out, err)
if os.system( cmd ):
    print open( err ).read()
else:
    lines = open( out ).readlines()
    print ''.join( lines[1:] )

import shutil
shutil.rmtree(d)
'''


def generate(project):
    return content


# version
__id__ = "$Id$"

# End of file 
