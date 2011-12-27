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


from luban.weaver.web.libraries import jquery_ext

from luban.weaver.web.Library import Library

root = 'jquery.ext'
jsp = lambda j: '%s/%s' % (root, j)

Library(
    name='jquery.history',
    javascripts = [jsp('jquery.history.js')],
    )

Library(
    name='jquery.iframe-transport',
    javascripts = [jsp('jquery.iframe-transport.js')],
    )


# End of file 
