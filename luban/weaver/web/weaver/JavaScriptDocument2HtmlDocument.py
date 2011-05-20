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

# weave JavaScriptDocument into a HtmlDocument

class Mill:

    def render(self, document, htmlDocument):
        includes = document.includes
        for include in includes:
            htmlDocument.script(src=include, contents=[''])

        main = document.main
        if _isFullHtml(htmlDocument):
            start, end = document.main_enclosure
            contents = [start] + main + [end]
        else:
            contents = main
        htmlDocument.script(contents=contents)
        return
    
    
def _isFullHtml(candidate):
    from luban.weaver.web.content.HtmlDocument import HtmlDocument
    return isinstance(candidate, HtmlDocument)



# version
__id__ = "$Id$"

# End of file 
