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

from luban.testing.selenium.TestCaseBase import TestCaseBase as base, makePySuite

class TestCaseBase(base):

    targetapp = 'aokuang'


    def initSelenium(self):
        sele = super(TestCaseBase, self).initSelenium()
        sele.open(self.appaddress)
        return sele


    def test_load(self):
        'aokuang: actions-load'
        actor = self.actor

        actor.select(type='link', label='actions').click()
        actor.select(type='link', label='load').click()

        # demo 1
        b = actor.select(type='button', id='load_example1_button')
        p = actor.select(type='paragraph', id='load_example1_ptoreplace')
        self.assertEqual(p.getText(), 'the text to replace')
        b.click(); actor.sleep(2)
        self.assertEqual(p.getText(), 'newvalue')

        # demo 2
        l = actor.select(type='link', label='Demo 2: load a new UI element')
        l.click()
        b = actor.select(type='button', id='load_example2_button')
        b.click()

        # demo 3
        l = actor.select(type='link', label='Demo 3: load an action')
        l.click()
        b = actor.select(type='button', id='load_example3_button')
        doc = actor.select(type='document', id='document-to-change')
        self.assert_('green-border' not in doc.getAttribute('class').split(' '))
        b.click(); actor.sleep(4)
        self.assert_('green-border' in doc.getAttribute('class').split(' '))

        # API panel
        l = actor.select(type='link', label='Properties')
        l.click()
        return


    def test_select(self):
        'aokuang: actions-select'
        actor = self.actor

        actor.select(type='link', label='actions').click()
        actor.select(type='link', label='select').click()

        # demo 1
        field = actor.select(type='formtextfield', id='comment')
        self.assertEqual(field.getValue(), '')
        
        l = actor.select(type='link', label='click me')
        l.click()

        actor.sleep(1)
        
        self.assertEqual(field.getValue(), 'my comment')
        return


    def test_alert(self):
        'aokuang: actions-alert'
        actor = self.actor

        actor.select(type='link', label='actions').click()
        actor.select(type='link', label='alert').click()

        # demo 1
        actor.select(type='link', label='click me').click()
        self.assertEqual(actor.getAlert(), 'hi, there')        
        return


    def test_table(self):
        'aokuang: table'
        actor = self.actor

        actor.select(type='link', label='misc').click()
        actor.select(type='link', label='table').click()
        
        # the following is to test the editing behavior. but selenum cannot seem
        # to catch lost focus.
        # self.double_click("//table[@id='user-table']/tbody/tr/td[@colname='email']")
        # time.sleep(2)
        # self.click("//table[@id='user-table']/tbody/tr/td[@colname='selected']/input")
        # self.assertEqual(s.get_alert(), 'email updated')
        # time.sleep(2)
        
        actor.select(type='link', label='get checked rows').click()
        actor.sleep(4)
        self.assertEqual(actor.getAlert(), 'checked usernames: []')

        # !!! abstraction for table is not there yet !!!
        actor.selenium.click("//table[@id='user-table']/tbody/tr/td[@colname='selected']/input")
        actor.sleep(1)
        actor.select(type='link', label='get checked rows').click()
        actor.sleep(4)
        self.assertEqual(actor.getAlert(), "checked usernames: ['demo']")
        
        return


    def test_progressbar(self):
        'aokuang: progressbar'
        actor = self.actor

        actor.select(type='link', label='misc').click()
        actor.select(type='link', label='progressbar').click()
        time.sleep(12)
        self.assertEqual(actor.getAlert(), 'done')
        return


def pysuite():
    from fixtures import fixtures
    return makePySuite(TestCaseBase, fixtures)


def main():
    pytests = pysuite()
    import unittest
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__": main()
    
# version
__id__ = "$Id$"

# End of file 
