#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                   Jiao Lin
#                        California Institute of Technology
#                          (C) 2007  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from .SimpleContainer import SimpleContainer, Meta
from .ElementContainer import ElementContainer, elementfactory


class Splitter(SimpleContainer):


    simple_description = 'A container of vertically or horizontally aligned sections'
    full_description = (
        "A 'splitter' splits a space into sections vertically or horizontally. "
        "The orientation of the splitter is defined by its attribute 'orientation'. "
        )
    examples = [
        '''
    # the follwoing code creates a splitter that is oriented horizontally and has 3 sections
    import luban.ui.elements
    splitter = luban.ui.elements.splitter(orientation='horizontal')
    left = splitter.section()
    middle = splitter.section()
    right = splitter.section()
    left.paragraph(text=['left'])
    middle.paragraph(text=['middle'])
    right.paragraph(text=['right'])
    ''',
        ]

    abstract = False
    
    @elementfactory
    def section(self, **kwds):
        section = SplitSection(**kwds)
        self.append(section)
        return section


    def identify(self, inspector):
        return inspector.onSplitter(self)


    orientation = descriptors.str(default='horizontal')
    orientation.validators = [validators.choice(['vertical', 'horizontal'])]
    orientation.tip = 'Orientation of the splitter'


from .DocumentFactory import DocumentFactory
from .ParagraphFactory import ParagraphFactory
from .ElementNotRoot import ElementNotRoot
class SplitSection(DocumentFactory, ParagraphFactory, ElementNotRoot, ElementContainer, metaclass=Meta):

    simple_description = 'A section in a splitter'
    full_description = ''

    abstract = False


    def splitter(self, **kwds):
        element = Splitter(**kwds)
        self.append(element)
        return element


    def identify(self, inspector):
        return inspector.onSplitSection(self)

    size = descriptors.str(default=None)
    size.tip = 'deprecated'
    

# only allow splitsection to be children of spltters
Splitter.allowed_element_types = [SplitSection]

# version
__id__ = "$Id$"

# End of file
