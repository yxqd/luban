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


# use DocumentMill and weaver.HtmlDocumentMill to transform a luban document
# to a html page

from pyre.weaver.mills.HTMLMill import HTMLMill as base

class HtmlMill(base):

    # default set of options for HTMLMill base class
    class default_base_options:
        
        author = ''
        organization = ''
        copyright = ''

        bannerWidth = 70
        bannerCharacter = '~'

        creator = ''
        timestamp = 0

        lastLine = ' End of file '
        copyrightLine = '(C) %s  All Rights Reserved'
        licenseText = ["{LicenseText}"]
        
        timestampLine = " Generated automatically by %s on %s"

        versionId = ' $' + 'Id' + '$'


        
    # properties of this luban html mill
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


    def weave(self, document=None):
        if not self._options:
            self._options = self.__class__.default_base_options

        self.begin()
        if document:
            self._renderDocument(document)
            if not self._isFrame(document):
                return self._output()
        self.end()
        return self._output()


    def _output(self):
        if self.output_as_lines:
            return self._rep
        return '\n'.join(self._rep)


    def _renderDocument(self, document):
        html_target = self._createHtmlTarget(document)
        js_target = self._createJSTarget(document)
        
        if self._isFrame(document):
            controller_url = self.controller_url
            js_target.main.append('luban.Controller.url="%s";' % controller_url)
            
            cookie_path = self.cookie_path
            js_target.main.append('luban.Controller.cookie_settings.path="%s";' % cookie_path)

            use_cookie = self.use_cookie
            js_target.main.append('luban.Controller.cookie_settings.use_cookie=%s;' % int(use_cookie))

        librarian = self.librarian

        self.mill = mill = self._createDocumentMill(
            librarian = librarian
            )
        
        from luban.weaver.web.weaver import weave
        if self._isFrame(document):
            htmldoc, jsdoc = mill.render(
                document,
                html_target = html_target,
                javascript_target = js_target,
                )
            texts = weave(htmldoc, javascriptdoc = jsdoc)
            self._rep = texts
        else:
            docinjson = mill.render(
                document,
                html_target = html_target,
                javascript_target = js_target,
                )
            self._rep = docinjson.split('\n')
        return


    def _isFrame(self, document):
        from luban.content.Frame import Frame
        return isinstance(document, Frame)


    def _createDocumentMill(self, librarian):
        from DocumentMill import DocumentMill
        mill = DocumentMill(
            librarian = librarian,
            javascriptsbase = self.javascriptsbase,
            imagesbase = self.imagesbase,
            )
        return mill


    def _createHtmlTarget(self, document):
        from luban.weaver.web.content.HtmlDocument import HtmlDocument, PartialHtmlDocument
        if self._isFrame(document):
            doc =  HtmlDocument()
            doc.base(url=self.htmlbase)
            return doc
        else:
            return PartialHtmlDocument()


    def _createJSTarget(self, document):
        from luban.weaver.web.content.JavaScriptDocument import JavaScriptDocument
        return JavaScriptDocument()


from _utils import jsonEncode


# version
__id__ = "$Id$"

# End of file 
