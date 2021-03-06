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


from luban import py_major_ver, setup_context
if py_major_ver == 2: setup_context(locals())


from luban.ui.elements.Riveted import RivetedContainer, Meta, RivetedSubElement
from luban.ui.elements.ElementContainer import buildSubElementFactory


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
    # .. for inspector
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
_accordionsectionbase = Meta(
    '_accordionsectionbase',
    (RivetedSubElement, SimpleContainer),
    {'abstract': 1}
    )
class AccordionSection(_accordionsectionbase):

    # decorations
    simple_description = 'one of the panes that can expand or collapse in an accordion'
    full_description = ''

    # 
    parent_types = [Accordion]

    # properties
    label = descriptors.str()
    label.tip = 'label of the accordion section'

    selected = descriptors.bool()
    selected.tip = "whether this section is selected or not. among siblings. only one can be selected"

    # events -- must have one-one correspondence with event handler
    from luban.ui.Event import Event
    class select(Event):
        # decorations
        simple_description = "event happens when this section is selected"
        __unique_type_name__ = 'accordionselect'
        # attributes
        oldsection = descriptors.str()
        newsection = descriptors.str()
    del Event

    # methods
    def identify(self, inspector):
        return inspector.onAccordionSection(self)
    

Accordion.child_types = [AccordionSection]


# subelement factory
buildSubElementFactory('section', AccordionSection, Accordion)


# End of file
