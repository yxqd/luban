# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

# special containers are containers whose children that cannot be
# independent of their parent. For example, Tab cannot exist without
# a parent, Tabs.


from luban.ui.elements.Tabs import Tabs, Tab
from luban.ui.elements.Splitter import Splitter, SplitSection
from luban.ui.elements.Accordion import Accordion, AccordionSection
containertype2elementtype = {
    Splitter: SplitSection,
    Tabs: Tab,
    Accordion: AccordionSection,
    }


containertypes = iter(containertype2elementtype.keys())


# version
__id__ = "$Id$"

# End of file 
