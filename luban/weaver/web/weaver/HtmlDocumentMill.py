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

# works on a HtmlDocument instance and generates html code

class HtmlDocumentMill:

    def __init__(self, indentation = None, max_indentation=20):
        if not indentation:
            indentation = ' '
        self.indentation = indentation
        self.max_indentation = max_indentation
        return
    

    def render(self, document):
        self.texts = ['<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">']
        self.indent_level = 0
        document.identify(self)
        return self.texts


    def write(self, text):
        indent = self.indent_level*self.indentation
        if len(indent) >= self.max_indentation:
            newlen = len(indent) % self.max_indentation
            indent = indent[:newlen]
        self.texts.append(indent+text)
        return


    def indent(self): self.indent_level+=1
    def outdent(self): self.indent_level-=1


    def onTag(self, tag):
        if tag.type in self.special_types:
            self.handle(tag)
            return
        
        self.write(self.beginTag(tag))

        contents = tag.contents
        self.indent()
        for item in contents:
            if isinstance(item, basestring):
                self.texts.append(item)
            else:
                if not item:
                    raise RuntimeError, 'item is None in tag %s' % tag
                item.identify(self)
            continue
        self.outdent()
        
        self.write(self.endTag(tag))
        return

    special_types = [
        'textarea',
        ]


    def handle(self, tag):
        type = tag.type
        handler = 'on'+type
        handler = getattr(self, handler)
        return handler(tag)


    def ontextarea(self, tag):
        begin = self.beginTag(tag)

        contents = tag.contents
        text = '\n'.join(contents)
        
        end = self.endTag(tag)

        self.write(begin+text+end)
        return


    def beginTag(self, tag):
        kwds = tag.kwds
        for k,v in kwds.iteritems():
            if k.lower() != k:
                kwds[k.lower()] = v
                del kwds[k]
            
        type = tag.type
        try:
            assignments = kwdsstr(**kwds)
        except:
            raise RuntimeError, 'failed to convert %s to a string for tag %s' % (
                kwds, tag)

        text = '<'+type+' '+assignments + '>'
        #if tag.contents:
        #    text = '<'+type+' '+assignments + '>'
        #else:
        #    text = '<'+type+' '+assignments
        return text
    

    def endTag(self, tag):
        contents = tag.contents
        #if not contents:
        #    text = '/>'
        #else:
        #    type = tag.type
        #    text = '</' + type + '>'
        type = tag.type
        text = '</' + type + '>'

        return text


def kwdsstr(**kwds):
    return ' '.join( [k+'="'+str(v)+'"' for k,v in kwds.iteritems()] )

    
# version
__id__ = "$Id$"

# End of file 
