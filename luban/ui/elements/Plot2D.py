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
class Plot2D(Element):

    simple_description = 'Plot x-y curve(s)'
    full_description = (
        "A Plot2D widget displays a plot of x-y curve(s)."
        )
    examples = [
        '''
    import luban.content
    plot = luban.content.plot2d()
    x = range(10)
    y1 = x; y2 = [xi*xi for xi in x]
    plot.curve(x=x, y=y1, label='curve1')
    plot.curve(x=x, y=y2, label='curve2')
        '''
        ]

    curves = descriptors.referenceSet(name='curves')
    curves.tip = 'The x-y curves to display'
    
    xticks = descriptors.list(name='xticks')
    xticks.tip = 'ticks for x axis'
    
    yticks = descriptors.list(name='yticks')
    yticks.tip = 'ticks for y axis'
    
    caption = descriptors.str(name='caption')
    caption.tip = 'caption of the plot'

    abstract = False
    experimental = True

    def curve(self, **kwds):
        curve = Curve(**kwds)
        self.curves.append(curve)
        return
    

    def identify(self, visitor):
        return visitor.onPlot2D(self)


class Curve(Element):

    x = descriptors.array(name='x')
    y = descriptors.array(name='y')
    label = descriptors.str(name='label')

    def identify(self, visitor):
        return visitor.onPlot2DCurve(self)
    

# version
__id__ = "$Id$"

# End of file 
