#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                     California Institute of Technology
#                       (C) 2008  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .Element import Element
class XYPlot(Element):

    # decorations
    simple_description = 'Plot x-y curve(s)'
    full_description = (
        "A XYPlot widget displays a plot of x-y curve(s)."
        )
    experimental = True
    
    examples = [
        '''
    import luban
    plot = luban.e.xyplot()
    x = range(10)
    y1 = x; y2 = [xi*xi for xi in x]
    plot.curve(x=x, y=y1, label='curve1')
    plot.curve(x=x, y=y2, label='curve2')
        '''
        ]

    # XXX
    # should be a list of Curve objects
    # need a way to validate this
    curves = descriptors.object()
    curves.tip = 'The x-y curves to display'
    
    xticks = descriptors.list()
    xticks.tip = 'ticks for x axis'
    
    yticks = descriptors.list()
    yticks.tip = 'ticks for y axis'
    
    caption = descriptors.str()
    caption.tip = 'caption of the plot'


    # methods
    def curve(self, **kwds):
        curve = Curve(**kwds)
        self.curves.append(curve)
        return
    

    def identify(self, visitor):
        return visitor.onXYPlot(self)


class Curve(Element):

    x = descriptors.array()
    y = descriptors.array()
    label = descriptors.str()

    def identify(self, visitor):
        return visitor.onXYPlotCurve(self)
    

# version
__id__ = "$Id$"

# End of file 
