#!/usr/bin/env python3

import sys
sys.path.insert(0, '..')

from cpapp import Root


import unittest
class TestCase(unittest.TestCase):
    
    def test(self):
        root = Root()
        print(root.index(actor='hello'))
        return


def main():
    unittest.main()
    return

if __name__ == '__main__': main()
