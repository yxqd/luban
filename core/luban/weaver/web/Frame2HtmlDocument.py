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


import luban


# renders a ui document into a html document instance and a javascript document
# instance

class Frame2HtmlDocument(object):

    javascript_is_required = "This site requires javascript to be enabled."


    def __init__(
        self, 
        librarian=None, 
        javascriptsbase = 'javascripts', imagesbase='images',
        controller_parameter_prefix = '',  # 'actor.' if use pyre like component structure
        obj2json = None,
        ):
        if librarian is None: raise RuntimeError
        self.librarian = librarian

        self.javascriptsbase = javascriptsbase
        self.imagesbase = imagesbase

        self.controller_parameter_prefix = controller_parameter_prefix

        if obj2json is None: raise RuntimeError
        self.obj2json = obj2json
        return


    def render(
        self, uiobject,
        html_target=None, javascript_target=None,
        ):

        if html_target is None:
            from .content.HtmlDocument import HtmlDocument
            html_target = HtmlDocument()
        self.html_target= html_target
        
        if javascript_target is None:
            from .content.JavaScriptDocument import JavaScriptDocument
            javascript_target = JavaScriptDocument()
        self.javascript_target = javascript_target

        # cover the bases
        # we need to add a few things to head
        htmlroot = html_target.root
            
        librarian = self.librarian
        for category in ['base', 'application']:
            for stylesheet in librarian.getStyleSheets(widget=category):
                htmlroot.stylesheet(url=stylesheet)
            for jslib in librarian.getJavaScriptLibs(widget=category):
                javascript_target.include(script=jslib)

        # the body wrapper div
        html_target.body.tag('div', id='body-wrapper')
        nojs_div = html_target.body.tag('div', id='no-javascript-banner')
        nojs_div.contents = [self.javascript_is_required]

        # image base
        self.javascript_target.main += [
            "$('#no-javascript-banner').remove();",
            
            'luban.configuration.javascripts_base = "%s";' % self.javascriptsbase,
            'luban.configuration.images_base = "%s";' % self.imagesbase,
            'luban.configuration.icons_base = "%s/icons";' % self.imagesbase,
            'luban.Controller.parameter_prefix = "%s";' % self.controller_parameter_prefix,
            ]
        if not luban.debug:
            self.javascript_target.main.append(
                'luban.configuration.debug = false;'
                )
            
        #
        for widget in librarian.iterWidgets():
            if not widget: continue
            stylesheets = librarian.getStyleSheets(widget=widget)
            jslibs = librarian.getJavaScriptLibs(widget=widget)
            d = {'javascripts': jslibs, 'stylesheets': stylesheets}
            d = jsonEncode(d)
            self.javascript_target.main += ["luban.widgets.implementationRegistry.%s = %s;" % (widget, d) ]
            continue

        injson = self.obj2json.render(uiobject)
        
        self.javascript_target.main.append(
            'luban.docmill.render(%s);' % injson)
        return html_target, javascript_target


from ._utils import jsonEncode


from luban import journal
debug = journal.debug('luban.weaver.web')


# version
__id__ = "$Id$"

# End of file 
