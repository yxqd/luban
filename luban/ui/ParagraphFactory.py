#!/usr/bin/env python
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


from ElementContainer import elementfactory


class ParagraphFactory(object):

    @elementfactory
    def paragraph(self, **kwds):
        from Paragraph import Paragraph
        paragraph = Paragraph(**kwds)

        self.add(paragraph)

        return paragraph


# version
__id__ = "$Id$"

# End of file 
