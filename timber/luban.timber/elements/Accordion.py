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



from luban.ui.elements.Riveted import RivetedContainer, Meta, RivetedSubElement
from luban.ui.elements.ElementContainer import elementfactory


class Accordion(RivetedContainer):

    # decorations
    simple_description = 'An accordion widget that shows one selected AccordionSection and collapse others'
    full_description = (
        "An accordion can be used to view some mutually exclusive items. "
        "Each item (section) has a title. An accordion item (section) "
        "can be parent of luban elements such as documents, which will "
        "show up when this item was selected."
        )

    # properties
    
    # events

    # methods
    @elementfactory
    def section(self, label=None, **kwds):
        kwds['label'] = label
        from luban.ui.elements.SubElementFactory import createSubElement
        return createSubElement(self, AccordionSection, **kwds)
    

    def identify(self, inspector):
        return inspector.onAccordion(self)


    # XXX: need more thoughts 
    # this helps establish the context in which derived element types
    # would be defined. see ..AttributeContainer.Meta for more details
    @classmethod
    def __get_subclass_preparation_context__(cls):
        d = super().__get_subclass_preparation_context__()
        d['Section'] = d['AccordionSection']
        return d



from luban.ui.elements.SimpleContainer import SimpleContainer
class AccordionSection(RivetedSubElement, SimpleContainer, metaclass=Meta):

    # decorations
    simple_description = 'one of the panes that can expand or collapse in an accordion'
    full_description = ''

    # 
    parent_types = [Accordion]

    # properties
    label = descriptors.str()
    label.tip = 'label of the accordion section'

    # methods
    def identify(self, inspector):
        return inspector.onAccordionSection(self)
    

Accordion.child_types = [AccordionSection]


# End of file
