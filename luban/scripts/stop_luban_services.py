#!/usr/bin/env python

cmdsstr = """

journald.py --- -stop
idd.py --- -stop

"""

# ipad.py



def main():
    from luban.utils.sh import execCmdsStr
    execCmdsStr(cmdsstr)
    return


