#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                   Jiao Lin
#                        California Institute of Technology
#                        (C) 2006-2011  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from .TeleContainer import TeleContainer, TeleSection
from .ElementContainer import elementfactory


class Accordion(TeleContainer):

    simple_description = 'An accordion widget that shows one selected AccordionSection and collapse others'
    full_description = (
        "An accordion can be used to view some mutually exclusive items. "
        "Each item (section) has a title. An accordion item (section) "
        "can be parent of luban elements such as documents, which will "
        "show up when this item was selected."
        )

    abstract = False
    
    onchange = descriptors.action()
    onchange.tip = 'action when a different section was selected'

    @elementfactory
    def section(self, label=None, **kwds):
        section = AccordionSection(label=label, **kwds)
        self.append(section)
        return section


    def identify(self, inspector):
        return inspector.onAccordion(self)



from .DocumentFactory import DocumentFactory
from .ParagraphFactory import ParagraphFactory
class AccordionSection(DocumentFactory, ParagraphFactory, TeleSection):

    simple_description = 'one of the panes that can expand or collapse in an accordion'
    full_description = ''
    abstract = False

    label = descriptors.str()
    label.tip = 'label of the accordion section'

    def identify(self, inspector):
        return inspector.onAccordionSection(self)
    


class AccordionActions:

    def accordion(self, actionname, **kwds):
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(self, actionname, **kwds)


#from ElementActionExtensions import extensions
#extensions.append(AccordionActions)


# only allow accordionsection to be children of accordions
Accordion.allowed_element_types = [AccordionSection]


# version
__id__ = "$Id$"

# End of file
