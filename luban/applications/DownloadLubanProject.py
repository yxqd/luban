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

class DownloadLubanProject(base):

    class Inventory(base.Inventory):

        import pyre.inventory

        auto_expand = pyre.inventory.bool('auto-expand', default=True)
        server = pyre.inventory.str('server', default = 'http://danse.cacr.caltech.edu/packages/dev_danse_us/luban')
        
        
    def main(self):
        name_or_url = self.project

        if isurl(name_or_url):
            url = name_or_url
        else:
            if name_or_url == 'list': return self.showProjectList()
            server = self.inventory.server
            url = '%s/%s.tgz' % (server, name_or_url)

        # version = opts.version
        auto_expand = self.inventory.auto_expand

        # download the file
        filename = url.split('/')[-1]
        download(url, filename)

        # expand the file
        if auto_expand:
            expand(filename)

            
    def showProjectList(self):
        import urllib
        f = urllib.urlopen('%s/PROJECTS' % self.inventory.server)
        lines = [l.strip() for l in f.readlines()]
        for l in lines:
            print ' * %s' % l
            continue
        return
    


def isurl(url):
    return url.find('/') != -1


def expand(filename):
    print ' * expanding %s ...' % filename
    import tarfile
    tar = tarfile.open(filename)
    tar.extractall()
    tar.close()
    return


def download(url, filename):
    print ' * downloading %s to %s ...' % (url, filename)
    import urllib
    return urllib.urlretrieve(url, filename)

        
# version
__id__ = "$Id$"

# End of file 
