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


def typeconversion(func):
    
    if not hasattr(func,'__annotations__'): return method
    
    import inspect
    argspec = inspect.getfullargspec(func)
    
    def convert( t, T ):
        return T(t)
        
    def wrapper(*args, **kwds):
        
        if len(argspec.args) != len(args):
            raise TypeError( "%s() takes exactly %s positional argument (%s given)"
                           %(func.__name__,len(argspec.args),len(args)) )

        newargs = []
        for argname,t in zip(argspec.args, args):
            if argname in func.__annotations__:
                T = func.__annotations__[argname]
                t = T(t)
            newargs.append(t)
            continue

        r = func(*newargs, **kwds)
        
        if 'return' in func.__annotations__:
            T = func.__annotations__['return']
            r = T(r)
            
        return r

    return wrapper


def bool(s):
    if s.lower() in ['0', 'false', 'off']: return False
    return True

def int(s):
    import builtins
    return builtins.int(s)


# End of file 

