# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from ProjectScriptBase import ProjectScriptBase as base

class StartLubanProject(base):

    class Inventory(base.Inventory):

        import pyre.inventory

        open_browser = pyre.inventory.bool('open-browser', default=True)

        
    def main(self):
        project = self.project

        import os
        if not project:
            path = os.path.abspath(os.curdir)
        else:
            path = os.path.abspath(project)

        project = os.path.split(path)[-1]

        # build commands
        cmds = []

        #
        cmds.append('start-luban-services.py')

        # startservices
        bindir = '%s/bin' % path
        scriptname = 'startservices.sh'
        scriptpath = os.path.join(bindir, scriptname)
        if os.path.exists(scriptpath):
            cmds.append( (bindir, './%s' % scriptname) )

        # http server
        cmds.append(
            ('%s/html' % path,  'SimpleHttpServer.py'),
            )

        # exec cmds
        from luban.utils.sh import execCmds
        execCmds(cmds)

        # wait a bit to let the servers start
        import time
        time.sleep(3)

        url = getUrl(path, project)
        printUrl(url, project)
        if self.inventory.open_browser:
            print ' * starting web browser ... '
            import webbrowser
            webbrowser.open(url)
            # print ' * Please point your browser to http://localhost:%s/cgi-bin/main.py' % port
        return


def getUrl(path, project):
    import os
    config = os.path.join(path, 'config')
    pml = os.path.join(config, 'SimpleHttpServer.pml')
    port = getPort(pml)
    url = 'http://localhost:%s/cgi-bin/main.py' % port
    return url


def printUrl(url, project):
    print
    print ' * luban project %s served at %s' % (project, url)
    print
    return
    

def getPort(pml):
    from xml.etree.ElementTree import ElementTree
    tree = ElementTree()
    tree.parse(pml)
    comp = tree.find('component')
    prop = comp.find('property')
    assert prop.attrib['name'] == 'port'
    return prop.text

        
# version
__id__ = "$Id$"

# End of file 
