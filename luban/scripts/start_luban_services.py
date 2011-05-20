#!/usr/bin/env python

cmdsstr = """

journald.py
idd.py

"""

# ipad.py



def main():
    from luban.utils.sh import execCmdsStr
    execCmdsStr(cmdsstr)
    return


