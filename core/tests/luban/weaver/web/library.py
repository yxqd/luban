#!/usr/bin/env python3
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from luban.weaver.web.Library import Library, expand


import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        """luban.weaver.web.Library"""
        jquery = Library('jquery', javascripts=['jquery.js'])
        self.assertEqual(Library.get('jquery'), jquery)
        return


    def test2(self):
        """luban.weaver.web.Library.extractAllDeps"""
        Library.reset()
        jquery = Library('jquery', javascripts=['jquery.js'])
        luban = Library('luban', javascripts=['luban.js'], dependencies=['jquery'])
        deps = list(luban.extractAllDeps())
        self.assertEqual(len(deps), 1)
        self.assertEqual(deps[0], jquery)
        return
     
    
    def test3(self):
        """luban.weaver.web.Library.extractAllDeps recurse"""
        Library.reset()
        jquery = Library('jquery', javascripts=['jquery.js'])
        luban = Library('luban', javascripts=['luban.js'], dependencies=['jquery'])
        tabs = Library('luban.tabs', javascripts=['luban.tabs.js'], dependencies=['luban'])
        deps = list(tabs.extractAllDeps())
        self.assertEqual(len(deps), 2)
        self.assertEqual(deps[0], jquery)
        self.assertEqual(deps[1], luban)
        return
     
    
    def test4(self):
        """luban.weaver.web.Library.expand"""
        Library.reset()
        jquery = Library('jquery', javascripts=['jquery.js'])
        luban = Library('luban', javascripts=['luban.js'], dependencies=['jquery'])
        expanded = list(expand((luban)))
        self.assertEqual(len(expanded), 2)
        self.assertTrue(luban in expanded)
        self.assertTrue(jquery in expanded)
        return
     
    
    def test5(self):
        """luban.weaver.web.Library.extractAllDeps exclude_libs"""
        Library.reset()
        jquery = Library('jquery', javascripts=['jquery.js'])
        luban = Library('luban', javascripts=['luban.js'], dependencies=['jquery'])
        jui_tabs = Library('jquery.ui.tabs', dependencies=['jquery'])
        tabs = Library('luban.tabs', javascripts=['luban.tabs.js'], dependencies=['luban', 'jquery.ui.tabs'])
        deps = list(tabs.extractAllDeps(exclude_libs=['luban']))
        self.assertEqual(len(deps), 1)
        self.assertEqual(deps[0], jui_tabs)
        return
     
    
def main():
    from luban import journal
    # journal.debug('luban.weaver.web').activate()
    
    unittest.main()
    return

    
if __name__ == "__main__":
    main()
    
# End of file 
