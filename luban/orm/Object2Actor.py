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
from luban.content import load, alert, select


from luban.components.AuthorizedActor import AuthorizedActor
from luban.components.FormProcessor import FormProcessorInterface


# convert a data object476 to an actor
# done by using dsaw.model orm to introspect a data object and build dsaw.model
# Inventory, and then convert the inventory to an actor inventory and an actor
class Object2Actor(object):


    def __call__(self, Object, ActorBase=AuthorizedActor, descriptors=None):
        from dsaw.model.visitors import getDataObjectClassInventory as getInventory
        Inventory = getInventory(Object)
        descriptors = descriptors or Inventory.getDescriptors()

        class _(FormProcessorInterface, ActorBase):


            def _setupORM(self, orm):
                """overload this method to setup orm to fit the special
                needs of the target data object, such as registering
                all data types referrred to by the target object.
                """
                orm.registerObjectType(Object)
                return


            def store(self, director):
                '''store user inputs into data base'''
                orm = director.clerk.orm
                
                obj = self._load(director)

                if obj is None:
                    obj = Object()
                    orm.save(obj)
                    record = orm(obj)
                    self.inventory.id = record.id
                else:
                    record = orm(obj)

                for descriptor in descriptors:
                    name = descriptor.name
                    type = descriptor.type
                    if type== 'array':
                        shape = descriptor.shape
                        if shape:
                            if isinstance(shape, int) or len(shape)==1:
                                inputs = self._getVectorInputsFromInventory(descriptor)
                            elif len(shape)==2:
                                inputs = self._getMatrixInputsFromInventory(descriptor)
                            else:
                                raise NotImplementedError

                            # retrieve the old value
                            value = getattr(obj.inventory, name)
                            # apply user inputs
                            for k, v in inputs.iteritems(): value[k] = v
                        else:
                            value = getattr(self.inventory, name)
                    elif type == 'reference':
                        # 
                        continue
                    elif type == 'referenceset':
                        # 
                        continue
                    else:
                        value = getattr(self.inventory, name)

                    # set new value
                    setattr(record, name, value)
                    continue

                orm.db.updateRecord(record)
                return


            def _castInventoryProperties(self):
                super(_,self)._castInventoryProperties()
                for descriptor in descriptors:
                    type = descriptor.type
                    if type != 'array': continue

                    name = descriptor.name
                    shape = descriptor.shape
                    
                    # no shape info, skip
                    if shape is None: continue

                    # with shape
                    if isinstance(shape, int) or len(shape) == 1: # array
                        arr = self._getVectorInputsFromInventory(descriptor)

                        # convert to a real array, right now it is still a dictionary
                        if isinstance(shape, int): length = shape
                        else: length = shape[0]
                        arr = [arr.get(i) or 0  for i in range(length)]

                        #
                        setattr(self.inventory, name, arr)
                        
                    elif len(shape)==2: # matrix
                        
                        m = self._getMatrixInputsFromInventory(descriptor)

                        # conver to a numpy matrix
                        import numpy
                        mm = numpy.zeros(shape)
                        for i in range(shape[0]):
                            for j in range(shape[1]):
                                mm[i,j] = m.get((i,j))
                            continue

                        #
                        setattr(self.inventory, name, mm)
                        
                    else:
                        raise NotImplementedError
                    
                    continue
                return
            

            def edit(self, director):
                obj = self._load(director)
                if obj is None:
                    orm = director.clerk.orm
                    obj = orm.objectFactory(Object)
                title = self.inventory.title
                if not title: title=None

                drawer = director.painter.paintObj.drawers.getDrawer(obj.__class__)
                drawer.title = title

                edithierarchy = self.inventory.edithierarchy
                return drawer(obj, edithierarchy=edithierarchy)


            def debug_edit(self, director):
                page = lc.page()
                page.add(self.edit(director))
                return page


            def createViewForReferenceSet(self, director):
                '''create a view for a referenceset
                id: id of this object
                refname: name of the referenceset
                '''
                obj = self._load(director)
                #
                orm = director.clerk.orm
                record = orm(obj)
                #
                refname = self.inventory.refname
                descriptor = getattr(obj.Inventory, refname)
                #
                drawers = director.painter.paintObj.drawers
                drawer = drawers.getDrawer(obj.__class__)
                return drawer.createViewForReferenceSet(
                    obj, 
                    descriptor
                    )


            def createSubViewForAnItemInReferenceSet(self, director):
                '''create a sub view for an item in a referenceset
                id: id of this object
                refname: name of the referenceset
                refvalue: unique identifier of the item of interest
                '''
                obj = self._load(director)
                #
                orm = director.clerk.orm
                record = orm(obj)
                #
                refname = self.inventory.refname
                descriptor = getattr(obj.Inventory, refname)
                #
                itemrecord = orm.db.fetchRecordUsingUniqueIdentifierStr(self.inventory.refvalue)
                item = orm.record2object.findObject(itemrecord)
                #
                drawers = director.painter.paintObj.drawers
                drawer = drawers.getDrawer(obj.__class__)
                return drawer.createSubViewForAnItemInReferenceSet(
                    obj, descriptor, item,)


            def createReferenceSelectorForm(self, director):
                '''create a form with a selector to select value for a reference

                id: id of this object
                refname: name of the reference
                '''
                obj = self._load(director)
                refname = self.inventory.refname
                descriptor = getattr(obj.Inventory, refname)
                
                drawer = director.painter.paintObj.drawers.getDrawer(obj.__class__)
                return drawer.createReferenceSelectorForm(obj, descriptor)


            def changeType(self, director):
                '''change the type of an object referenced by this object

                refname: name of the reference(set)
                typename: name of new type (actually table name)
                id: id of this object

                The following is only used for referenceset:
                refvalue: unique identifier of a record that is an item
                    in the referenceset
                '''
                refname = self.inventory.refname
                typename = self.inventory.typename
                
                obj = self._load(director)

                descriptor = getattr(obj.Inventory, refname)
                if not descriptor.owned:
                    raise RuntimeError

                #
                orm = director.clerk.orm

                # create a new instance
                newtype = orm.getObjectTypeFromTableName(typename)
                newinst = newtype()

                if descriptor.type == 'reference':
                    # replace
                    orm.setObjectAttribute(obj, refname, newinst)
                    # save
                    orm.save(obj)
                elif descriptor.type == 'referenceset':
                    # get the old item
                    uid = self.inventory.refvalue
                    olditem_record = orm.db.fetchRecordUsingUniqueIdentifierStr(uid)
                    olditem = orm.record2object.findObject(olditem_record)
                    # get the set
                    set = getattr(obj.inventory, refname)
                    # index
                    index = set.index(olditem)
                    # save the new object
                    orm.save(newinst)
                    # replace the old item
                    refset = getattr(orm(obj), refname)
                    refset.setElement(index=index, element=orm(newinst), db=orm.db)
                    # set[index] = newinst
                    # destroy the old item
                    orm.destroy(olditem)
                    
                return orm.db.getUniqueIdentifierStr(orm(newinst))



            def deleteItem(self, director):
                '''delete an item from a reference set

                id: id of this object
                refname: name of the referenceset
                refvalue: unique identifier of the item to delete
                '''
                orm = director.clerk.orm

                # the object
                obj = self._load(director)
                
                # get the item
                uid = self.inventory.refvalue
                record = orm.db.fetchRecordUsingUniqueIdentifierStr(uid)
                item = orm.record2object(record)

                # the refset
                set = getattr(obj.inventory, self.inventory.refname)

                # delete the item
                del set[set.index(item)]

                # save
                orm.save(obj)

                return


            def displayReferenced(self, director):
                '''display the view of the object referenced by this object

                id: id of the record that represents this object
                refname: the name of the reference(set)
                refvalue: in case of reference set, the unique id that represents the item to be displayed
                '''
                # load object
                obj = self._load(director)

                #
                orm = director.clerk.orm

                #
                descriptor = getattr(obj.Inventory, self.inventory.refname)

                # the referred
                if descriptor.type == 'reference':
                    referred = getattr(obj.inventory, self.inventory.refname)
                elif descriptor.type == 'referenceset':
                    referred_record = director.clerk.db.fetchRecordUsingUniqueIdentifierStr(
                        self.inventory.refvalue)
                    referred = orm.record2object.findObject(referred_record)

                # get the view
                routine = 'display'
                actor = director.painter.paintObj.actor_formatter(referred.__class__)
                return director.redirect(
                    actor=actor, routine=routine,
                    id=orm(referred).id, editlink=descriptor.owned,
                    include_credential=False
                    )


            def changeReference(self, director):
                '''change the object referenced by this object

                refname: name of the reference
                refvalue: unique identifier of the db record that represents the new data object to be referred to.
                id: id of the record that represents this object
                '''
                # this object
                obj = self._load(director)

                #
                orm = director.clerk.orm
                
                # load the new record to refer to
                refvalue = self.inventory.refvalue
                referred_record = director.clerk.db\
                                  .fetchRecordUsingUniqueIdentifierStr(refvalue)

                # convert to object
                orm = director.clerk.orm
                referred = orm.record2object(referred_record)

                # change reference
                refname = self.inventory.refname
                orm.setObjectAttribute(obj, refname, referred)

                # save
                orm.save(obj)

                #
                old_display_id = self.inventory.old_display_id
                new_display_creator = self.inventory.new_display_creator
                return select(id=old_display_id).replaceBy(
                    load(actor=self.name, routine=new_display_creator,
                         id = self.inventory.id, refname=refname)
                    )


            def changeReferenceSetItem(self, director):
                '''change an item in a reference set of this object

                id: id of the record that represents this object
                refname: name of the reference set
                oldrefvalue: unique identifier of the db record that represents the old item
                refvalue: unique identifier of the db record that represents the new item
                '''
                # this object
                obj = self._load(director)

                #
                orm = director.clerk.orm
                
                # load the new item
                refvalue = self.inventory.refvalue
                newitemrecord = orm.db.fetchRecordUsingUniqueIdentifierStr(refvalue)

                # load the old item
                oldrefvalue = self.inventory.oldrefvalue
                record = orm.db.fetchRecordUsingUniqueIdentifierStr(oldrefvalue)
                olditem = orm.record2object.findObject(record)

                # index of olditem
                refname = self.inventory.refname
                index = getattr(obj.inventory, refname).index(olditem)
                #
                refset = getattr(orm(obj), refname)
                refset.setElement(index=index, element=newitemrecord, db=orm.db)

                return


            def insertNewReferenceSetItem(self, director):
                '''insert a new item into a reference set of this object

                id: id of the record that represents this object
                refname: name of the reference set
                refvalue: unique identifier of the db record that represents the reference item
                position_relative_to_reference: position of the new item relative to the reference item. before or after
                '''
                # this object
                obj = self._load(director)

                #
                orm = director.clerk.orm
                
                # the reference record
                refrecord = orm.db.fetchRecordUsingUniqueIdentifierStr(self.inventory.refvalue)
                
                # create a new item
                refname = self.inventory.refname
                descriptor = getattr(obj.Inventory, refname)
                if descriptor.isPolymorphic():
                    elementtype = descriptor.targettypes[0]
                else:
                    elementtype = descriptor.targettype
                # the record of new element
                elementtable = orm(elementtype)
                elementrecord = elementtable()
                elementrecord.id = director.getGUID()
                orm.db.insertRow(elementrecord)

                # add to the refset
                record = orm(obj)
                refset = getattr(record, refname)
                kwds = {self.inventory.position_relative_to_reference: refrecord}
                refset.insert(elementrecord, db=orm.db, **kwds)

                return orm.db.getUniqueIdentifierStr(elementrecord)


            def appendNewReferenceSetItem(self, director):
                '''append a new item to a reference set of this object

                id: id of the record that represents this object
                refname: name of the reference set
                '''
                # this object
                obj = self._load(director)

                #
                orm = director.clerk.orm
                
                # create a new item
                refname = self.inventory.refname
                descriptor = getattr(obj.Inventory, refname)
                if descriptor.isPolymorphic():
                    elementtype = descriptor.targettypes[0]
                else:
                    elementtype = descriptor.targettype
                # the record of new element
                elementtable = orm(elementtype)
                elementrecord = elementtable()
                elementrecord.id = director.getGUID()
                orm.db.insertRow(elementrecord)

                # add to the refset
                record = orm(obj)
                refset = getattr(record, refname)
                refset.add(elementrecord, db=orm.db)

                return orm.db.getUniqueIdentifierStr(elementrecord)


            def deleteReferenceSetItem(self, director):
                '''delete an item in a reference set of this object

                id: id of the record that represents this object
                refname: name of the reference set
                refvalue: unique identifier of the db record to be deleted
                '''
                # this object
                obj = self._load(director)

                #
                orm = director.clerk.orm
                
                # load the item to delete
                refvalue = self.inventory.refvalue
                itemrecord = orm.db.fetchRecordUsingUniqueIdentifierStr(refvalue)

                # db record of obj
                record = orm(obj)
                # the reference set
                refname = self.inventory.refname
                refset = getattr(record, refname)
                # remove the item from the refset
                refset.delete(itemrecord, orm.db)

                # destroy the record
                descriptor = getattr(obj.Inventory, refname)
                if descriptor.owned:
                    orm.destroy(orm.record2object.findObject(itemrecord))
                return


            def getSelectorEntriesForReference(self, director):
                # overload this method to return a list of 2-tuples
                # each tuple is (value, label) to be used as entries for a selector
                # widget to select an instance to be referred to by the
                # data object of interest using name "refname"
                #
                # refname: name of reference
                #
                # id: id of the data object. it is not used in this implementation. 
                # but the overloaded method may use this to fine tune the entries.
                #
                I = Object.Inventory
                refname = self.inventory.refname
                descriptor = getattr(I, refname)

                # if descriptor.isPolymorphic(): raise NotImplementedError
                
                type = descriptor.targettype
                actor = director.painter.paintObj.actor_formatter(type)

                records = director.redirect(
                    actor=actor, routine='_getRecords')
                # no records, return nothing
                if not records:
                    return
                
                db = director.clerk.db
                orm = director.clerk.orm
                uidstr = db.getUniqueIdentifierStr
                def description(r):
                    try: return getattr(r, 'short_description')
                    except AttributeError: pass
                    obj = orm.record2object(r)
                    if '__str__' in dir(obj):
                        return str(obj)
                    return uidstr(r)
                return [ (uidstr(r), description(r)) for r in records]


            def _getRecords(self, director, filter=None):
                orm = director.clerk.orm
                Table = orm(Object)
                q = director.clerk.db.query(Table)
                
                if filter: q = q.filter(filter)

                return q.all()


            def getActorName(self, director):
                typename = self.inventory.typename
                orm = director.clerk.orm
                self._setupORM(orm)
                type = orm.getObjectTypeFromTableName(typename)
                return director.painter.paintObj.actor_formatter(type)
                

            def display(self, director):
                'a simpley display of target data object'

                obj = self._load(director)
                
                title = self.inventory.title
                if not title: title=None

                editlink = self.inventory.editlink

                drawer = director.painter.paintObj.drawers.getDrawer(obj.__class__)
                drawer.title = title
                
                return drawer(obj, readonly=True, editlink=editlink)


            def display_noedit(self, director):
                self.inventory.editlink = False
                return self.display(director)
            display_noedit.open_to_public = True
            

            def displayProperties(self, director):
                'display of properties of target data object'
                obj = self._load(director)
                drawer = director.painter.paintObj.drawers.getDrawer(obj.__class__)
                editlink = self.inventory.editlink
                return drawer.createPropertiesView(obj, editlink=editlink)


            def editProperties(self, director):
                obj = self._load(director)
                drawer = director.painter.paintObj.drawers.getDrawer(obj.__class__)
                return drawer.createPropertiesForm(obj)


            def _getVectorInputsFromInventory(self, descriptor):
                '''retrieve inputs about the given vector from inventory'''
                name = descriptor.name
                converter = descriptor.elementconverter
                shape = descriptor.shape
                if isinstance(shape, int):
                    length = shape
                else:
                    length = shape[0]

                ret = {}
                for i in range(length):
                    n = '%s_%s' % (name, i)
                    if n in self.inventory.__dict__:
                        v = getattr(self.inventory, n)
                        v = converter(v)
                        ret[i] = v
                    continue
                return ret
                        
                    
            def _getMatrixInputsFromInventory(self, descriptor):
                '''retrieve inputs about the given matrix from inventory'''
                name = descriptor.name
                converter = descriptor.elementconverter
                nrows, ncols = descriptor.shape
                ret = {}
                for i in range(nrows):
                    for j in range(ncols):
                        n = '%s_%s_%s' % (name, i, j)
                        if n in self.inventory.__dict__:
                            v = getattr(self.inventory, n)
                            v = converter(v)
                            ret[(i,j)] = v
                        continue
                    continue
                return ret


            def _load(self, director):
                self._setupORM(director.clerk.orm)
                id = self.inventory.id
                uid = self.inventory.uid
                if id:
                    ret = self._loadByID(id, director)
                elif uid:
                    ret = self._loadByUID(uid, director)
                else:
                    return
                ret.inventory = director.clerk.orm.inv(ret)
                return ret
            

            def _loadByUID(self, uid, director):
                orm = director.clerk.orm
                record = orm.db.fetchRecordUsingUniqueIdentifierStr(uid)
                return orm.record2object(record)

            
            def _loadByID(self, id, director):
                'load data object'
                orm = director.clerk.orm
                return orm.load(Object, id)


            pass

        _.Inventory = self._createComponentInventory(Inventory, ActorBase)
        return _

    # create the inventory class for the actor
    def _createComponentInventory(self, Inventory, ActorBase):
        descriptors = self._createDescriptors(Inventory.getDescriptors())
        class _(FormProcessorInterface.Inventory, ActorBase.Inventory):

            for name, descriptor in descriptors.iteritems():
                exec '%s=descriptor' % name
                continue
            # clean up
            try:
                del name, descriptor
            except:
                pass

            # id of the record for this object
            id = luban.inventory.str(name='id')
            # uid of the record of this object
            uid = luban.inventory.str(name='uid')

            # title of document
            title = luban.inventory.str('title')

            # style of the view
            view_style = luban.inventory.str('view_style', default='')

            # type name of referred object
            typename = luban.inventory.str('typename')
            # name of the reference
            refname = luban.inventory.str('refname')
            # value of the reference represented by a unique string (tablename###id)
            refvalue = luban.inventory.str('refvalue')
            #
            oldrefvalue = luban.inventory.str('oldrefvalue')
            # position of new element relative to the reference element: before, after
            position_relative_to_reference = luban.inventory.str('position_relative_to_reference')

            # whether the display has a "edit" link
            import pyre.inventory
            editlink = pyre.inventory.bool('editlink', default=True)

            # whether it is allowed to change the hierarchy structure of the object
            edithierarchy = luban.inventory.bool('edithierarchy', default=True)

        return _


    # the descriptors in the actor inventory class
    def _createDescriptors(self, model_descriptors):
        r = {}
        for descriptor in model_descriptors:
            name = descriptor.name
            d = self._createDescriptor(descriptor)
            if d:
                r[name] = d
            continue
        return r


    def _createDescriptor(self, descriptor):
        type = descriptor.type
        handler = '_on%s' % type.capitalize()
        if handler in self.__class__.__dict__:
            handler = getattr(self, handler)
            return handler(descriptor)
        return self._onSimpleDescriptor(descriptor)


    def _onReference(self, descriptor):
        return


    def _onReferenceset(self, descriptor):
        return


    def _onArray(self, descriptor):
        shape = descriptor.shape
        if shape is None:
            return self._onSimpleDescriptor(descriptor)
        if isinstance(shape, int) or len(shape) == 1:
            return self._onVector(descriptor)
        return self._onMatrix(descriptor)


    def _onVector(self, descriptor):
        name = descriptor.name
        type = descriptor.elementtype
        return luban.inventory.propertySet(
            name = name,
            pattern = re.compile('%s_.*'%name),
            type = type,
            validator = descriptor.elementvalidator,
            )


    def _onMatrix(self, descriptor):
        name = descriptor.name
        type = descriptor.elementtype
        return luban.inventory.propertySet(
            name = name,
            pattern = re.compile('%s_.*_.*'%name),
            type = type,
            validator = descriptor.elementvalidator,
            )


    def _onSimpleDescriptor(self, descriptor):
        name = descriptor.name
        type = descriptor.type
        validator = descriptor.validator
        default = descriptor.default
        return getattr(luban.inventory, type)(name, validator=validator, default=default)


    def _onBool(self, descriptor):
        name = descriptor.name
        type = descriptor.type
        validator = descriptor.validator
        return getattr(luban.inventory, type)(name, validator=validator)


import re
import luban.inventory


object2actor = Object2Actor()


# version
__id__ = "$Id$"

# End of file 
