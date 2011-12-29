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

from luban import py_major_ver, setup_context
if py_major_ver == 2: setup_context(locals())


from luban.ui.elements.Element import Element

class Uploader(Element):

    # decorations
    simple_description = 'A upload button'
    full_description = ""
    experimental = True

    # attributes
    label = descriptors.str()
    
    maxsize = descriptors.int(default=20*1024*1024)
    maxsize.tip = (
        "hint on the client side the max file size. "
        "this is actually just a hint, since really only server can "
        "dictate the upload size limit. "
        )
    # Note:
    # this hint is implemented now for most browsers except IE.
    # For IE client, we rely on the server side to limit the size
    # of the upload. 
    # This is now implemented in 
    
    multiple = descriptors.bool()
    multiple.tip = "allow multiple uploads"

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
        
        filenames = descriptors.str()
        filenames.tip = "filenames of the uploaded files. useful if upload is multiple"
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
