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


from luban import py_major_ver


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
if py_major_ver == 2:
    import __builtin__ as builtins
elif py_major_ver == 3:
    import builtins
    
def bool(s):
    if s.lower() in ['0', 'false', 'off']: return False
    return True

def int(s):
    try:
        return builtins.int(s)
    except ValueError:
        raise ValueError("%r is not an integer" % s)
    raise RuntimeError("should not reach here")


def str(s):
    if not isinstance(s, builtins.str):
        raise TypeError("needs a string")
    return s


def positive(c):
    if c <= 0:
        raise ValueError("should be positive")
    return c


def notemptystr(s):
    if not isinstance(s, builtins.str): raise TypeError("%s is not a string" % s)
    if not s: raise ValueError("empty string")
    return s


def email(s):
    if not email_pattern.match(s):
        raise ValueError("invalid email address")
    return s
import re
email_pattern = re.compile('[a-zA-Z0-9+_\-\.]+@[0-9a-zA-Z][.-0-9a-zA-Z]*.[a-zA-Z]+')


positiveInteger = lambda x: positive(int(x))


# End of file 

