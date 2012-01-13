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


# XXXX
# luban core js lib knows about default position of luban widget js libs
# so "javascripts" is an empty list.
# is this really a good strategy?
# XXXX

from luban.weaver.web.Library import Library

elements = [
    #
    'portlet', 'portletitem',
    'accordion', 'accordionsection',
    'codeviewer',
    #
    'toolbar',
    'image',
    'grid', 'gridrow', 'gridcell',
    'uploader',
    'slides', 'slide',
    'bulletinboard', 'bulletinboardannouncement',
    
    'form', 
    'formtextfield', 'formpasswordfield', 'formtextarea',
    'formselectorfield', 'formradiobox', 'formcheckbox',
    'formsubmitbutton',

    'progressbar',
    
    'dialog',

    'sketchcanvas',
    
    ]


for element in elements:
    js = 'luban.timber/widgets/%s.js' % element
    lib = Library(
        "luban.widgets.%s" % element,
        javascripts = [js],
        )
    continue


Library.get('luban.widgets.accordion').dependencies = ['jqueryui.accordion']
Library.get('luban.widgets.codeviewer').dependencies = ['prettify']
Library.get('luban.widgets.uploader').dependencies = [
    'blueimp-fileupload', 'jqueryui.progressbar']
Library.get('luban.widgets.slides').dependencies = ['jquery.cycle']
Library.get('luban.widgets.progressbar').dependencies = ['jqueryui.progressbar']
Library.get('luban.widgets.dialog').dependencies = ['jqueryui.dialog']
Library.get('luban.widgets.sketchcanvas').dependencies = ['jquery.sketch']


# End of file 
