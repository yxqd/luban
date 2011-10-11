# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from spawn import spawn
import os

def execCmd(cmd):
    'execute a command'
    print ' * executing %s' % cmd
    ret, out, err =spawn(cmd)
    if ret:
        raise RuntimeError, "failed to execute %r.\noutput:\n%s\nerror:\n%s\n" % (cmd, out, err)
    print out
    return


def execCmds(cmds):
    '''execute a list of commands

    command can be either a string (command itself), or a tuple of (path, command),
    which means that it will cd into the path, and then execute the command.
    '''
    for cmd in cmds:
        if isinstance(cmd, basestring):
            execCmd(cmd)
        else:
            where, cmd = cmd
            pwd = os.path.abspath(os.curdir)
            print ' * cd into %s' % where
            os.chdir(where)
            execCmd(cmd)
            os.chdir(pwd)
    return


def execCmdsStr(cmdsstr):
    'execute a multi-line str. each line is a command'
    cmds = cmdsstr.splitlines()
    cmds = filter(lambda c: c.strip(), cmds)
    execCmds(cmds)
    return


# End of file 
