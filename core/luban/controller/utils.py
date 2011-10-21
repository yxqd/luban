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


def getSnapshot(url):
    jar = getHSnapshotJar()
    cmd = 'java -jar %s %s' % (jar, url)
    import subprocess
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    
    if p.wait(): 
        raise RuntimeError(
            "failed to create snapshot for %s:\n%s" % (
                url, err)
            )
    return out

        
def getHSnapshotJar():
    f = __file__
    import os
    dir = os.path.dirname(f)
    return os.path.join(dir, 'hsnapshot.jar')

    
# End of file 

