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


from luban import ui as lui
from .DemoPanelActor import Actor as DemoPanelActor
from .ObjectInterface import Factory as ObjectInterfaceFactory


from luban.controller.Actor import Actor as base
class Actor(base):

    frame_title = None # title of the frame
    interface_factory = None # interface factory
    
    def default(self):
        # frame
        title = self.frame_title
        f = lui.e.frame(title = title)
        
        # interior
        d = self.createInterface()
        
        f.append(d)
        return f


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
            panels.append(panel)
            candidates.append(name)
            continue
        return panels


# End of file 
