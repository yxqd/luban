#!/usr/bin/env python
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


from Element import Element as base


class Dock(base):


    abstract = False


    def identify(self, inspector):
        return inspector.onDock(self)




from Action import Action as base

class DockAction(base):


    abstract = False


    def identify(self, inspector):
        return inspector.onDockAction(self)
    

    dock = base.descriptors.reference(name='dock')
    widget = base.descriptors.reference(name='widget')
    actionname = base.descriptors.str(name='actionname')



class DockActions(object):


    def dock(self, actionname, widget, **kwds):
        '''
        actionname:
          * attach: attach the widget to the dock
          * release: release the widget from the dock
        '''
        return DockAction(dock=self, actionname=actionname, widget=widget, **kwds)



# version
__id__ = "$Id$"

# End of file 
