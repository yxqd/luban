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
This controller should support as many features as possible.
"""


from .CherrypyController import CherrypyController as base
class Base(base):

    def __init__(self, **kwds):
        
        from luban import py_major_ver
        if py_major_ver == 2:
            superme = super(Base, self)
        elif py_major_ver == 3:
            superme = super()

        superme.__init__(**kwds)
        self._initdb()
        return


    def _initdb(self):
        # db mixin should override this
        return
    
    pass


# mixin class to add sqlalchemy db support 
class UseSqlalchemy:

    def _initdb(self):
        
        import cherrypy, luban

        try:
            import sqlalchemy
        except ImportError:
            import traceback; tb = traceback.format_exc()
            import warnings
            warnings.warn("sqlalchemy not available: %s" % tb)
            return

        from luban.db import sqlalchemy
        try:
            luban.app_config.db
        except:
            import traceback; tb = traceback.format_exc()
            import warnings
            warnings.warn("db not configured: %s" % tb)
            return
        
        cherrypy.config.update({
            'tools.SATransaction.on': True,
            'tools.SATransaction.dburi': luban.app_config.db.uri,
            'tools.SATransaction.echo': luban.app_config.db.echo,
            'tools.SATransaction.convert_unicode': luban.app_config.db.convert_unicode,
            })
        
        from luban.db.sqlalchemy_cherrypy_tool import session
        self.db = session
        return


#
class CherrypyFullController(UseSqlalchemy, Base):

    pass

    
# End of file 

