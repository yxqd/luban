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


class CommonElementActionFactory:

    """factory of element actions common for all elements

    Here we only implement one as an example
    """

    def replaceContent(self, newcontent):
        '''replace my content with the given new content '''
        from .ReplaceContent import ReplaceContent
        return ReplaceContent(element=self, newcontent=newcontent)

    pass


# End of file 

