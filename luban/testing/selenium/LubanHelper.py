# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


class LubanHelper:
    
    
    def __init__(self, selenium):
        self.selenium = selenium
        return
    
    
    def expandDocument(self, **attrs):
        ctrl = self.document_expandcontrol(**attrs)
        s = self.selenium
        s.waitForElementPresent(ctrl)
        s.click(ctrl)
        return
    
    
    def selector(self, tag, **attrs):
        l = []
        tag = "//" + tag; l.append(tag)
        for k, v in attrs.iteritems():
            l.append("[@%s='%s']" % (k, v))
            continue
        return ''.join(l)
    
    
    def formfield(self, type, **attrs):
        s = self.selector('div', **attrs)
        return "%s/table/tbody/tr/td[1]/%s" % (s, type)
    
    
    def document_expandcontrol(self, **attrs):
        s = self.selector('div', **attrs)
        s += "/div[1]/table/tbody/tr/td[1]/a[1]"
        return s
    
    
    def sleep(self, seconds):
        time.sleep(seconds)
        return
    

import time

# version
__id__ = "$Id$"

# End of file 

