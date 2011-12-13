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
    def default(self, actor=None, routine=None, *args, **kwds):
        sig = '_escaped_fragment_'
        if sig in kwds:
            fragment = kwds[sig]
            del kwds[sig]
            return self._snapshot(fragment, actor, routine, *args, **kwds)
        return self.run(actor, routine, *args, **kwds)

    
    snapshot_dir = None
    def _snapshot(self, fragment, actor, routine, *args, **kwds):
        snapshot_dir = self.snapshot_dir or "static/snapshots"
        import os
        snapshot_dir = os.path.abspath(snapshot_dir)
        
        from luban.utils.sitemap import hash
        f = os.path.join(snapshot_dir, hash(fragment))
        if not os.path.exists(f):
            return "missing %s" % (f, )
        stream =  open(f, 'rb')
        s = stream.read()
        return s
    
    

# End of file 

