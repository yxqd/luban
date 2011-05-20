# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.components.Component import Component as base


class ActivityLogger(base):
    

    def __init__(self, name='activity-logger'):
        super(ActivityLogger, self).__init__(name=name, facility = 'activity-logger')
        return


    def log(self, activity):
        self._journal.log(str(activity))
        return


    def _init(self):
        super(ActivityLogger, self)._init()
        
        import journal
        self._journal = journal.info('activities')
        return

    
# version
__id__ = "$Id$"

# End of file 
