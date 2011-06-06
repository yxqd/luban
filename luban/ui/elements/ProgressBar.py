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


from .Element import Element


class ProgressBar(Element):


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

    abstract = False

    skip = descriptors.int(name='skip')
    onchecking = descriptors.eventHandler(name='onchecking')
    onfinished = descriptors.eventHandler(name='onfinished')
    oncanceled = descriptors.eventHandler(name='oncanceled')
    
    status = descriptors.str(name='status')
    percentage = descriptors.int(name='percentage')

    def identify(self, inspector):
        return inspector.onProgressBar(self)


class ProgressBarActions:

    def progressbar(self, actionname, **kwds):
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(self, actionname, **kwds)
    


# version
__id__ = "$Id$"

# End of file 
