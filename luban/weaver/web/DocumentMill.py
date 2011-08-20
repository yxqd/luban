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


# renders a ui document into a html document instance and a javascript document
# instance

class DocumentMill(object):

    """This mill creates html or json output from a luban ui model.

    luban ui model is represented by a hierarchy of luban ui objects.
    
    The renderer first 
    """

    prerenderer = None # overload prerenderer of a DocumentMill instance to provide custom behavior


    def __init__(self, librarian=None, javascriptsbase = 'javascripts', imagesbase='images'):
        if librarian is None: raise RuntimeError
        self.librarian = librarian

        self.javascriptsbase = javascriptsbase
        self.imagesbase = imagesbase

        from luban.weaver.Object2Dict import Object2Dict
        self._obj2dict = Object2Dict()

        # XXX: need to think about this pre renderer more
        self._prerenderer = PreRenderer()
        return

    
    def render(
        self, document,
        html_target=None, javascript_target=None,
        ):

        if html_target is None:
            from .content.HtmlDocument import HtmlDocument
            html_target = HtmlDocument()
        self.html_target= html_target
        
        if javascript_target is None:
            from .content.JavaScriptDocument import JavaScriptDocument
            javascript_target = JavaScriptDocument()
        self.javascript_target = javascript_target

        # cover the bases
        # check if the target root is a full html document
        # if yes, we need to add a few things to head
        htmlroot = html_target.root
        from .content.HtmlDocument import HtmlDocument
        self._fullhtmltarget = isinstance(htmlroot, HtmlDocument)
            
        if self._fullhtmltarget:
            librarian = self.librarian
            for category in ['base', 'application']:
                for stylesheet in librarian.getStyleSheets(widget=category):
                    htmlroot.stylesheet(url=stylesheet)
                for jslib in librarian.getJavaScriptLibs(widget=category):
                    javascript_target.include(script=jslib)

            # the body wrapper div
            html_target.body.tag('div', id='body-wrapper')

            # image base
            self.javascript_target.main += [
                'luban.configuration.javascripts_base = "%s";' % self.javascriptsbase,
                'luban.configuration.images_base = "%s";' % self.imagesbase,
                'luban.configuration.icons_base = "%s/icons";' % self.imagesbase,
                ]

            #
            for widget in librarian.iterWidgets():
                if not widget: continue
                stylesheets = librarian.getStyleSheets(widget=widget)
                jslibs = librarian.getJavaScriptLibs(widget=widget)
                d = {'javascripts': jslibs, 'stylesheets': stylesheets}
                d = jsonEncode(d)
                self.javascript_target.main += ["luban.widgets.implementationRegistry.%s = %s;" % (widget, d) ]
                continue

        docasdict = self._render(document)
        docinjson = jsonEncode(docasdict)
        
        if self._fullhtmltarget:
            self.javascript_target.main.append(
                'luban.docmill.render(%s);' % docinjson)
            return html_target, javascript_target
        
        return docinjson


    def _render(self, obj):
        obj = self._prerenderer.render(obj)
        return self._obj2dict.render(obj)



from luban.ui.elements.AttributeContainer import AttributeContainer
class PreRenderer(object):

    def __init__(self):
        import journal
        self._debug = journal.debug('luban.weaver.web.prerenderer')
        return
    

    def render(self, element):
        self._debug.log('working on %s' % (element,))
        try: return element.identify(self)
        except AttributeError :
            import traceback
            self._debug.log('"identify" failed on %s. use default. Exception is: %s' % (
                element, traceback.format_exc(), ))
            return self.default(element)
        except Exception:
            import traceback
            msg = 'error rendering %r(%r): %s' % (
                element, element.__class__, traceback.format_exc())
            self._debug.log(msg)
            return element
        raise RuntimeError
    

    def default(self, element):
        descriptors = element.iterDescriptors()
        for descriptor in descriptors:
            type = descriptor.type
            name = descriptor.name
            value = descriptor.__get__(element, element.__class__)
            value = self._convertValue(value)
            if type == 'referenceset' and value:
                descriptor.__set__(element, value)
                    
            elif type == 'reference' and value:
                descriptor.__set__(element, value)
                
            continue
        
        return element


    def _convertValue(self, value):
        if isinstance(value, dict): return self._ondict(value)
        if isinstance(value, list) or isinstance(value, tuple): return self._onlist(value)
        if isinstance(value, AttributeContainer): return self.render(value)
        return value


    def _ondict(self, value):
        for k, v in value.items():
            v = self._convertValue(v)
            value[k] = v
            continue
        return value
    def _onlist(self, value):
        if isinstance(value, tuple):
            value = list(value)
            
        for item in value:
            if not item: continue
            newitem = self._convertValue(item)
            # replace
            value[value.index(item)] = newitem
        return value

    
from ._utils import jsonEncode

from luban import journal
debug = journal.debug('luban.weaver.web')


# version
__id__ = "$Id$"

# End of file 
