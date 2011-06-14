#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin     
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .SimpleContainer import SimpleContainer as base


class NewsTicker(base):

    simple_description = 'Displays news headers periodically'
    full_description = (
        "A newsticker widget rotates headers of news items. "
        "A news item will stay a few seconds (defined by attribute 'delay'). "
        "A newsticker will triggers 'refresh' event every few moments "
        "(defined by attribute 'refreshtime'), which can be used to "
        "retrieve a new set of news items, for example."
        )

    abstract = False
    experimental = True

    title = descriptors.str(name='title')
    title.tip = 'Title of the widget'
    
    delay = descriptors.int(name='delay')
    delay.tip = 'idle time before the next news item shows up. unit: seconds'

    
    refreshtime = descriptors.int(name='refreshtime')
    refreshtime.tip = 'time elapsed before the refresh event fires. unit: seconds'

    onrefresh = descriptors.action()
    onrefresh.tip = 'event handler that triggers at refresh event'
    

    def item(self, **kwds):
        pi = NewsTickerItem(**kwds)
        self.add(pi)
        return pi


    def identify(self, inspector):
        return inspector.onNewsTicker(self)



from .Element import Element

class NewsTickerItem(Element):


    abstract = False
    
    text = descriptors.list(name='text')
    
    def identify(self, inspector):
        return inspector.onNewsTickerItem(self)
    

# only allow newstickeritems to be children of newstickers
NewsTicker.allowed_element_types = [NewsTickerItem]

# version
__id__ = "$Id$"

# End of file 
