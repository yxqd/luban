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


class SubclassDefinitionContextBuilder:

    @classmethod
    def __prepare__(cls, name, bases, **kwds):
        d = super().__prepare__(name, bases, **kwds)
        context = cls._collectContextFromBases(bases)
        d.update(context)
        return d

    
    @classmethod
    def _collectContextFromBases(cls, bases):
        """collect context for preparation of the target class of this meta class
        from bases of the target class.
        """
        context = dict()
        
        # only check the farthest one in the immediate parent classes
        base = bases[-1]
        
        method = "__get_subclass_preparation_context__"
        # first check that parent class itself
        if hasattr(base, method):
            c = getattr(base, method)()
            context.update(c)
        else:
            # if not found, check all bases of that parent class
            for base1 in base.__mro__:
                if hasattr(base1, method):
                    c = getattr(base1, method)()
                    context.update(c)
                    break # assume all implementation of __get_subclass_preparation_context__ to call super correctly
                continue
                
        return context


# End of file 
