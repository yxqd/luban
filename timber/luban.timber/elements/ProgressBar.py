#!/usr/bin/env python
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


from luban.ui.elements.SimpleElement import SimpleElement as base
class ProgressBar(base):

    # decorations
    simple_description = 'An indicator of the progress of some work'
    full_description = (
        "A ProgressBar widget is an indicator of the progress of some work. "
        "Every few seconds (defined by attribute 'skip'), a 'checking' event "
        "will trigger and the event handler for the 'checking' event has to"
        "load the progress status and percentage from the controller, "
        "in order to update the progress bar. "
        "When the progress is 100%, a 'finished' event will trigger and "
        "the 'checking' event will not fire anymore. "
        "Before a progressbar is 'finished', it can be canceled and, "
        "when canceled, a 'canceled' event will trigger. "
        )

    # properties
    skip = descriptors.int()
    skip.tip = "time to skip forward before checking progress. unit: millisecond"

    status = descriptors.str()
    status.tip = "text field to show the status"
    
    percentage = descriptors.int()
    percentage.tip = "percentage of progress"
    
    # events
    # events -- must have one-one correspondence with event handler
    from luban.ui.Event import Event
    #
    class checking(Event):
        # decorations
        simple_description = "checking progress"
        __unique_type_name__ = 'progressbarchecking'
        # attributes
    onchecking = descriptors.eventhandler(eventtype=checking)
    onchecking.notnull = True # force users to define this event handler
    #
    class finish(Event):
        # decorations
        simple_description = "progressbar finished"
        __unique_type_name__ = 'progressbarfinish'
        # attributes
    onfinish = descriptors.eventhandler(eventtype=finish)
    #
    class cancel(Event):
        # decorations
        simple_description = "progressbar canceled"
        __unique_type_name__ = 'progressbarcancel'
        # attributes
    del Event
    

    def identify(self, inspector):
        return inspector.onProgressBar(self)


# actions
# to define a new element action, subclass ElementActionBase
from luban.ui.actions.ElementActionBase import ElementActionBase
class ProgressBarCancelAction(ElementActionBase):

    "cancel a progress bar"
    
    # decorations
    element_type = ProgressBar
    factory_method = "cancel"
    
    # methods
    def identify(self, visitor):
        return visitor.onProgressBarCancelAction(self)


# version
__id__ = "$Id$"

# End of file 
