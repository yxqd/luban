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



# _createfield_for_<propertyname> can be overloaded to provide custom behavior
# overload should happen in customizeLubanObjectDrawer method.


import luban.content as lc


from MoldBase import MoldBase

class ObjectPropertiesMold(MoldBase):


    # sequence of properties
    sequence = None


    def __call__(self, obj, readonly=False, **kwds):
        if readonly:
            f = self._readonlyview
        else:
            f = self._editableview
        return f(obj, **kwds)


    def _editableview(self, obj):
        doc = lc.document(Class='container')
        doc.add(self._form(obj))
        return doc


    def _form(self, obj):
        # a form for the attributes
        form = lc.form(
            name='properties-form',
            Class='%s-properties-form' % obj.__class__.__name__.lower())
        #
        self._addfieldstoform(form, obj)
        #
        return form


    def _createfields(self, obj):
        fields = self.o2f(obj)
        # special handler
        sequence = self._getSequence(obj)
        for name in sequence:
            handler = "_createfield_for_%s" % name
            if not hasattr(self, handler): continue
            handler = getattr(self, handler)
            fields[name] = handler(obj)
            continue
        return fields


    def _addfieldstoform(self, form, obj):
        # form fields
        fields = self._createfields(obj)

        #
        sequence = self._getSequence(obj)

        
        expert_fields = []

        # iterate over all items
        for item in sequence:

            name = item
            descriptor = getattr(obj.Inventory, name)
            #if descriptor.type in ['reference', 'referenceset']:
            #    continue
            field = fields[name]

            if field:
                desc = obj.Inventory.getDescriptor(name)
                if getattr(desc, 'expert', False):
                    expert_fields.append(field)
                else:
                    form.add(field)
            continue

        #
        if expert_fields:
            doc = lc.document(title='Expert'); form.add(doc)
            doc.collapsable = doc.collapsed = True
            for field in expert_fields:
                doc.add(field)
                continue

        form.submitbutton(label='Save')

        form.onsubmit = lc.select(element=form).submit(
            actor = self.actor, routine='process',
            id = self.orm(obj).id,
            old_display_id = form.id,
            formid = form.id,
            new_display_creator = 'displayProperties',
            )

        return 


    def _readonlyview(self, obj, editlink=False):
        doc = lc.document(Class='container')
        
        grid = lc.grid(Class='object-properties properties')
        doc.add(grid);

        reftypes = ['reference', 'referenceset']
        for item in self._getSequence(obj):
            desc = getattr(obj.Inventory, item)
            # if desc.type in reftypes: continue
            row = grid.row()
            name = desc.name
            value = getattr(obj.inventory, name)
            row.cell(Class='prop-name').add(name)
            row.cell(Class='prop-value').add(str(value))
            continue

        if editlink:
            editlink = lc.link(label='edit')
            editlink.onclick = lc.select(element=doc).replaceBy(
                lc.load(actor=self.actor, routine='editProperties',
                        id = self.orm(obj).id)
                )
            doc.add(editlink)
        
        return doc


    def _getSequence(self, obj):
        sequence = self.sequence
        if not sequence:
            sequence = [d.name for d in obj.Inventory.getDescriptors()]
        return sequence


    def _getO2F(self):
        from luban.orm.Object2FormFields import Object2FormFields
        return Object2FormFields(self.orm)
    o2f = property(_getO2F)


# version
__id__ = "$Id$"

# End of file 
