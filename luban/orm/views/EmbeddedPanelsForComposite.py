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



from CompositeOrganizerBase import CompositeOrganizerBase as base

class EmbeddedPanelsForComposite(base):


    title = None # title of outmost panel
    sequence = None # sequence of panels (a list of strings). "properties" means properties panel, other strings are regarded as names of references or reference sets
    readonly_view_sequence = None # if this is None, defaults to sequence. sequence of panels (a list of strings) for the readonly view. "properties" means properties panel. other strings are regarded as names of references or reference sets
    
    
    def createViewForReferenceSet(
        self, obj, descriptor,
        edithierarchy=True,
        ):
        actor = self.actor
        orm = self.orm
        record = orm(obj)
        return self._createViewForReferenceSet(
            obj, record,
            descriptor,
            actor,
            edithierarchy = edithierarchy
            )


    def createSubViewForAnItemInReferenceSet(
        self, obj, descriptor, item,
        edithierarchy = True,
        ):
        orm = self.orm
        record = orm(obj)
        
        actor = self.actor
        
        return self._createSubDocumentForItemInReferenceSet(
            obj, record,
            descriptor,
            item,
            actor,
            edithierarchy = edithierarchy,
            )


    def createReferenceSelectorForm(
        self, obj, descriptor,):

        record = self.orm(obj)
        value = getattr(obj.inventory, descriptor.name)
        actor = self.actor
        
        return self._createReferenceSelectorForm(
            descriptor, record,
            value and self.orm(value),
            actor
            )


    def createPropertiesForm(self, obj):
        # adjust myself to suit the particalur obj
        self.adjustTo(obj)        
        return self.mold(obj)


    def createPropertiesView(self, obj, **kwds):
        # adjust myself to suit the particalur obj
        self.adjustTo(obj)
        return self.mold(obj, readonly=1, **kwds)
            

    def _createMold(self):
        from ObjectPropertiesMold import ObjectPropertiesMold
        return ObjectPropertiesMold(self.orm, self.actor)
    def _getMold(self):
        if hasattr(self, '_mold'): return self._mold
        r = self._createMold()
        self._mold = r
        return r
    mold = property(_getMold)


    def __call__(self, obj, readonly=False, **kwds):
        # adjust myself to suit the particalur obj
        self.adjustTo(obj)
        
        if readonly:
            return self.createReadOnlyView(obj, **kwds)
        return self.createEditableView(obj, **kwds)


    def createReadOnlyView(self, obj, editlink=True):
        
        # adjust myself to suit the particalur obj
        self.adjustTo(obj)

        actor = self.actor
        
        orm = self.orm
        record = orm(obj)
        
        title = self.title
        if title is None: title = self.makeTitle(obj)
        container = lc.document(title = title, Class='object-viewer', collapsable=True)

        if editlink:
            editview = load(actor=self.actor, routine='edit', id=record.id)
            changeviewtoedit = select(element=container).replaceBy(editview)
            link = lc.link(label='edit', onclick=changeviewtoedit)
            container.add(link)
            
        sequence = self.readonly_view_sequence or self.sequence
        if sequence is None: sequence = self.makeSequence(obj)
        
        for name in sequence:
            
            if name == 'properties':
                propertiescontainer = container.document(
                    title='Properties', Class='object-properties', collapsable=True)
                doc = self.createPropertiesView(obj)
                propertiescontainer.add(doc)
                continue

            descriptor = getattr(obj.Inventory, name)
            value = getattr(obj.inventory, name)
            
            if descriptor.type == 'reference':

                subdoc = self._createReadonlyViewForReference(
                    descriptor, value, editlink=editlink)
                container.add(subdoc)
                    
                
            elif descriptor.type == 'referenceset':
                subdoc = self._createReadonlyViewForReferenceSet(
                    descriptor, value, editlink=editlink)
                container.add(subdoc)

        if editlink:
            link2 = lc.link(label='edit', onclick=changeviewtoedit)
            container.add(link2)
            
        return container


    def _createReadonlyViewForReference(self, descriptor, value, editlink):
        title = descriptor.name
        doc = lc.document(title=title, collapsable=True)
        if value is None:
            doc.paragraph(text='None')
            return doc
        label = 'click for details'
        link = lc.link(label = label); doc.add(link)

        # action
        # .. actor
        actor = getattr(
            value, 
            'luban_orm_actor',
            'orm/%ss' % value.__class__.__name__.lower(),
            )
        # .. routine
        if editlink:
            routine = 'display'
        else:
            routine = 'display_noedit'
        # .. id
        record = self.orm(value)
        id = record.id
        # .. assign action
        link.onclick = select(element=doc).replaceBy(
            load(actor=actor, routine=routine, id = id)
            )
        return doc


    def _createReadonlyViewForReferenceSet(self, descriptor, items, editlink):
        subdoc = lc.document(
            title = descriptor.name, collapsable = True, collapsed = True)

        for item in items:
            # link
            # .. id
            record = self.orm(item)
            id = record.id
            # .. label
            label = '%s %s - click for details' % (
                item.__class__.__name__, id)
            link = lc.paragraph(text = '* ' + label)
            # .. append
            subdoc.add(link)

            # action
            # .. actor
            actor = getattr(
                item, 
                'luban_orm_actor',
                'orm/%ss' % item.__class__.__name__.lower(),
                )
            # .. routine
            if editlink:
                routine = 'display'
            else:
                routine = 'display_noedit'
            # .. assign action
            link.onclick = select(element=link).replaceBy(
                load(actor=actor, routine=routine, id = id)
                )
            continue
        return subdoc
        subdoc = lc.document(
            title = descriptor.name, collapsable = True, collapsed = True)

        for item in items:
            subsubdoc = subdoc.document(title='Item', collapsable=True)

            drawer = self.drawers.getDrawer(item.__class__)
            view = drawer(item, readonly=True, editlink=editlink and descriptor.owned)

            subsubdoc.add(view)
            continue
        return subdoc


    def createEditableView(self, obj, edithierarchy=True):
        '''create an "editable" view of the given object

        edithierarchy:
            if it is true, there will be insert/append/delete links
            in the view to insert/append/delete new items to reference set.
            on the other word, if it is true, user can use this view
            to change the hierarchy structure of the object.
        '''

        # adjust myself to suit the particalur obj
        self.adjustTo(obj)

        actor = self.actor
        
        orm = self.orm
        record = orm(obj)
        
        title = self.title
        if title is None: title = self.makeTitle(obj)
        container = lc.document(title = title, Class='object-editor', collapsable=True)

        sequence = self.sequence
        if sequence is None: sequence = self.makeSequence(obj)
        
        for name in sequence:
            
            if name == 'properties':
                propertiescontainer = container.document(
                    title='Properties', Class='object-properties', collapsable=True)
                doc = self.createPropertiesForm(obj)
                propertiescontainer.add(doc)
                continue

            descriptor = getattr(obj.Inventory, name)
            value = getattr(obj.inventory, name)
            
            if descriptor.type == 'reference':
                
                # reference is owned
                if descriptor.owned:
                    doc = self._createViewForOwnedReference(
                        obj, record,
                        value, descriptor,
                        actor,
                        edithierarchy=edithierarchy
                        )
                # reference is NOT owned
                else:
                    doc = self._createViewForNotOwnedReference(
                        obj, record,
                        value, descriptor,
                        actor,
                        edithierarchy=edithierarchy
                        )
                    
                doc.addClass('referred-object')
                doc.collapsable = True
                container.add(doc)

            elif descriptor.type == 'referenceset':
                doc = self._createViewForReferenceSet(
                    obj, record,
                    descriptor,
                    actor=actor,
                    edithierarchy = edithierarchy,
                    )
                if doc:
                    doc.addClass('object-referenceset')
                    container.add(doc)

        return container


    def makeTitle(self, obj):
        record = self.orm(obj)
        if record.id:
            title = '%s #%s' % (record.getTableName().capitalize(), record.id)
        else:
            title = 'New %s' % (record.getTableName(),)
        return title


    def makeSequence(self, obj):
        s = ['properties']
        for descriptor in obj.Inventory.iterDescriptors():
            if descriptor.type in ['reference', 'referenceset']:
                s.append(descriptor.name)
            continue
        return s
    

    # reloadable view factories
    #
    # 1. reference
    #     not owned
    def _createReferenceSelectorForm(self, descriptor, record, referred_record, actor, ):
        form = lc.form()
        
        selector = self._createReferenceSelector(
            descriptor, record, referred_record, actor)
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
                refname = descriptor.name, 
                old_display_id = form.id, new_display_creator = 'displayReferenced'
                )
            ]

        doc = lc.document(title=descriptor.name.capitalize())
        doc.addClass('referred-object')
        doc.collapsable = True
        doc.add(form)

        editlink = lc.link(label='edit')
        editlink.onclick = select(element=doc).replaceBy(
            load(actor=actor, routine='createReferenceSelectorForm',
                 id = record.id, refname = descriptor.name)
            )
        editlink.hidden = True
        doc.add(editlink)

        # after form submitted, need to update the view to display view
        form.onsubmit += [
            select(element=editlink).show(),
            ]
        
        return doc


    def _createReferenceSelector(self, descriptor, record, referred_record, actor,):
        name = descriptor.name
        handler = '_createReferenceSelector_for_%s' % name
        if hasattr(self, handler):
            handler = getattr(self, handler)
            return handler(descriptor, record, referred_record, actor)
        
        if descriptor.isPolymorphic():
            self._checkPolymorphicReference(descriptor)

        selector = FormSelectorField(label='Choices:', name='refvalue')
        tip = getattr(descriptor, 'tip', None)
        if tip:
            selector.tip = tip

        if referred_record:
            value=self.orm.db.getUniqueIdentifierStr(referred_record)
        else:
            value=None
        entries = load(
            actor=actor, routine='getSelectorEntriesForReference',
            id = record.id,
            refname=name)
        selector.oncreate = select(element=selector).setAttr(entries=entries, value=value)
        return selector


    def _createViewForNotOwnedReference(
        self, obj, record,
        value, descriptor,
        actor,
        **drawingoptions
        ):
        edithierarchy = drawingoptions['edithierarchy']
        # if hierarchy is not to be edited, we should just return a readonly view
        if not edithierarchy:
            return self._createReadonlyViewForReference(descriptor, value, editlink=False)
        
        return self._createReferenceSelectorForm(
            descriptor, record,
            value and self.orm.object2record(value),
            actor
            )


    #     owned
    def _createViewForOwnedReference(
        self, obj, record,
        value, descriptor,
        actor, **drawingoptions
        ):
        edithierarchy = drawingoptions['edithierarchy']

        orm = self.orm
        inv = orm.inv(obj)
        
        if value is None:
            value = self._createDefaultValueForReference(descriptor)
            setattr(inv, descriptor.name, value)
            from dsaw.model.Inventory import restoreObjectFromInventory
            restoreObjectFromInventory(obj, inv)
            orm.save(obj)
            
        doc = self.drawers.getDrawer(value.__class__)(value, **drawingoptions)
        
        # polymorphic reference
        if descriptor.isPolymorphic() and edithierarchy:
            doc1 = self._createPolymorphicReferenceEditor(
                obj, record,
                descriptor, value,
                actor,
                )
            doc1.body.add(doc)
            return doc1
        # normal reference
        else:
            doc.title = "%s==>%s" % (descriptor.name, doc.title)
            return doc


    def _createPolymorphicReferenceEditor(
        self,
        obj, record, # the "container" object
        descriptor, referred_value, # the referred object
        actor, # actor name for the "container" object
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
            )
        newreferred_uid = load(
            actor = actor, routine='changeType',
            id = record.id,
            refname = name, typename=newtype)
        selector.onchange = select(id=body.id).replaceContent(
            load(actor=newactorname,
                 routine='edit', uid=newreferred_uid,
                 )
            )
        return doc


    # 2. reference set
    def _createViewForReferenceSet(
        self, obj, record,
        descriptor,
        actor,
        **drawingoptions
        ):
        edithierarchy = drawingoptions['edithierarchy']
        orm = self.orm
        
        name = descriptor.name

        set = getattr(obj.inventory, name)

        # if it is not allowed to edit the hierarchy, and the reference set is not
        # owned, we should just present a readonly view
        if not edithierarchy and not descriptor.owned:
            return self._createReadonlyViewForReferenceSet(descriptor, set, editlink=False)

        container = lc.document(Class='container', name=name)
        
        title = name.capitalize()
        doc = lc.document(title=title, collapsable=True); container.add(doc)
        
        for i, item in enumerate(set):
            subdoc = self._createSubDocumentForItemInReferenceSet(
                obj, record,
                descriptor,
                item,
                actor,
                **drawingoptions
                )
            doc.add(subdoc)
            continue

        #
        controls = doc.document(Class='controls')
        if edithierarchy:
            # append link
            append = load(
                actor=actor, routine='appendNewReferenceSetItem',
                id = record.id,
                refname = name,
                )
            appenddoc = select(element=controls).before(
                load(actor=actor, routine='createSubViewForAnItemInReferenceSet',
                     id = record.id, refname=name, refvalue=append)
                )
            appendlink = lc.link(
                label='Append a new item',
                onclick = appenddoc,
                Class = "append"
                )
            controls.add(appendlink)
        
        return container


    def _createSubDocumentForItemInReferenceSet(
        self, obj, record,
        descriptor,
        item, 
        actor,
        **drawingoptions
        ):
        """
        create the sub document that represents an item in the reference set

        This method is different from the methods _createViewForItemInReferenceSet...
        in that this method draws not only the item itself, but also the insert
        link that allow inserting item just before this item.
        """
        edithierarchy = drawingoptions['edithierarchy']

        #
        orm = self.orm

        # name of the reference set
        name = descriptor.name

        # the document to build
        subcontainer = lc.document(Class='container')

        # hidden field to save the unique identifier of this item
        hiddenuid = FormTextField(name='??', hidden=True); subcontainer.add(hiddenuid)
        uid_for_item = orm.db.getUniqueIdentifierStr(orm(item))
        hiddenuid.value = uid_for_item
        # action to get uid
        getuid = select(element=hiddenuid).getAttr('value')

        if edithierarchy:
            # insert link
            insert = load(
                actor=actor, routine='insertNewReferenceSetItem',
                id = record.id,
                refname = name,
                refvalue = getuid,
                position_relative_to_reference = 'before',
                )
            insertdoc = select(element=subcontainer).before(
                load(actor=actor, routine='createSubViewForAnItemInReferenceSet',
                     id = record.id, refname=name, refvalue=getuid)
                )
            insertlink = lc.link(
                label='Insert a new item',
                onclick = [insert, insertdoc],
                Class = "insert"
                )
            insertlinkcontainer = subcontainer.document(Class='controls')
            insertlinkcontainer.add(insertlink)

        # hack
        # for not-owned reference set, we need to have this edit link
        # constructed here and used later.
        replacedoc = select(element=subcontainer).replaceBy(
            load(actor=actor, routine='createSubViewForAnItemInReferenceSet',
                 id = record.id, refname=name, refvalue=getuid)
            )
        self.__editlink = lc.link(
            label = 'edit',
            onclick = replacedoc,
            Class = 'edit',
            )

        subdoc = self._createViewForItemInReferenceSet(
            obj, record,
            descriptor,
            item,
            actor,
            hiddenuid,
            **drawingoptions
            )
        subdoc.collapsable = True
        subdoc.addClass('object-referenceset-item')
        #
        subcontainer.add(subdoc)

        if edithierarchy:
            # delete link
            destroy = select(element=subcontainer).destroy()
            delete = load(
                actor=actor, routine='deleteReferenceSetItem',
                id = record.id,
                refname = name,
                refvalue = getuid,
                )
            deletelink = lc.link(
                label='Delete this item',
                onclick = [delete, destroy],
                Class = "delete",
                )
            subdoc.controlsdoc.add(deletelink)

        return subcontainer


    def _createViewForItemInReferenceSet(
        self, obj, record,
        descriptor,
        item, 
        actor,
        hiddenuid = None,
        **drawingoptions
        ):
        
        if descriptor.owned:
            doc = self._createViewForItemInOwnedReferenceSet(
                obj, record,
                descriptor,
                item,
                actor,
                hiddenuid = hiddenuid,
                **drawingoptions
                )
        else:
            doc = self._createViewForItemInNotOwnedReferenceSet(
                obj, record,
                descriptor,
                item, 
                actor,
                hiddenuid = hiddenuid,
                **drawingoptions
                )
        controls = doc.document(Class='controls')
        doc.controlsdoc = controls
        return doc


    def _createViewForItemInOwnedReferenceSet(
        self, obj, record,
        descriptor,
        item, 
        actor,
        hiddenuid = None,
        **drawingoptions
        ):
        edithierarchy = drawingoptions['edithierarchy']
        
        doc = self.drawers.getDrawer(item.__class__)(item, **drawingoptions)
        
        # polymorphic reference
        if descriptor.isPolymorphic() and edithierarchy:
            doc1 = self._createPolymorphicReferenceSetItemEditor(
                obj, record,
                descriptor,
                item,
                actor,
                hiddenuid = hiddenuid
                )
            doc1.body.add(doc)
            return doc1
        # normal reference
        else:
            name = descriptor.name
            doc.title = "Item: %s" % (doc.title,)
            return doc
        


    def _createPolymorphicReferenceSetItemEditor(
        self,
        obj, record, # the "container" object
        descriptor, item, # the refset descriptor, the item in the set
        actor, # actor name for the "container" object
        hiddenuid, # the hidden ui element that holds the value of uid of the item in the reference set
        ):

        self._checkPolymorphicReference(descriptor)

        # title
        name = descriptor.name
        title = 'Item'
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
            )
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
                 )
            ),
            ]
        return doc


    def _createViewForItemInNotOwnedReferenceSet(
        self, obj, record,
        descriptor,
        item,
        actor,
        hiddenuid = None,
        **drawingoptions
        ):
        
        name = descriptor.name
        title = "Item"
        doc = lc.document(title=title)

        body = doc.document(Class='container')
        form = self._createReferenceSetItemSelectorForm(
            obj, record,
            descriptor,
            item, 
            actor,
            hiddenuid = hiddenuid,
            )

        editlink = self.__editlink
        editlink.hidden = 1
        doc.add(editlink)
        
        # after form submitted, need to update the view to display view
        getuid = select(element=hiddenuid).getAttr('value')
        form.onsubmit += [
            select(element=body).replaceContent(
                load(actor=actor, routine='displayReferenced',
                     id = record.id, refname=name, refvalue=getuid)
                ),
            select(element=editlink).show()
            ]
        
        body.add(form)
        return doc
    

    def _createReferenceSetItemSelectorForm(
        self, obj, record,
        descriptor,
        item, 
        actor,
        hiddenuid = None
        ):
        
        form = lc.form()
        
        selector = self._createReferenceSetItemSelector(
            obj, record,
            descriptor,
            item,
            actor,
            )
        form.add(selector)

        orm = self.orm
        
        form.submitbutton(label='Change')
        
        getselectorvalue = select(element=selector).getAttr('value')
        form.onsubmit = [
            lc.select(element=form).submit(
                actor=actor, routine='changeReferenceSetItem',
                id = record.id,
                refname = descriptor.name,
                oldrefvalue = select(element=hiddenuid).getAttr('value'),
                ),
            lc.select(element=hiddenuid).setAttr(value=getselectorvalue),
            ]
        return form


    def _createReferenceSetItemSelector(
        self, obj, record,
        descriptor,
        item, 
        actor,
        ):
        
        name = descriptor.name
        targettype = descriptor.targettype
        if targettype is None:
            self._checkPolymorphicReference(descriptor)

        selector = FormSelectorField(label='Choices:', name='refvalue')
        tip = getattr(descriptor, 'tip', None)
        if tip:
            selector.tip = tip

        orm = self.orm
        value=self.orm.db.getUniqueIdentifierStr(orm(item))
        entries = load(
            actor=actor, routine='getSelectorEntriesForReference',
            id = record.id,
            refname=name,
            )
        selector.oncreate = select(element=selector).setAttr(entries=entries, value=value)
        return selector
    
    
    
    # helpers
    def _checkPolymorphicReference(self, descriptor):
        targettypes = descriptor.targettypes
        if not targettypes:
            raise RuntimeError, "need to know the possible types for the polymorphic reference. please decorate your reference with keyword 'targettypes'"
        return
    

    def _createDefaultValueForReference(self, descriptor):
        if descriptor.isPolymorphic():
            type = descriptor.targettypes[0]
        else:
            type = descriptor.targettype
        return self.orm.objectFactory(type)




import luban.content as lc
from luban.content import select, alert, load
from luban.content.FormSelectorField import FormSelectorField
from luban.content.FormTextField import FormTextField


# version
__id__ = "$Id$"

# End of file 
