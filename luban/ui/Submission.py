# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .Loading import Loading as base

class Submission(base):

    abstract = False


    form = base.descriptors.reference(name='form')

    def __init__(self, form=None, actor=None, routine=None, **params):
        super(Submission, self).__init__(actor=actor, routine=routine, **params)
        self.form = self.elementSelector(form)
        return


    def identify(self, inspector):
        return inspector.onSubmission(self)


# version
__id__ = "$Id$"

# End of file 

