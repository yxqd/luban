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


# create editor view from an object


from ObjectViewBase import Factory as base


class Factory(base):


    def createViewForReferenceSet(
        self, obj, record,
        descriptor,
        actor,
        style=None, actor_formatter=None):
        
        return self._createViewForReferenceSet(
            obj, record,
            descriptor,
            actor,
            style=style, actor_formatter=actor_formatter)



    def __call__(self, obj, title=None, sequence=None, actor=None,
                 style=None, actor_formatter=None):
        
        record = self.orm.object2record(obj)

        # the skeleton
        if title is None:
            if record.id:
                title = '%s #%s' % (record.getTableName().capitalize(), record.id)
            else:
                title = 'New %s' % (record.getTableName(),)
        container = lc.document(title = title, Class='object-editor', collapsable=True)

        # a form for the attributes
        propertiescontainer = container.document(
            title='Properties', Class='object-properties', collapsable=True)
        form = propertiescontainer.form()

        # the actor
        if actor is None:
            actor = self._getActorName(obj.__class__, actor_formatter)
            
        # form fields
        fields = self.tools.obj2formfields(obj)
        if not sequence:
            sequence = [d.name for d in obj.Inventory.iterDescriptors()]

        # iterate over all items
        for item in sequence:
            # item is just a name
            if isinstance(item, basestring):
                name = item
                field = fields[name]
                if field:
                    form.add(field)
                    continue

            # item is a tuple of name, document. just add the document
            elif isinstance(item, tuple) and len(item)==2:
                name, doc = item
                doc.title = "%s==>%s" % (name, doc.title)
                container.add(doc)
                continue

            else:
                raise NotImplementedError

            # no field yet.
            # it might be a reference or a reference set.

            # for reference
            # need to create a panel (owned) or a selector field (not owned)
            descriptor = getattr(obj.Inventory, name)
            value = getattr(obj.inventory, name)
            if descriptor.type == 'reference':
                # reference is owned
                if descriptor.owned:
                    doc = self._createViewForOwnedReference(
                        obj, record,
                        value, descriptor,
                        actor,
                        style=style, actor_formatter=actor_formatter,
                        )
                # reference is NOT owned
                else:
                    form1 = self._createReferenceSelectorForm(
                        descriptor, record,
                        value and self.orm.object2record(value),
                        actor, actor_formatter
                        )
                    
                    doc = lc.document(title=name.capitalize())
                    doc.add(form1)

                    # after form submitted, need to update the view to display view
                    form1.onsubmit.append(
                        select(element=doc).replaceContent(
                          load(actor=actor, routine='displayReferenced',
                               id = record.id, refname=name, actor_formatter=actor_formatter)
                          )
                        )
                doc.addClass('referred-object')
                doc.collapsable = True
                container.add(doc)

            elif descriptor.type == 'referenceset':
                doc = self._createViewForReferenceSet(
                    obj, record,
                    descriptor,
                    actor=actor,
                    style=style, actor_formatter=actor_formatter)
                doc.addClass('object-referenceset')
                container.add(doc)
                
            else:
                raise NotImplementedError
            continue

        form.submitbutton(label='Save')
        form.onsubmit = lc.select(element=form).submit(
            actor = actor, routine='process',
            id = record.id,
            new_display_container_id = propertiescontainer.id,
            new_display_creator = 'displayProperties',
            )

        return container


    # reference set
    def _createViewForReferenceSet(
        self, obj, record,
        descriptor,
        actor,
        style=None, actor_formatter=None):

        orm = self.orm
        
        name = descriptor.name

        set = getattr(obj.inventory, name)

        container = lc.document(Class='container')
        refreshdoc = select(element=container).replaceContent(
            load(actor=actor, routine='createViewForReferenceSet',
                 id = record.id, refname = name)
            )
        
        title = name.capitalize()
        doc = lc.document(title=title, collapsable=True); container.add(doc)

        for i, item in enumerate(set):
            # insert link
            insert = load(
                actor=actor, routine='insertNewReferenceSetItem',
                id = record.id,
                refname = name,
                refvalue = orm.db.getUniqueIdentifierStr(orm(item)),
                position_relative_to_reference = 'before',
                )
            insertlink = lc.link(
                label='Insert a new item',
                onclick = [insert, refreshdoc],
                Class = "insert"
                )
            doc.add(insertlink)
            
            subdoc = self._createViewForItemInReferenceSet(
                obj, record,
                i, item, descriptor,
                actor,
                style=style, actor_formatter=actor_formatter)
            subdoc.collapsable = True
            subdoc.addClass('object-referenceset-item')
            #
            doc.add(subdoc)
            
            # delete link
            delete = load(
                actor=actor, routine='deleteReferenceSetItem',
                id = record.id,
                refname = name,
                refvalue = orm.db.getUniqueIdentifierStr(orm(item)),
                )
            # destroy = select(element=subdoc).destroy()
            deletelink = lc.link(
                label='Delete this item',
                onclick = [delete, refreshdoc],
                Class = "delete",
                )
            subdoc.add(deletelink)

            continue
        
        # append link
        append = load(
            actor=actor, routine='appendNewReferenceSetItem',
            id = record.id,
            refname = name,
            )
        appendlink = lc.link(
            label='Append a new item',
            onclick = [append, refreshdoc],
            Class = "append"
            )
        doc.add(appendlink)
            
        return container


    def _createViewForItemInReferenceSet(
        self, obj, record,
        i, item, descriptor,
        actor,
        style=None, actor_formatter=None):
        
        if descriptor.owned:
            return self._createViewForItemInOwnedReferenceSet(
                obj, record,
                i, item, descriptor,
                actor,
                style =style, actor_formatter=actor_formatter)
        else:
            return self._createViewForItemInNotOwnedReferenceSet(
                obj, record,
                i, item, descriptor,
                actor,
                style =style, actor_formatter=actor_formatter)
        


    def _createViewForItemInOwnedReferenceSet(
        self, obj, record,
        i, item, descriptor,
        actor,
        style=None, actor_formatter=None):
        
        doc = self(item, style=style, actor_formatter=actor_formatter)
        
        # polymorphic reference
        if descriptor.isPolymorphic():
            doc1 = self._createPolymorphicReferenceSetItemEditor(
                obj, record,
                i, descriptor, item,
                actor,
                style=style, actor_formatter=actor_formatter,
                )
            doc1.body.add(doc)
            return doc1
        # normal reference
        else:
            name = descriptor.name
            doc.title = "%s item %s==>%s" % (name, i, doc.title)
            return doc
        


    def _createPolymorphicReferenceSetItemEditor(
        self,
        obj, record, # the "container" object
        i, descriptor, item, # the refset descriptor, the item in the set
        actor, # actor name for the "container" object
        style=None, actor_formatter=None,
        ):

        self._checkPolymorphicReference(descriptor)

        # title
        name = descriptor.name
        title = '%s item %s' % (name.capitalize(), i)
        doc = lc.document(
            title=title, Class='polymorphic-referenceset-item-editor',
            collapsable=True)

        # body section
        body = doc.document(Class='container')
        doc.body = body

        # selector to change type
        targettypes = descriptor.targettypes
        orm = self.orm
        typenames = [orm(t).getTableName() for t in targettypes]
        values = typenames
        entries = zip(values, typenames)
        selector = FormSelectorField(
            label = 'Change to a different type',
            error = 'once changed, all information about the old item will be lost!',
            entries=entries,
            selection=orm(item.__class__).getTableName(),
            )
        doc.add(selector)

        # when user change the type, need to let the container object know
        # and point the reference to the new object, and then
        # also update the editor view
        newtype = select(element=selector).getAttr('value')
        newactorname = load(
            actor=actor, routine='getActorName',
            typename=newtype,
            actor_formatter=actor_formatter)
        #
        orm = self.orm
        uid_for_item = orm.db.getUniqueIdentifierStr(orm(item))
        # a hidden field for uid of item
        hiddenuid = FormTextField(name='??', hidden=True); doc.add(hiddenuid)
        hiddenuid.oncreate = select(element=hiddenuid).setAttr(value=uid_for_item)
        #
        newreferred_uid = load(
            actor = actor, routine='changeType',
            id = record.id,
            refname = name, typename=newtype,
            refvalue=select(element=hiddenuid).getAttr('value'),
            )
        selector.onchange = [
            select(element=hiddenuid).setAttr(value=newreferred_uid),
            select(id=body.id).replaceContent(
            load(actor=newactorname,
                 routine='edit', uid=select(element=hiddenuid).getAttr('value'),
                 actor_formatter = actor_formatter,
                 )
            ),
            ]
        return doc


    def _createViewForItemInNotOwnedReferenceSet(
        self, obj, record,
        i, item, descriptor,
        actor,
        style=None, actor_formatter=None):

        name = descriptor.name
        title = "%s item %s" % (name, i)
        doc = lc.document(title=title)
        
        form = self._createReferenceSetItemSelectorForm(
            obj, record,
            i, item, descriptor,
            actor,
            style=style, actor_formatter=actor_formatter,
            )
        doc.add(form)
        return doc
    

    def _createReferenceSetItemSelectorForm(
        self, obj, record,
        i, item, descriptor,
        actor,
        style, actor_formatter):
        
        form = lc.form()
        
        selector = self._createReferenceSetItemSelector(
            obj, record,
            i, item, descriptor,
            actor,
            style=style, actor_formatter=actor_formatter)
        form.add(selector)

        orm = self.orm
        hiddenfield = FormTextField(
            hidden=1, name='oldrefvalue',
            value=orm.db.getUniqueIdentifierStr(orm(item)))
        form.add(hiddenfield)
        
        form.submitbutton(label='Change')
        
        getselectorvalue = select(element=selector).getAttr('value')
        form.onsubmit = [
            lc.select(element=form).submit(
                actor=actor, routine='changeReferenceSetItem',
                id = record.id,
                refname = descriptor.name,
                ),
            #lc.select(element=hiddenfield).setAttr(value=getselectorvalue),
            ]
        return form        


    def _createReferenceSetItemSelector(
        self, obj, record,
        i, item, descriptor,
        actor,
        style=None, actor_formatter=None,
        ):
        
        name = descriptor.name
        targettype = descriptor.targettype
        if targettype is None:
            self._checkPolymorphicReference(descriptor)

        selector = FormSelectorField(label='Choices:', name='refvalue')

        orm = self.orm
        value=self.orm.db.getUniqueIdentifierStr(orm(item))
        entries = load(
            actor=actor, routine='getSelectorEntriesForReference',
            refname=name, actor_formatter=actor_formatter)
        selector.oncreate = select(element=selector).setAttr(entries=entries, value=value)
        return selector
    
    
    
    # reference
    def _createViewForOwnedReference(
        self, obj, record,
        value, descriptor,
        actor,
        style=None, actor_formatter=None):

        orm = self.orm
        inv = orm.inv(obj)
        
        if value is None:
            value = self._createDefaultValueForReference(descriptor)
            setattr(inv, descriptor.name, value)
            from dsaw.model.Inventory import restoreObjectFromInventory
            restoreObjectFromInventory(obj, inv)
            self.orm.save(obj)
            
        doc = self(value, style=style, actor_formatter=actor_formatter)
        
        # polymorphic reference
        if descriptor.isPolymorphic():
            doc1 = self._createPolymorphicReferenceEditor(
                obj, record,
                descriptor, value,
                actor,
                style=style, actor_formatter=actor_formatter,
                )
            doc1.body.add(doc)
            return doc1
        # normal reference
        else:
            doc.title = "%s==>%s" % (descriptor.name, doc.title)
            return doc


    def _createDefaultValueForReference(self, descriptor):
        if descriptor.isPolymorphic():
            type = descriptor.targettypes[0]
        else:
            type = descriptor.targettype
        return self.orm.objectFactory(type)


    def _createReferenceSelectorForm(self, descriptor, record, referred_record, actor, actor_formatter):
        form = lc.form()
        
        selector = self._createReferenceSelector(
            descriptor, record, referred_record, actor, actor_formatter)
        form.add(selector)

        if referred_record is None:
            label = 'Select'
        else:
            label = 'Change'
            
        form.submitbutton(label=label)
        form.onsubmit = [
            lc.select(element=form).submit(
                actor=actor, routine='changeReference',
                id = record.id,
                refname = descriptor.name, refvalue=select(element=selector).getAttr('value')
                )
            ]
        return form        


    def _createReferenceSelector(self, descriptor, record, referred_record, actor, actor_formatter):
        name = descriptor.name
        targettype = descriptor.targettype
        if targettype is None:
            self._checkPolymorphicReference(descriptor)

        selector = FormSelectorField(label='Choices:')

        if referred_record:
            value=self.orm.db.getUniqueIdentifierStr(referred_record)
        else:
            value=None
        entries = load(
            actor=actor, routine='getSelectorEntriesForReference',
            refname=name, actor_formatter=actor_formatter)
        selector.oncreate = select(element=selector).setAttr(entries=entries, value=value)
        return selector


    def _createPolymorphicReferenceEditor(
        self,
        obj, record, # the "container" object
        descriptor, referred_value, # the referred object
        actor, # actor name for the "container" object
        style=None, actor_formatter=None,
        ):

        self._checkPolymorphicReference(descriptor)

        # title
        name = descriptor.name
        title = name.capitalize()
        doc = lc.document(
            title=title, Class='polymorphic-reference-editor',
            collapsable=True)

        # body section
        body = doc.document(Class='container')
        doc.body = body

        # selector in the title section to select type of referred object
        targettypes = descriptor.targettypes
        orm = self.orm
        typenames = [orm(t).getTableName() for t in targettypes]
        values = typenames
        entries = zip(values, typenames)
        selector = FormSelectorField(
            label = 'Change to a different type',
            error = 'once changed, all information about the old item will be lost!',
            entries=entries,
            selection=orm(referred_value.__class__).getTableName()
            )
        doc.add(selector)

        # when user change the type, need to let the container object know
        # and point the reference to the new object, and then
        # also update the editor view
        newtype = select(element=selector).getAttr('value')
        newactorname = load(
            actor=actor, routine='getActorName',
            typename=newtype,
            actor_formatter=actor_formatter)
        newreferred_uid = load(
            actor = actor, routine='changeType',
            id = record.id,
            refname = name, typename=newtype)
        selector.onchange = select(id=body.id).replaceContent(
            load(actor=newactorname,
                 routine='edit', uid=newreferred_uid,
                 actor_formatter = actor_formatter,
                 )
            )
        return doc


    # helpers
    def _checkPolymorphicReference(self, descriptor):
        targettypes = descriptor.targettypes
        if not targettypes:
            raise RuntimeError, "need to know the possible types for the polymorphic reference. please decorate your reference with keyword 'targettypes'"
        return
    

    def _getActorName(self, kls, actor_formatter=None):
        if actor_formatter is None:
            actor_formatter = actor_default_formatter
        objtypename = self.orm(kls).getTableName()
        return actor_formatter % objtypename



actor_default_formatter = '%s' 

import luban.content as lc
from luban.content import select, alert, load
from luban.content.FormSelectorField import FormSelectorField
from luban.content.FormTextField import FormTextField


# version
__id__ = "$Id$"

# End of file 
