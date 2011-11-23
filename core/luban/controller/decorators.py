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

    convention: when a function is called, all arguments with annotations should be called as keyword arguments
    """
    
    if not hasattr(func,'__annotations__'): return method
    
    # import inspect
    # argspec = inspect.getfullargspec(func)
    
    def convert( t, T ):
        return T(t)
        
    def wrapper(*args, **kwds):
        newkargs = []; errors = []
        for argname,T in func.__annotations__.items():
            t = kwds.get(argname)
            if t is None: continue
            try:
                t = T(t)
            except TypeError as e:
                errors.append((argname, e)); continue
            except ValueError as e:
                errors.append((argname, e)); continue
            kwds[argname] = t
            continue
        if errors:
            raise ArgumentConversionError(*errors)
        
        r = func(*args, **kwds)
        
        if 'return' in func.__annotations__:
            T = func.__annotations__['return']
            r = T(r)
            
        return r

    if onerror:
        def wrapper2(*args, **kwds):
            try: return wrapper(*args, **kwds)
            except ArgumentConversionError as e: return onerror(e.args, _func_=func)
        rt = wrapper2
    else:
        rt = wrapper

    # keep a reference the original non-decorated function, so we can get its
    # source, for example
    rt.not_decorated = func
    return rt


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

