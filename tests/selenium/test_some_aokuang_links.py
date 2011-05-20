"""To make this work, first execute start-luban-project.py aokuang to host it on localhost."""

from selenium import selenium
import unittest, time, re

class TestAokuang(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://localhost:8002/cgi-bin/main.py")
        self.selenium.start()
    
    def waitForElementPresent(self, element, timeout=10):
        for i in range(timeout):
            try:
                if self.selenium.is_element_present(element): break
            except: pass
            time.sleep(1)
        else: raise RuntimeError, "time out"

    def test_aokuang(self):
        sel = self.selenium

        def clickLink(linkname):
            self.waitForElementPresent('link=' + linkname)
            sel.click('link=' + linkname)
            return

        sel.open("/cgi-bin/main.py")
        links = ['load', 'select', 'alert', 'basic widgets', 'document', 'form', 'link', \
'button', 'image', 'dialog', 'portlet', 'organizers', 'accordion', 'tabs', 'splitter', \
'grid', 'text-base documents', 'htmldocument', 'restructuredtext', 'graphics', 'plot2d', \
'misc', 'codeeditor', 'progressbar', 'table', 'toolbar', 'newsticker']

        for link in links:
            clickLink(link)
            clickLink('Code')

            try:
                sel.click('Properties')
                sel.click('Events')
                sel.click('Actions')
            except Exception:
                pass
            
        

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
