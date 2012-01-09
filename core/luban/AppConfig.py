# -*- python -*-
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

class Option:

    def __init__(self, name, doc, example):
        self.name = name
        self.doc = doc
        self.example = example
        self.value = None
        return
    


class AppConfig:

    def __init__(self):
        self.options = {}
        return
    

    def register(self, name, doc, example):
        opt = Option(name, doc, example)
        self.options[name] = opt
        return


    def __getattr__(self, name):
        return self._retrieveValue(name)


    def _retrieveValue(self, name):
        try:
            import luban_app_config
        except ImportError:
            raise RuntimeError("luban app configuration not found")
        # check option definition
        opt = self.options.get(name)
        if opt is None:
            msg = "Unknown option %r. Before using an option, developer should register the option." % name
            raise RuntimeError(msg)
        
        try:
            v = getattr(luban_app_config, name)
        except AttributeError:
            import os; modfile = os.path.abspath(luban_app_config.__file__)
            msg = "Missing option...\n\nPlease assign value to option %r in %s\n\nWhat it is:\n  %s\n\nExample\n  %s = %r\n" % (
                name, modfile, opt.doc, name, opt.example)
            raise RuntimeError(msg)
        return toobj(v)


class RecurseStruct:

    def __init__(self, d):
        for k, v in d.items():
            if isinstance(v, dict):
                v = RecurseStruct(v)
            self.__dict__[k] = v
            continue
        return
    
def toobj(v):
    if isinstance (v, dict):
        return RecurseStruct(v)
    return v
    

def test1():
    d = {
        'a': {'b': 1},
        "c": 3
        }
    o = RecurseStruct(d)
    assert o.a.b == 1
    assert o.c == 3
    return

def main():
    test1()
    return


if __name__ == '__main__': main()


# End of file 

