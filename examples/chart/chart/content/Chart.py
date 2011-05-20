#!/usr/bin/env python

from luban.content.Element import Element

class Chart(Element):

    simple_description = 'Chart'
    full_description = ''

    curves = Element.descriptors.referenceSet(name='curves')
    curves.tip = 'The x-y curves to display'

    caption = Element.descriptors.str(name='caption')
    caption.tip = 'caption of the plot'

    xrange = Element.descriptors.array(name='xrange')
    yrange = Element.descriptors.array(name='yrange')
    zrange = Element.descriptors.array(name='zrange')

    abstract = False
    experimental = True


    def curve(self, **kwds):
        curve = ChartCurve(**kwds)
        self.curves.append(curve)
        return
    

    def identify(self, visitor):
        return visitor.onChart(self)

    

class ChartCurve(Element):

    x = Element.descriptors.array(name='x')
    y = Element.descriptors.array(name='y')
    z = Element.descriptors.array(name='z')
    label = Element.descriptors.str(name='label')

    def identify(self, visitor):
        return visitor.onChartCurve(self)
    
    
