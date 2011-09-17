#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                     California Institute of Technology
#                     (C) 2006-2011  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from luban.ui.elements.Element import Element

class Uploader(Element):

    # decorations
    simple_description = 'A upload button'
    full_description = ""

    # attributes
    label = descriptors.str()
    
    # events
    from luban.ui.Event import Event
    class submit(Event):
        # decorations
        simple_description = "event happens when the uploaded stuff is submitted" 
        __unique_type_name__ = 'uploadersubmit'
        # attributes
        
    class complete(Event):
        # decorations
        simple_description = "event happens when upload is finished" 
        __unique_type_name__ = 'uploaderfinish'
        # attributes
    # ..
    del Event
    

    # methods
    def identify(self, visitor):
        return visitor.onUploader(self)


# End of file 
