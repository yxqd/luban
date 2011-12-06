# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# the signature of the class attribute to define unique name of a luban type
# NOTE: name is case-insensitive. all names will be converted to lower case as
#       the key to the name:type store
UNIQUE_TYPE_NAME_SIGNAUTURE = '__unique_type_name__'


class TypeRegistryCurator:

    def __new__(cls, name, bases, attributes, **kwds):
        # the created class
        created = super().__new__(cls, name, bases, attributes, **kwds)
        registry.register(created)
        return created


# registry of real luban types (no base classes, no templates)
class Registry:


    def __init__(self):
        self._store = {}
        self._cls2name = {}
        return


    def names(self):
        return self._store.keys()


    def types(self):
        return self._store.values()


    def get(self, name):
        return self._store.get(name)

    
    def __iter__(self):
        return iter(self._store)


    def register(self, cls):
        # no templates
        if 'template' in cls.__dict__ and cls.template:
            return
        # if it has "abstract" decoration, skip
        if 'abstract' in cls.__dict__ and cls.abstract:
            return
            
        name = self._getUniqueName(cls)
        self._register(name, cls)
        return


    def _register(self, name, cls):
        #
        # note that lower case name is also registered
        
        # already registered, skip
        if cls in self._store.values():
            return
        
        import luban
        if not luban.extension_allow_override:
            
            # find if the name or its lower case already registered
            registered = None
            if name in self._store:
                registered = self._store[name]
            if name.lower() in self._store:
                registered = self._store[name.lower()]

            if registered:
                # conflict
                m = "type of the same name already registered. name: %s, new element: %s, existing element: %s" % (name, cls, registered)
                from .exceptions import TypeConflict
                raise TypeConflict(m)

        # register
        self._store[name] = self._store[name.lower()] = cls
        self._cls2name[cls] = name
        return


    def _getUniqueName(self, target):
        # get unique name to identify the element type
        sig  = UNIQUE_TYPE_NAME_SIGNAUTURE
        if sig in target.__dict__:
            name = target.__dict__[sig]
        else:
            name = target.__name__.lower()
            # set it to the class
            setattr(target, sig, name)
        return name


registry = Registry()


# End of file 
