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

import luban.content as lc
from luban.content.FormTextField import FormTextField
from luban.content.FormSelectorField import FormSelectorField
from luban.content.FormCheckBox import FormCheckBox
from luban.content.FormRadioBox import FormRadioBox
from luban.content.FormTextArea import FormTextArea

class Object2FormFields(object):

    rules = {}

    def __init__(self, orm, rules=None):
        self.orm = orm
        
        default = self.__class__.rules.copy()
        if rules:
            default.update(rules)
        self.rules = rules
        return


    def __call__(self, obj):
        record = self.orm.object2record(obj)
        visuals = {}
        for descriptor in obj.Inventory.iterDescriptors():
            type = descriptor.type
            handler = '_on%s' % type.capitalize()
            handler = getattr(self, handler)
            visual = handler(descriptor, record)
            visuals[descriptor.name] = visual
            continue
        return visuals


    def _onReference(self, descriptor, record):
        return


    def _onReferenceset(self, descriptor, record):
        return


    def _onStr(self, descriptor, record):
        if self._hasChoice(descriptor):
            choices = descriptor.validator.value
            return self._onChoice(descriptor, record, choices)
        return self._onSimpleAttribute(descriptor, record, FormTextField)


    def _onInt(self, descriptor, record):
        if self._hasChoice(descriptor):
            choices = descriptor.validator.value
            return self._onChoice(descriptor, record, choices)
        return self._onSimpleAttribute(descriptor, record, FormTextField)


    def _onFloat(self, descriptor, record):
        if self._hasChoice(descriptor):
            choices = descriptor.validator.value
            return self._onChoice(descriptor, record, choices)
        return self._onSimpleAttribute(descriptor, record, FormTextField)


    def _onDate(self, descriptor, record):
        return self._onSimpleAttribute(descriptor, record, FormTextField)


    def _onBool(self, descriptor, record):
        return self._onSimpleAttribute(descriptor, record, FormCheckBox)


    def _onArray(self, descriptor, record):
        name = descriptor.name
        value = getattr(record, name)
        if value is None:
            return

        shape = descriptor.shape
        if shape:
            if isinstance(shape, tuple):
                if len(shape)==2:
                    return self._onMatrix(descriptor, shape, record)
                elif len(shape)==1:
                    length = shape[0]
                    return self._onVector(descriptor, length, record)
            elif isinstance(shape, int):
                length = shape
                return self._onVector(descriptor, length, record)
            raise ValueError, 'shape: %s' % (shape,)
                
        # value is usually a numpy array, convert to list to better formatting
        value = list(value)
        label = _label(descriptor)
        try:
            help = descriptor.help
        except:
            help = ''

        try:
            tip = descriptor.tip
        except:
            tip = ''
            
        return FormTextField(
            name = name,
            value = value,
            label = label,
            help = help,
            tip = tip,
            )


    def _onMatrix(self, descriptor, shape, record):
        nrows, ncols = shape
        if nrows > 10 and ncols > 10: raise NotImplementedError
        
        name = descriptor.name
        value = getattr(record, name)
        label = _label(descriptor)
        try:
            help = descriptor.help
        except:
            help = ''

        try:
            tip = descriptor.tip
        except:
            tip = ''

        doc = lc.document(title=label)
        if help:
            doc.document(Class='help').paragraph(text=[help])
        if tip:
            doc.tip = tip
        grid = lc.grid(); doc.add(grid)

        if descriptor.elementtype == 'bool':
            factory = FormCheckBox
        else:
            factory = FormTextField

        for i in range(nrows):
            gr = grid.row()
            for j in range(ncols):
                gc = gr.cell()
                v = value[i,j]                
                w = factory(value=v,name='%s_%s_%s' % (name, i, j) )
                gc.add(w)
                
        return doc
        


    def _onVector(self, descriptor, length, record):
        if length > 10: raise NotImplementedError
        
        name = descriptor.name
        value = getattr(record, name)
        label = _label(descriptor)
        try:
            help = descriptor.help
        except:
            help = ''

        try:
            tip = descriptor.tip
        except:
            tip = ''

        doc = lc.document(title=label)
        if help:
            doc.document(Class='help', name='%s-help'%name)\
                .paragraph(text=[help])
        if tip:
            doc.tip = tip
        grid = lc.grid(name='grid'); doc.add(grid)

        if descriptor.elementtype == 'bool':
            factory = FormCheckBox
        else:
            factory = FormTextField

        gr = grid.row()
        ncols = length
        for j in range(ncols):
            gc = gr.cell()
            v = value[j]
            w = factory(value=v,name='%s_%s' % (name, j) )
            gc.add(w)
                
        return doc
        


    def _hasChoice(self, descriptor):
        return descriptor.validator.__class__.__name__.lower() == 'choice'


    def _onChoice(self, descriptor, record, choices):
        name = descriptor.name
        value = getattr(record, name)
        label = _label(descriptor)

        try:
            help = descriptor.help
        except:
            help = ''
            
        try:
            tip = descriptor.tip
        except:
            tip = ''

        return FormSelectorField(
            name = name,
            value = value,
            label = label,
            help = help,
            tip = tip,
            entries = zip(choices, choices),
            )
        


    def _onSimpleAttribute(self, descriptor, record, factory):
        name = descriptor.name
        value = getattr(record, name)
        label = _label(descriptor)
        try:
            help = descriptor.help
        except:
            help = ''
            
        try:
            tip = descriptor.tip
        except:
            tip = ''

        return factory(
            name = name,
            value = value,
            label = label,
            help = help,
            tip = tip,
            )



def _label(descriptor):
    if hasattr(descriptor, 'label'): return descriptor.label
    return descriptor.name.replace('_', ' ')

# version
__id__ = "$Id$"

# End of file 
