# -*- python -*-
# Jiao Lin
# Caltech


# minimal journal interface implemented with logging

class Channel(object):

    severity = None

    def __init__(self, name):
        self.name = name
        self._activated = False
        return

    def log(self, msg):
        if not self._activated:
            return
        import logging
        logger = getattr(logging, self.severity)
        return logger("%s - %s" % (self.name, msg))


    def _set_status(self, status):
        self.activate()
        return True
    def _get_status(self):
        return self._activated
    active = property(_get_status, _set_status)


    def activate(self):
        import logging
        logging.basicConfig(level=logging.DEBUG)
        self._activated = True
        return


class Debug(Channel):
    
    severity = 'debug'

    cache = {}


def debug(name):
    cache = Debug.cache
    if name not in cache:
        cache[name] = Debug(name)
    return cache[name]


# End of File
