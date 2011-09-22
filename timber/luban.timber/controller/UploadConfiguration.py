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


class UploadConfiguration:
    
    limit = 20*1024*1024 # 20M
    timeout = 600 # 10 minutes
    chunk_size = 1024*1024 # 1M  will accept data chunk by chunk
    path = "/tmp/uploads" # temporary path to save upload files


# End of file 

