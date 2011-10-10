# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


K = 1024
M = K * K
G = M * K
T = G * K
def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= T:
        terabytes = bytes / T
        size = '%.2fT' % terabytes
    elif bytes >= G:
        gigabytes = bytes / G
        size = '%.2fG' % gigabytes
    elif bytes >= M:
        megabytes = bytes / M
        size = '%.2fM' % megabytes
    elif bytes >= K:
        kilobytes = bytes / K
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size


# End of file 
