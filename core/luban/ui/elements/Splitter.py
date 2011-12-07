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



from luban.ui.elements.Riveted import RivetedContainer, Meta, RivetedSubElement
from luban.ui.elements.ElementContainer import buildSubElementFactory


class Splitter(RivetedContainer):

    # decorators
    simple_description = 'A container of vertically or horizontally aligned sections'
    full_description = (
        "A 'splitter' splits a space into sections vertically or horizontally. "
        "The orientation of the splitter is defined by its attribute 'orientation'. "
        )
    examples = [
        '''
    # the follwoing code creates a splitter that is oriented horizontally and has 3 sections
    import luban
    splitter = luban.e.splitter(orientation='horizontal')
    left = splitter.section()
    middle = splitter.section()
    right = splitter.section()
    left.paragraph(text=['left'])
    middle.paragraph(text=['middle'])
    right.paragraph(text=['right'])
    ''',
        ]

    
    # properties
    orientation = descriptors.str(default='horizontal')
    orientation.validator = validators.choice(['vertical', 'horizontal'])
    orientation.tip = 'Orientation of the splitter'
    
    
    # methods
    # .. for inspector
    def identify(self, inspector):
        return inspector.onSplitter(self)


from luban.ui.elements.SimpleContainer import SimpleContainer
class SplitSection(RivetedSubElement, SimpleContainer, metaclass=Meta):

    # decorators
    simple_description = 'A section in a splitter'
    full_description = ''
    abstract = False
    #
    parent_types = [Splitter]

    # attributes
    
    # methods
    # .. for inspector
    def identify(self, inspector):
        return inspector.onSplitSection(self)
    

Splitter.child_types = [SplitSection]


# subelement factory
buildSubElementFactory('section', SplitSection, Splitter)

# End of file
