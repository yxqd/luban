#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import time

import unittest

class TestCaseBase(unittest.TestCase):

    client = None # Fixture.Client
    server = None # Fixture.Server
    targetapp = None # string


    def __init__(self, *args, **kwds):
        super(TestCaseBase, self).__init__(*args, **kwds)
        self.initActor()
        return


    def __del__(self):
        self.finiActor()
        return


    def initActor(self):
        sel = self.initSelenium()
        from Actor import Actor
        self.actor = Actor(sel)
        return


    def finiActor(self):
        del self.actor
        return
    

    def initSelenium(self):
        from selenium import selenium
        if not hasattr(selenium, 'waitForElementPresent'):
            setattr(selenium, 'waitForElementPresent', waitForElementPresent)
            
        s = selenium(self.client.ip, self.client.port, self.client.browser, self.server.host)
        self.appaddress = self.server.appmap[self.targetapp]
        try:
            s.start()
        except:
            import traceback
            tb = traceback.format_exc()
            msg = "Unable to establish selenium server at %s. You will need to install selenium remote control server there, and make sure the browser is present.\n\nCaptured traceback: %s" % (self.client, tb)
            raise RuntimeError, msg

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # temporarily keep this luban helper. but this is to be thrown away
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        from LubanHelper import LubanHelper
        s.lh = s.lubanhelper = LubanHelper(s)

        return s



# extra methods for selenium
def waitForElementPresent(self, element, timeout=60):
    for i in range(timeout):
        try:
            if self.is_element_present(element): break
        except: pass
        time.sleep(1)
    else: raise RuntimeError, "time out"
    return


def testcasefactory(TestCaseBase, client, server):
    class _(TestCaseBase): pass
    _.client = client
    _.server = server
    _.__name__ = 'TestCase'

    # give test methods better doc strings
    import inspect
    for k in dir(_):
        if not k.startswith('test'): continue
        if not k in TestCaseBase.__dict__: continue
        v = getattr(_, k)
        if not inspect.ismethod(v): continue

        # get the original doc
        key = 'original_doc'
        if not hasattr(v, key):
            odoc = v.__doc__ or 'Please add a docstring for method %r' % v
            setattr(v.im_func, key, odoc)
        odoc = getattr(v, key)

        # set new doc
        v.im_func.func_doc = '%s, %s: %s' % (
            client, server.host, odoc)
    return _


def makePySuite(TestCaseBase, fixtures):
    if isinstance(fixtures, basestring):
        fixtures = getFixtures(fixtures)
        
    suite = unittest.TestSuite()
    
    from luban.testing.selenium.Fixture import Client

    for i, fixture in enumerate(fixtures):
        for browser in fixture.browsers:
            client = Client(fixture.computer, browser)
            server = fixture.server
            testcase = testcasefactory(TestCaseBase, client, server)
            suite1 = unittest.makeSuite(testcase)
            suite.addTest(suite1)
            continue
        continue

    return suite


def getFixtures(name):
    pkg = 'luban.testing.selenium.fixtures'
    module = '%s.%s' % (pkg, name)
    module = __import__(module, {}, {}, [''])
    return module.fixtures


# version
__id__ = "$Id$"

# End of file 
