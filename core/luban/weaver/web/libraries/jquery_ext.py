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


from ..Library import Library

jui_root = 'jquery/jquery-ui-1.8.16'
jui_dev = '%s/development-bundle' % jui_root
jui_external = '%s/external' % jui_dev
jsp = lambda j: '%s/%s' % (jui_external, j)

Library(
    name='qunit',
    javascripts = [jsp('qunit.js')],
    )
Library(
    name='jquery.metadata',
    javascripts = [jsp('jquery.metadata.js')],
    dependencies = ['jquery'],
    )
Library(
    name='jquery.cookie',
    javascripts = [jsp('jquery.cookie.js')],
    dependencies = ['jquery'],
    )
Library(
    name='jquery.bgiframe',
    javascripts = [jsp('jquery.bgiframe-2.1.2.js')],
    dependencies = ['jquery'],
    )


# End of file 
