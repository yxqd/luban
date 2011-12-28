# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from luban import py_major_ver


class Tag(object):

    def script(self, src=None, contents=None, **kwds):
        if src: kwds['src'] = src
        s = self.tag('script', **kwds)
        s.contents = contents
        return s


    def stylesheet(self, url=None, media='all', rel='stylesheet', **kwds):
        kwds.update( {
            'media': media,
            'rel': rel,
            } )
        t = self.tag('style', **kwds)
        t.contents = ['@import url('+url+');']
        return t


    def tag(self, type, **kwds):
        tag = Tag(type, **kwds)
        tag.root = self.root
        self.append(tag)
        return tag


    def append(self, item): self.contents.append(item)

    def identify(self, visitor): return visitor.onTag(self)
    
    def __init__(self, type, **kwds):
        self.type = type
        self.kwds = kwds
        self.contents = []
        self.root = self
        return

    def __str__(self):
        return '[%s (%s): %s]' % (
            self.type,
            ','.join(['%s=%s' % (k,v) for k,v in self.kwds.items()]),
            (self.contents or '') and \
            '\n'.join([str(item) for item in self.contents]),
            )

    
class HtmlDocument(Tag):

    def __init__(self, **kwds):

        Tag.__init__(self, 'html', **kwds)
        
        self.head = Head(); self.head.root = self
        self.body = Body(); self.body.root = self

        self.contents += [
            self.head,
            self.body,
            ]
        return

    def title(self, **kwds):
        return self.head.title(**kwds)

    def base(self, **kwds):
        return self.head.base(**kwds)

    def script(self, **kwds):
        return self.head.script(**kwds)

    def stylesheet(self, **kwds):
        return self.head.stylesheet(**kwds)



# a container for partial html document
# not real
class PartialHtmlDocument(Tag):

    def __init__(self):
        Tag.__init__(self, 'div')
        return
    

class Head(Tag):

    def base(self, url=None, **kwds):
        return self.tag('base', href=url, **kwds)

    def title(self, text=None, **kwds):
        t = self.tag('title', **kwds)
        t.contents = [text]
        return t

    def __init__(self):
        Tag.__init__(self, 'head')
        return


class Body(Tag):
    def __init__(self):
        Tag.__init__(self, 'body')
        return
    

# version
__id__ = "$Id$"

# End of file 
