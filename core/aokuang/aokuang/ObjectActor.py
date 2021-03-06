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


"""
actor base class for luban ui objects
"""


from luban import py_major_ver


import luban
from .DemoPanelActor import Actor as DemoPanelActor
from .ObjectInterface import Factory as ObjectInterfaceFactory


from luban.controller.Actor import Actor as base
class Actor(base):

    frame_title = None # title of the frame
    interface_factory = None # interface factory
    
    
    def default(self):
        # frame
        title = self.frame_title
        f = luban.e.frame(title = title)
        container = f.document(id='demo-container')

        # link to root demo
        text = '<a class="ext" href="/"><< aokuang</a>'
        container.htmldocument(text = text)
        
        # interior
        d = self.createInterface()
        
        container.append(d)
        return luban.a.establishInterface(f)


    def createInterface(self, **kwds):
        # interior
        self.interface_factory.controller = self.controller
        self.interface_factory.actor = self.name
        self.interface_factory.demo_panels = self._findDemoPanels()
        return self.interface_factory.create()


    def _findDemoPanels(self):
        # find demo panels by import all modules
        # and find those modules with demo panel actors
        # assumption: each module has one class "Actor" that
        # is inherited from .DemoPanelActor

        from luban.utils.importer import import_module

        import os
        d = os.path.dirname(self.py_pkg_path)
        
        entries = os.listdir(d)
        candidates = []; panels = []
        exts = ['.py', '.pyc', '.pyo']
        for entry in entries:
            if entry.startswith('_'):
                continue
            
            # some modules only work for a specific python version
            if entry.startswith('pyv'):
                sig = 'pyv%s' % py_major_ver
                if not entry.startswith(sig):
                    continue
                
            for ext in exts:
                if entry.endswith(ext): break
                continue
            else:
                continue
            name = entry[:-len(ext)]
            if name in candidates:
                continue
            # m = __import__('.'+name, fromlist=[''])
            m = import_module(name, pkg=self.py_pkg_name)
            Actor = getattr(m, 'Actor', None)
            if not Actor or not issubclass(Actor, DemoPanelActor):
                continue
            
            panel = ObjectInterfaceFactory.DemoPanel()
            panel.title = Actor.title
            panel.actor_name = '%s.%s' % (self.name, name)
            if hasattr(Actor, 'rank'):
                panel.rank = Actor.rank
                
            panels.append(panel)
            candidates.append(name)
            continue
        if panels:
            if hasattr(panels[0], 'rank'):
                panels = _sortPanels(panels)
        return panels


def _sortPanels(panels):
    def key(p):
        try:
            return p.rank
        except AttributeError:
            raise RuntimeError("panel %s does not have a rank" % p.actor_name)
    panels.sort(key=key)
    return panels


# End of file 
