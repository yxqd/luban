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
from luban.ui.elements.ElementContainer import elementfactory


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
    import luban.ui as lui
    splitter = lui.e.splitter(orientation='horizontal')
    left = splitter.section()
    middle = splitter.section()
    right = splitter.section()
    left.paragraph(text=['left'])
    middle.paragraph(text=['middle'])
    right.paragraph(text=['right'])
    ''',
        ]
    
    abstract = False
    
    # properties
    orientation = descriptors.str(default='horizontal')
    orientation.validators = [validators.choice(['vertical', 'horizontal'])]
    orientation.tip = 'Orientation of the splitter'
    
    
    # methods
    @elementfactory
    def section(self, **kwds):
        section = SplitSection(**kwds)
        self.append(section)
        return section

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
    


# version
__id__ = "$Id$"

# End of file
