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


from luban.ui import e as lue
import luban.timber # timber extension
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        doc = lue.rstdoc(text="abc")
        return


    def test2(self):
        text = """
Title
=====

List:
* a
* b
* c
"""
        doc = lue.rstdoc(text=text)
        from luban.weaver.web import create as createWeaver
        weaver = createWeaver()
        s = weaver.weave(doc)
        print (s)
        return


def main():
    from luban import journal
    journal.debug('luban.content.ElementContainer').active = 1
    journal.debug('luban.weaver.web.prerenderer').active = 1
    unittest.main()
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
