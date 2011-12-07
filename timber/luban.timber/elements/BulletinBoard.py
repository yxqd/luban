#!/usr/bin/env python
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


from luban.ui.elements.Riveted import RivetedContainer, Meta, RivetedSubElement
from luban.ui.elements.ElementContainer import buildSubElementFactory


class BulletinBoard(RivetedContainer):

    # decorations
    simple_description = 'a bulletin board'
    full_description = ''
    
    # properties
    title = descriptors.str()

    # methods
    # .. inspector
    def identify(self, inspector):
        return inspector.onBulletinBoard(self)


from luban.ui.elements.SimpleElement import SimpleElement
class Announcement(RivetedSubElement, SimpleElement, metaclass=Meta):
    
    # decorations
    simple_description = 'An event announcement'
    full_description = ''
    __unique_type_name__ = "bulletinboardannouncement"

    #
    parent_types = [BulletinBoard]

    # properties
    title = descriptors.str()
    
    icon = descriptors.str()
    
    date = descriptors.str()

    time = descriptors.str()

    place = descriptors.str()

    text = descriptors.str()

    authorlist = descriptors.str()

    # events
    
    # methods
    def identify(self, inspector):
        return inspector.onBulletinBoardAnnouncement(self)


BulletinBoard.child_types = [Announcement]


# subelement factory
buildSubElementFactory('announcement', Announcement, BulletinBoard)


# End of file 
