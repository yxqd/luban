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

import journal
debug = journal.debug('luban.testing.selenium.selector')

from ..SelectorBase import Selector as SelectorBase

class Selector(SelectorBase):


    def select(self, key):
        h = '_selectFrom%s' % self._type.capitalize()
        h = getattr(self, h, None)
        if h is None: raise NotImplementedError
        return h(key)
    

    def getAttribute(self, name):
        sel = self.selenium
        
        e = self._getMainElementSelector()
        sel.waitForElementPresent(e)
        
        s = self._getAttributeSelector(name)
        return sel.get_attribute(s)


    def click(self):
        clickable = self._getClickable()
        debug.log("clickable for %s: %s" % (self, clickable))
        
        s = self.selenium
        s.waitForElementPresent(clickable)
        return s.click(clickable)


    def type(self, text):
        inputcontainer = self._getInputContainer()
        debug.log("input widget for %s: %s" % (self, inputcontainer))

        sele = self.selenium
        sele.waitForElementPresent(inputcontainer)
        return sele.type(inputcontainer, text)


    def getText(self):
        textcontainer = self._getTextContainer()
        debug.log("text container for %s: %s" % (self, textcontainer))

        s = self.selenium
        s.waitForElementPresent(textcontainer)
        return s.get_text(textcontainer)


    def getValue(self):
        inputcontainer = self._getInputContainer()
        debug.log("input widget for %s: %s" % (self, inputcontainer))

        sele = self.selenium
        sele.waitForElementPresent(inputcontainer)
        return sele.get_value(inputcontainer)


    def expand(self):
        e = self._getMainElementSelector()
        ctrl = '%s/%s' % (e, "/div[1]/table/tbody/tr/td[1]/a[1]")
        sele = self.selenium
        sele.waitForElementPresent(ctrl)
        return sele.click(ctrl)


    #
    def _selectFromFormradiobox(self, key):
        e = self._getMainElementSelector()
        input = "%s/table/tbody/tr/td[1]/div/input[@value='%s']" % (e, key)
        debug.log("radio button for %s, key %s: %s" % (
                self, key, input))
        
        sele = self.selenium
        sele.waitForElementPresent(input)
        return sele.click(input)


    def _selectFromFormselectorfield(self, key):
        inputcontainer = self._getInputContainer()
        debug.log("input widget for %s: %s" % (self, inputcontainer))

        sele = self.selenium
        sele.waitForElementPresent(inputcontainer)
        return sele.select(inputcontainer, key)


    #
    def _getMainElementSelector(self):
        return selectorResolver.main_element(self)

    
    def _getClickable(self):
        return getClickable(self)


    def _getTextContainer(self):
        return getTextContainer(self)


    def _getInputContainer(self):
        return getInputContainer(self)


    def _getAttributeSelector(self, name):
        return getAttributeSelector(self, name)



class SelectorResolver(object):

    def __call__(self, selector):
        type = selector._type
        h = 'on%s' % type.capitalize()
        h = getattr(self, h, None)
        if not h:
            raise NotImplementedError, type
        return h(selector)


    def main_element(self, selector):
        'selector of the main element'
        tag = self.type2tag(selector._type)
        kwds = {}
        if selector._id:
            kwds['id'] = selector._id
        if selector.props.has_key('name'):
            kwds['luban-element-name'] = selector.props['name']
            
        return self.simple_selector(tag, **kwds)


    def simple_selector(self, tag, **attrs):
        'simple selector that involves no hierarchy traversing'
        l = []
        tag = "//" + tag; l.append(tag)
        for k, v in attrs.iteritems():
            l.append("[@%s='%s']" % (k, v))
            continue
        return ''.join(l)


    def type2tag(self, type):
        'convert luban element type to html tag'
        return  type2tag[type]
    
type2tag = {
    'paragraph': 'p',
    'document': 'div',
    'link': 'a',
    'button': 'div',
    'form': 'form',
    'formtextfield': 'div',
    'formsubmitbutton': 'div',
    'formselectorfield': 'div',
    'formtextarea': 'div',
    'formradiobox': 'div',
    }
selectorResolver = SelectorResolver()


class GetClickable(SelectorResolver):

    def onButton(self, selector):
        text = selector.props.get('label')
        if text:
            return 'link=%s' % text
        b = self.main_element(selector)
        return '%s/a' % b

    
    def onLink(self, selector):
        text = selector.props.get('label')
        if text:
            return 'link=%s' % text
        return self.main_element(selector)


    def onFormsubmitbutton(self, selector):
        label = selector.props.get('label')
        if label:
            return "//input[@type='submit'][@value='%s']" % label
        b = self.main_element(selector)
        return "%s/input[@type='submit']" % b

getClickable = GetClickable()



class GetTextContainer(SelectorResolver):

    def onParagraph(self, selector):
        p = self.main_element(selector)
        return p

getTextContainer = GetTextContainer()



class GetInputContainer(SelectorResolver):

    def onFormtextfield(self, selector):
        return self._onformfield(selector, 'input')
    
    def onFormselectorfield(self, selector):
        return self._onformfield(selector, 'select')

    def onFormtextarea(self, selector):
        return self._onformfield(selector, 'textarea')
    
    def _onformfield(self, selector, tag):
        name = selector.props.get('name')
        if name:
            return "//input[@name='%s']" % name
        e = self.main_element(selector)
        return "%s/table/tbody/tr/td/%s" % (e, tag)
    
getInputContainer = GetInputContainer()



class GetAttributeSelector(SelectorResolver):

    def __call__(self, selector, name):
        type = selector._type
        h = 'on%s_%s' % (type, name)
        h = getattr(self, h, None)
        h = self._default
        return h(selector, name)


    def _default(self, selector, name):
        s = self.main_element(selector)
        return '%s@%s' % (s, name)

getAttributeSelector = GetAttributeSelector()



# version
__id__ = "$Id$"

# End of file 

