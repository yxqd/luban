#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 


import urllib


class CGIParser(object):


    def parse(self, registry, arg, source):
        log = self.log
        import pyre.parsing.locators
        self.locator = pyre.parsing.locators.simple(source)

        for field in arg.split(self.argsep):
            if log:
                log('parsing %s' % field)
            tokens = field.split(self.assignment)
            key = tokens[0]
            value = self.assignment.join(tokens[1:])
            if not key: continue
            try:
                key, value = tokens
            except ValueError:
                if self.strict:
                    raise ValueError, "bad query field {%r}" % field
                elif self.keepBlanks:
                    key = field
                    value = ''
                else:
                    key = tokens[0]
                    value = self.assignment.join(tokens[1:])
            
            if not key: continue
            if log:
                log('process kv pair: %s, %s' % (key, value))
            try:
                self._processArgument(key, value, registry)
            except:
                raise RuntimeError, 'Error parsing cgi arguments: key=%s, arg=%s, source=%s' % (key, arg, source)

        self.locator = None

        return


    def __init__(self, strict=False, keepBlanks=False, log=None):
        self.argsep = '&'
        self.fieldsep = '.'
        self.assignment = '='

        self.strict = strict
        self.keepBlanks = keepBlanks
        self.log = log

        # options tracer
        self.locator = None

        return


    def _processArgument(self, key, value, registry):

        fields = key.split(self.fieldsep)

        children = []
        for field in fields:
            if field[0] == '[' and field[-1] == ']':
                candidates = field[1:-1].split(',')
            else:
                candidates = [field]
            children.append(candidates)

        self._storeValue(registry, children, value)

        return


    def _storeValue(self, node, children, value):
        if len(children) == 1:
            for key in children[0]:
                key = key.strip()
                node.setProperty(key, urllib.unquote_plus(value), self.locator)
            return

        for key in children[0]:
            self._storeValue(node.getNode(key), children[1:], value)

        return


# version
__id__ = "$Id: CGIParser.py,v 1.3 2008-08-21 17:44:56 pyre Exp $"

#  End of file 
