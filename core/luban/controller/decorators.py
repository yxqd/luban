# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def public(f):
    f.public = True
    return f


def typeconversion(onerror=None):
    return lambda func: _typeconversion(func, onerror)


class ArgumentConversionError(Exception): pass
def _typeconversion(func, onerror=None):
    """decorator to convert a function to convert arguments
    to appropriate types.

    func: the function to decorate
    onerror: error handler in case argument conversion fail
    """
    
    if not hasattr(func,'__annotations__'): return method
    
    import inspect
    argspec = inspect.getfullargspec(func)
    
    def convert( t, T ):
        return T(t)
        
    def wrapper(*args, **kwds):
        
        if len(argspec.args) != len(args):
            raise TypeError( "%s() takes exactly %s positional argument (%s given)"
                           %(func.__name__,len(argspec.args),len(args)) )

        newargs = []; errors = []
        for argname,t in zip(argspec.args, args):
            if argname in func.__annotations__:
                T = func.__annotations__[argname]
                try:
                    t = T(t)
                except TypeError as e:
                    errors.append((argname, e)); continue
                except ValueError as e:
                    errors.append((argname, e)); continue
                continue
            newargs.append(t)
            continue
        if errors:
            raise ArgumentConversionError(*errors)
        
        r = func(*newargs, **kwds)
        
        if 'return' in func.__annotations__:
            T = func.__annotations__['return']
            r = T(r)
            
        return r

    if onerror:
        def wrapper2(*args, **kwds):
            try: return wrapper(*args, **kwds)
            except ArgumentConversionError as e: return onerror(e.args)
        return wrapper2

    return wrapper


# type conversion handlers
def bool(s):
    if s.lower() in ['0', 'false', 'off']: return False
    return True

def int(s):
    import builtins
    try:
        return builtins.int(s)
    except ValueError:
        raise ValueError("%r is not an integer" % s)
    raise RuntimeError("should not reach here")


# End of file 

