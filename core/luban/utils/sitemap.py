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
        url = self.base + '/' + url
        self._write('<loc>' + url + '</loc>')
        '''
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
    """create("http://example.com", ["home", "about", "consulting"], 'sitemap.xml')
    """
    r = Renderer()
    text = r.render(base, urls)
    open(output, 'w').write(text)
    return


# End of file 
