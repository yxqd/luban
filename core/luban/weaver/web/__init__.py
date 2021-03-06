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


def create(htmlbase='', controller_url='/controller/main.cgi',
           statichtmlbase='', cssbase='css', jsbase='javascripts', imagesbase='images',
           cookie_path='', use_cookie=False,
           library_bundle = None,
           output_as_lines = False
           ):
    '''create a weaver that weaves html or json output out of luban UI specifications
    
* htmlbase: the base url of the site. rendered as <base> tag in the <head> section.
* controller_url: the url of the controller.
* statichtmlbase: the url of the root of the static html
* cssbase: the path of the root of the css style sheets files relative to statichtmlbase
* jsbase: the path of the root of the javascripts relative to statichtmlbase
* imagesbase: the path of the root of the images relative to statichtmlbase
* cookie_path: the path for cookie
* use_cookie: if True, cookie will be used
* library_bundle: the javascript/css plugin library bundle to render luban widgets and actions. if not specified, a default library bundle will be used
* output_as_lines: if true, output will ba a list of lines
    '''
    #
    if statichtmlbase:
        cssbase = '%s/%s' % (statichtmlbase, cssbase)
        jsbase = '%s/%s' % (statichtmlbase, jsbase)
        imagesbase = '%s/%s' % (statichtmlbase, imagesbase)
    #
    from .Weaver import Weaver
    weaver = Weaver()
    #
    weaver.obj2html.htmlbase = htmlbase
    weaver.obj2html.javascriptsbase = jsbase
    weaver.obj2html.cssbase = cssbase
    weaver.obj2html.imagesbase = imagesbase
    #
    weaver.obj2html.controller_url = controller_url
    #
    weaver.obj2html.cookie_path = cookie_path
    weaver.obj2html.use_cookie = use_cookie
    #
    weaver.obj2html.output_as_lines = output_as_lines

    # librarian
    from .Librarian import Librarian
    weaver.obj2html.librarian = Librarian(cssbase=cssbase, jsbase=jsbase)
    
    # load the library
    weaver.use_library_bundle(library_bundle)

    #
    return weaver


def set_default_library_bundle_for_weaver(bundle):
    from .Weaver import Weaver
    Weaver.default_bundle = bundle
    return bundle


# End of file 
