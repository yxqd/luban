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


def tag2xmltxt(tag):
    rep = Tag2Xml().render(tag)
    return '\n'.join(rep)


class Tag2Xml(object):

    def render(self, tag):
        self._indent = '  '
        self._indent_level = 0
        self._rep = []
        self.onTag(tag)
        return self._rep


    def onTag(self, tag):
        content = tag.content
        if isinstance(content, basestring):
            return self._onelinetag(tag)
        
        self._startTag(tag)

        self.indent()
        for item in tag.content:
            if isinstance(item, basestring):
                self.write(item)
            else:
                self.onTag(item)
            continue
        self.outdent()
        
        self._endTag(tag)
        return

    
    def _onelinetag(self, tag):
        self.write('<%s %s>%s</%s>' % (
            tag.name,
            ' '.join( ['%s="%s"' % (k,v) for k, v in tag.attrs.iteritems()] ),
            tag.content,
            tag.name
            ) )
        return


    def _startTag(self, tag):
        self.write('<%s %s>' % (
            tag.name,
            ' '.join( ['%s="%s"' % (k,v) for k, v in tag.attrs.iteritems()] )
            ) )
        return


    def _endTag(self, tag):
        self.write('</%s>' % tag.name)
        return


    def indent(self):
        self._indent_level +=1

    def outdent(self):
        self._indent_level -=1

    def write(self, line):
        self._rep.append(self._indent*self._indent_level+line)
        return



def test():
    from _xmlrep import Tag
    inventory = Tag('inventory', {'name': 'a'})

    component = Tag('component', {'name': 'SimpleHttpServer'})
    inventory.content.append(component)

    property = Tag('property', {'name': 'port'}, '8100')
    component.content.append(property)
    
    print '\n'.join(Tag2Xml().render(inventory))
    return


if __name__ == '__main__': test()

# version
__id__ = "$Id$"

# End of file 
