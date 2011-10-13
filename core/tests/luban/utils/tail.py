#!/usr/bin/env python3
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import unittest, threading, time

class TestCase(unittest.TestCase):
     
    def test1(self):
        """luban.utils.tail"""
        
        #
        logfile = 'out-testtail.log'
        
        # thread to write file
        class write(threading.Thread):
            def run(self):
                f = open(logfile,'w')
                for i in range(5):
                    f.write('new line\n')
                    f.flush()
                    time.sleep(1)
                    continue
                return
        write().start()
        time.sleep(1)

        from luban.utils.tail import tail
        tail(logfile, duration=5)
        return
     
    
def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
