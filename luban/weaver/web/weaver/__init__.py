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


def weave(htmldoc, javascriptdoc=None):
    if javascriptdoc:
        from .JavaScriptDocument2HtmlDocument import Mill
        mill = Mill()
        mill.render(javascriptdoc, htmldoc)
    return htmlmill().render(htmldoc)


def htmlmill(**kwds):
    from .HtmlDocumentMill import HtmlDocumentMill
    mill = HtmlDocumentMill(**kwds)
    return mill


# version
__id__ = "$Id$"

# End of file 
