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


class Client(object):

    
    def __init__(self, server):
        self.server = server
        return
    

    def load(self, actor, routine='default', **params):
        server = self.server
        server.redirect(actor=actor, routine=routine, **params)
        return


    def notify(self, element, evtname, actor, routine='default', **params):
        server = self.server

        evtdata = element.getEventData(evtname)
        
        # XXX: this overrides parameters. could cause trouble
        params.update(evtdata)
        
        return server.redirect(actor=actor, routine=routine, **params)


    def submit(self, form, actor, routine='default', **params):
        # data from form
        formdata = form.serialize()
        
        # extra data from the submission call
        params.update(formdata)

        #
        params = formatArgs(params)
        
        self.load(actor, routine=routine, **params)
        return
    

def formatArgs(args):
    d = {}
    for k, v in args.items():
        k = str(k)
        d[k] = v
        continue
    return d


# version
__id__ = "$Id$"

# End of file 
