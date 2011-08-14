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

import luban.ui.elements as lue


import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        frame = lue.frame()
        d1 = frame.document(name='d1')
        p1 = d1.paragraph(text="hello")
        b1 = lue.button(label='b1', name='b1'); d1.append(b1)
        # print (frame)
        return
     
    
if __name__ == "__main__": unittest.main()

    
# End of file 
