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

class Object2Form(object):


    def __init__(self, object2formfields):
        self.object2formfields = object2formfields
        return


    def __call__(self, obj, title=None, fieldsequence = [], submit='OK', actor=None):
        fields = self.object2formfields(obj)

        record = self.object2formfields.orm.object2record(obj)
        
        if title is None: title = 'Edit %s #%s' % (record.getTableName(), record.id)
        form = lc.form(title=title)

        if not fieldsequence:
            fieldsequence = [d.name for d in obj.Inventory.iterDescriptors()]

        expert_fields = []
        for name in fieldsequence:
            field = fields[name]
            if field:
                desc = obj.Inventory.getDescriptor(name)
                if getattr(desc, 'expert', False):
                    expert_fields.append(field)
                else:
                    form.add(field)
            continue

        doc = lc.document(title='Expert'); form.add(doc)
        doc.collapsable = doc.collapsed = True
        for field in expert_fields:
            doc.add(field)

        form.submitbutton(label=submit)

        if actor is None:
            actor = obj.__class__.__name__.lower()
            
        form.onsubmit = lc.select(element=form).submit(
            actor = actor, routine='process',
            formid = form.id, id = record.id,
            )
        
        return form
        

# version
__id__ = "$Id$"

# End of file 
