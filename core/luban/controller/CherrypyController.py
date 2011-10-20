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


import cherrypy


from .WebAppController import WebAppController
class CherrypyController(WebAppController):
    
    @cherrypy.expose
    def index(self, actor=None, routine=None, *args, **kwds):
        if "_escaped_fragment_" in kwds:
            return self._snapshot()
        return self.run(actor, routine, *args, **kwds)
    default = index


    def _snapshot(self):
        url = cherrypy.url()
        url = url.replace("?_escaped_fragment_=", "#!")
        jar = getHSnapshotJar()
        cmd = 'java -jar %s %s' % (jar, url)
        import subprocess
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if p.wait(): raise RuntimeError("failed to create snapshot: %s" % err)
        return out


def getHSnapshotJar():
    f = __file__
    import os
    dir = os.path.dirname(f)
    return os.path.join(dir, 'hsnapshot.jar')

    
# End of file 

