#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                       (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .Panel import Panel as base
from .CommonInterface import CommonInterface

class Form(base):
    
    def __init__(self, parentWindow, **kwds):
        CommonInterface.__init__(self, parentWindow)
        
        base.__init__(self, parentWindow, **kwds)

        self._input_widgets = {}
        self._input_containers = {}
        return


    def addInputWidget(self, widget):
        self._input_widgets[widget.GetName()] = widget
        return


    def addInputContainer(self, container):
        self._input_containers[container.GetName()] = container
        return


    def serialize(self):
        d = {}
        for name, widget in self._input_widgets.items():
            value = widget.value()
            d[name] = value
            continue
        return d


    def clearErrors(self):
        for name, container in self._input_containers.items():
            try:
                error = container.errorwidget
            except:
                continue
            error.Hide()
            error.fit()
            continue
        
        self.fitall()
        return


    def disable(self):
        # disable all my fields
        for field in self._input_widgets.values():
            field.disable()
            continue
        # disable myself too
        # super(Form, self).disable()
        return
        
    
    def enable(self):
        # enable all my fields
        for field in self._input_widgets.values():
            field.enable()
            continue
        # enable myself too
        # super(Form, self).enable()
        return
        
    
    pass # end of Panel



# version
__id__ = "$Id$"

# End of file 
