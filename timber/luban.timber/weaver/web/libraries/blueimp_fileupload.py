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


from luban.weaver.web.Library import Library
lib = Library(
    name = 'blueimp-fileupload',
    css = ['jquery.ext/blueimp-file-upload/jquery.fileupload-ui.css'],
    javascripts = ['jquery.ext/blueimp-file-upload/jquery.fileupload.js'],
    dependencies = ['jquery.iframe-transport'],
    website = "https://github.com/blueimp/jQuery-File-Upload",
    )

lib.demosite = "http://aquantum-demo.appspot.com/file-upload"


# End of file 

