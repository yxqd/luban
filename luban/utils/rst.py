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


def rest2html(rest):
    from docutils import core
    
    parts = core.publish_parts(
        source=rest,
        writer_name='html')
    lines = (parts['body_pre_docinfo']+parts['fragment']).splitlines()

##     # XXX: hack
##     lines = map(str, lines)
##     return []
    return lines


# version
__id__ = "$Id$"

# End of file 
