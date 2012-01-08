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


from luban.timber.controller.CherrypyController import CherrypyController as base
class CherrypyController(base):

    def __init__(self, **kwds):
        super().__init__(**kwds)
        self._initdb()
        return


    def _initdb(self):
        # database session
        from ..db.sqlalchemy_cherrypy_tool import session
        self.db = session
        return


# End of file 
