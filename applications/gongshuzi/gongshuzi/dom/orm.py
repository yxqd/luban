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


class ORM(object):


    def __init__(self):
        super(ORM, self).__init__()
        self.n2t = {} # table name to table
        self.o2t = {} # object type to table
        self.t2o = {} # table to object type
        return


    def iterTables(self):
        return self.t2o.iterkeys()


    def registerObject(self, Object, Table=None):
        if not Table:
            Table = AttributeContainer2Table(Object)
        self.o2t[Object] = Table
        self.t2o[Table] = Object
        self.n2t[Table.name] = Table
        return


    def getTable(self, Object):
        return self.o2t[Object]


    def getObject(self, Table):
        if Table in self.t2o:
            return self.t2o[Table]
        return self.getObject(self.n2t[Table.name])


    def record2object(self, record, recursive=False, db=None):

        debug.log('record %s, name %s, id=%s' % (record, record.name, record.id))
                  
        from dsaw.db._reference import reference
        from dsaw.db._referenceset import referenceset
        from luban.content.descriptors import Reference, ReferenceSet
        
        Obj = self.getObject(record.__class__)
        obj = Obj()
        objdescriptors = obj.getDescriptors()
        objdescriptornames = [d.name for d in objdescriptors]

        for descriptor in objdescriptors:
            attrname = descriptor.name
            colname = attrname2colname(attrname, Obj)
            
            if isinstance(descriptor, Reference):
                if not recursive: continue
                value = getattr(record, colname)
                debug.log('reference: attrname %s, colname %s, value %s' % (attrname, colname, value))
                if not value: continue
                value = value.dereference(db)
                if not value: continue
                value = self.record2object(value, recursive=1, db=db)

            elif isinstance(descriptor, ReferenceSet):
                if not recursive: continue
                value = getattr(record, colname)
                value = value.dereference(db)
                value = [
                    self.record2object(record1, recursive=1, db=db)
                    for name, record1 in value
                    ]

            elif descriptor.type == 'list':
                value = getattr(record, colname) or ''
                value = value.split('\n')
                
            else:
                value = record.getColumnValue(colname)
                
            debug.log('attribute name %s, value %s' % (attrname, value))

            obj.setAttribute(attrname, value)
            continue
        return obj



def AttributeContainer2Table(AttributeContainer): 
    '''convert ui element to dsaw.db Table'''
    
    from OwnedObject import OwnedObject as base
    class Table(base):

        import dsaw.db
        
        for descriptor in AttributeContainer.getDescriptors():
            name = descriptor.name

            colname = attrname2colname(name, AttributeContainer)
            
            default = descriptor.default
            type = descriptor.type
            colvarname = colname.replace(' ', '_').replace('-', '_')

            # debug.log('processing descriptor: name=%s, default=%s, type=%s, colvarname=%s, colname=%s' % (
            #    name, default, type, colvarname, colname) )
            
            if type == 'str':
                code = '%s = dsaw.db.varchar(name="%s", length=128, default="%s")' % (
                    colvarname, colname, default or '')
                
            elif type == 'bool':
                code = '%s = dsaw.db.boolean(name="%s", default=%s)' % (
                    colvarname, colname, default or False)
                
            elif type == 'int':
                code = '%s = dsaw.db.integer(name="%s", default=%s)' % (
                    colvarname, colname, default or 0)
                
            elif type == 'lists':
                # skip for now
                continue
            
            elif type == 'dict':
                # skip for now
                continue
            
            elif type == 'list':
                code = '%s = dsaw.db.varchar(name="%s", length=1024, default="%s")' % (
                    colvarname, colname, default or '')

            elif type == 'reference':
                code = '%s = dsaw.db.versatileReference(name="%s")' % (
                    colvarname, colname)

            elif type == 'referenceset':
                code = '%s = dsaw.db.referenceSet(name="%s")' % (
                    colvarname, colname)
                
            else:
                raise NotImplementedError, type

            #debug.log('executing: %s' % code)
            exec code in locals()
            continue

        # id is special. we want to differentiate the id of the record in the db table
        # and the real id of the ui element
        luban_elment_id = dsaw.db.varchar(name='luban_elment_id', length=128)
        
        # pyre db tables need a member "name" to denote the name of the table
        name = AttributeContainer.__name__.lower() + 's'

        pass # end of Table

    return Table



uielementid_name = 'luban_elment_id'



def colname2attrname(colname, objtype):
    if colname == _nameVariableName(objtype):
        return 'name'
    if colname == 'luban_elment_id':
        return 'id'
    if colname == 'id':
        raise RuntimeError, "'id' is not translatable to attribute"
    return colname


def attrname2colname(attrname, objtype):
    if attrname == 'name':
        return _nameVariableName(objtype)
    if attrname == 'id':
        return 'luban_elment_id'
    return attrname


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# this is a hack
# the dsaw.db.Table uses 'name' variable. this is
# very inconvinient if your object has a "name" property
# here we have to create a map for "name" to "<tabletype>name"
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def _nameVariableName(objtype):
    return objtype.__name__.lower() + 'name'


import journal
debug = journal.debug('gongshuzi.dom.orm')


# version
__id__ = "$Id$"

# End of file 
