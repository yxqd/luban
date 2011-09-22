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
    maxsize = descriptors.int(default=20*1024*1024)
    
    # events
    from luban.ui.Event import Event
    # complete
    class complete(Event):
        # decorations
        simple_description = "event happens when upload is finished" 
        __unique_type_name__ = 'uploadercomplete'
        # attributes
        filename = descriptors.str()
        filename.tip = "filename of the uploaded file"
    # fail
    class fail(Event):
        # decorations
        simple_description = "event happens when upload is failed" 
        __unique_type_name__ = 'uploaderfail'
        # attributes
        reason = descriptors.str()
    # ..
    del Event
    

    # methods
    def identify(self, visitor):
        return visitor.onUploader(self)


# End of file 
