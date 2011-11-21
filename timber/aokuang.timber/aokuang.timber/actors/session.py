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
url examples:

1. http://localhost:22346/session/set/?a=abc
   set "a" to "abc"
2. http://localhost:22346/session/get/a
   get value of "a"
"""


import luban


from luban.controller.Actor import Actor as base
class Actor(base):

    expose = 1

    
    def set(self, **kwds):
        frame = luban.e.frame(title='set session data')
        doc = frame.document()
        for k, v in kwds.items():
            self.controller.session[k] = v
            doc.paragraph(text='%s=%s' % (k,v))
            continue
        return luban.a.establishInterface(frame)


    def get(self, key, **kwds):
        val = self.controller.session[key]
        frame = luban.e.frame(title='get session data')
        doc = frame.document()
        doc.paragraph(text = '%s=%s' % (key, val))
        return luban.a.establishInterface(frame)



# End of file 

