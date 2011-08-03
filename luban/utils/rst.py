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
    """convert rst str to a html str
    """
    from docutils import core
    
    parts = core.publish_parts(
        source=rest,
        writer_name='html')
    return parts['body_pre_docinfo']+parts['fragment']


# version
__id__ = "$Id$"

# End of file 
