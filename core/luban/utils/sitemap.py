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

class Url:

    properties = [
        'location',
        'lastmod',
        'changefreq',
        'priority',
        ]

    def __init__(self, **kwds):
        self.base = None
        for k, v in kwds.items():
            setattr(self, k, v)
        return

    
    def getFragment(self):
        """for luban, we really only care about the fragment for, for example,
        building the static snapshots for crawlers"""
        location = self.location
        if not location: return ''
        index = location.find('#!')
        if index == -1:
            raise RuntimeError("Don't know how to get fragment from %r" % location)
        return location[index+2:]


    def getFragmentHash(self):
        return hash(self.getFragment())


    def __iter__(self):
        base = self.base
        for k in self.properties:
            v = getattr(self, k, None)
            if k == 'location':
                if base:
                    v = base + '/' + v
                k = 'loc'
            yield k,v
            continue
        return


    def __str__(self):
        return 'Url(' + ','.join('%s=%r' % (k,v) for k,v in self) + ')'

    __repr__ = __str__



def hash(s):
    import hashlib
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class Renderer:

    def render(self, base, urls):
        self.base = base
        self._rep = []; self._indentation = 0
        self._header()
        self._urlset(urls)
        return '\n'.join(self._rep)

    
    def _urlset(self, urls):
        self._write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
        self._indent()
        for url in urls:
            self._url(url)
            continue
        self._outdent()
        self._write('</urlset>')
        return

    def _write(self, line):
        self._rep.append(' '* self._indentation + line)
        return
    def _indent(self): self._indentation += 1
    def _outdent(self): self._indentation -= 1


    def _url(self, url):
        self._write('<url>')
        self._indent()
        url.base = self.base
        d = dict(url)
        for k,v in d.items():
            if v is None: continue
            self._write('<%s>%s</%s>' % (k, v, k))
            continue
        '''
        '<loc>' + url + '</loc>'
        <lastmod>2008-01-01</lastmod> 
        <changefreq>weekly</changefreq> 
        <priority>0.8</priority> 
        '''
        self._outdent()
        self._write('</url>')
        return


    def _header(self):
        self._write('<?xml version="1.0" encoding="UTF-8"?>')
        return



def create(base, urls, output):
    """
    create(
        "http://example.com", 
        [Url(location="home"), Url(location="about")],
        'sitemap.xml'
        )
    """
    r = Renderer()
    text = r.render(base, urls)
    open(output, 'w').write(text)
    return


# End of file 
