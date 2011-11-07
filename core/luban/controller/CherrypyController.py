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
        sig = '_escaped_fragment_'
        if sig in kwds:
            fragment = kwds[sig]
            del kwds[sig]
            return self._snapshot(fragment, actor, routine, *args, **kwds)
        return self.run(actor, routine, *args, **kwds)
    default = index


    def _snapshot(self, fragment, actor, routine, *args, **kwds):
        
        url = self.url
        if not url.startswith('http:'):
            url = cherrypy.url(self.url)
            
        # args = (actor or 'default', routine or 'default') + args
        # argstr = '/'.join(args)
        # kargstr = '&'.join('%s=%s' % (k,v) for k,v in kwds.items())
        # url += argstr + '?' + kargstr
        url += fragment
        
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

