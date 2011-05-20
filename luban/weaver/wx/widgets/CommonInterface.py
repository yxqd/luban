#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2009  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# event handler extension
from ext import Extension


class CommonInterface(Extension):


    def __init__(self, parent):
        self.parent = parent
        self.root = parent.root
        self.evtdata = {}
        return


    def getEventData(self, evtname):
        return self.evtdata[evtname]


    def setEventData(self, name, data):
        self.evtdata[name] = data
        return data


    def fit(self):
        wxwidget = self
        sizer = wxwidget.GetSizer()
        if sizer:
            sizer.Fit(wxwidget)
        return
    
    
    def fitall(self):
        self.fit()
        parent = self.getParent()
        if parent and parent is not self: parent.fitall()
        return
    
    
    def setAttribute(self, **attrs):
        raise NotImplementedError
    
    
    def getParent(self):
        return self.parent
    

    def addChild(self, new):
        return addChild(self, new)


    def empty(self):
        return destroyChildren(self)


    def destroy(self):
        return self.Destroy()


    def addClass(self, Class=None):
        # XXX: need implementation here
        return
        

    def removeClass(self, Class=None):
        # XXX: need implementation here
        return


    def show(self):
        self.Show()
        return


    def hide(self):
        self.Hide()
        return


    def enable(self):
        self.Enable()
        return


    def disable(self):
        self.Disable()
        return


    #
    def findFormParent(self):
        '''find the form widget that contains me'''
        from Form import Form
        parent = self.getParent()
        if isinstance(parent, Form): return parent
        return parent.findFormParent()
        

        
def destroyChildren(wxwidget):
    wxsizer = wxwidget.GetSizer()
    wxchildren = wxwidget.GetChildren()
    for wxchild in wxchildren:
        wxsizer.Detach(wxchild)
        wxchild.Destroy()
        continue
    return


def addChild(wxwidget, wxchild, ratio=1.):
    wxsizer = wxwidget.GetSizer()
    wxsizer.add(wxchild, ratio)
    wxsizer.Fit(wxwidget)
    return



# version
__id__ = "$Id$"

# End of file 
