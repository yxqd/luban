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


# transform a luban object to a html text

class HtmlRenderer:


    # properties
    htmlbase = 'http://site/url/'
    javascriptsbase = 'javascripts'
    cssbase = 'css'
    imagesbase = 'images'
    #
    controller_url = '/controller/main.cgi'
    #
    cookie_path = '/'
    use_cookie = False
    # output a list of lines
    # if false, output a big string
    output_as_lines = True
    obj2json = None # luban object -> json repr converter


    # options for creating skeleton
    # of the html text, including things like copyright information
    # header and footer.
    # Not yet used
    class skeleton_options:
        
        author = 'Author'
        organization = 'Organization'
        copyright = 'Copyright'

        bannerWidth = 70
        bannerCharacter = '~'

        creator = ''
        timestamp = 0

        lastLine = ' End of file '
        copyrightLine = '(C) {!s}  All Rights Reserved'
        licenseText = ["{LicenseText}"]
        
        timestampLine = "Generated automatically by {!s}"

        
    def render(self, action):
        from luban.ui.actions.EstablishInterface import EstablishInterface
        if not isinstance(action, EstablishInterface):
            e = "%s is not right type of action. need EstablishInterface" % action
            raise RuntimeError(e)
        self._rep = []
        self.begin()
        self.renderBody(action.frame)
        self.end()
        return self._output()


    def begin(self):
        return

    
    def end(self):
        return


    def renderBody(self, frame):
        # init html docs
        html_target = self._createHtmlTarget(frame)
        js_target = self._createJSTarget(frame)
        
        # luban object -> html doc converter
        frame2htmldoc = self._createDocumentMill(librarian = self.librarian)
        
        # convert luban object to html docs
        htmldoc, jsdoc = frame2htmldoc.render(
            frame,
            html_target = html_target,
            javascript_target = js_target,
            )

        # html docs -> text
        from luban.weaver.web.renderer import render
        texts = render(htmldoc, javascriptdoc = jsdoc)
        self._rep += texts
        return


    def _createDocumentMill(self, librarian):
        from .Frame2HtmlDocument import Frame2HtmlDocument
        mill = Frame2HtmlDocument(
            librarian = librarian,
            javascriptsbase = self.javascriptsbase,
            imagesbase = self.imagesbase,
            obj2json = self.obj2json,
            )
        return mill


    def _createHtmlTarget(self, frame):
        from .content.HtmlDocument import HtmlDocument
        doc =  HtmlDocument()
        doc.base(url=self.htmlbase)
        return doc


    def _createJSTarget(self, frame):
        from .content.JavaScriptDocument import JavaScriptDocument
        js_target = JavaScriptDocument()
        
        # controller properties
        controller_url = self.controller_url
        js_target.main.append('luban.Controller.url="%s";' % controller_url)
            
        cookie_path = self.cookie_path
        js_target.main.append('luban.Controller.cookie_settings.path="%s";' % cookie_path)

        use_cookie = self.use_cookie
        js_target.main.append('luban.Controller.cookie_settings.use_cookie=%s;' % int(use_cookie))

        return js_target


    def _output(self):
        if self.output_as_lines:
            return self._rep
        return '\n'.join(self._rep)


# version
__id__ = "$Id$"

# End of file 
