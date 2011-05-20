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


def registerElementProvider(provider):
    from _accountant import element_providers as providers
    providers.append(provider)
    return providers


# elements

elementtypes = [
    'Accordion',
    'AppMenuBar',
    'Button',
    'CodeEditor',
    'CodeViewer',
    'Credential',
    'Dialog',
    'Dock',
    'Document',
    'Downloader',
    'File', 
    'Form',
    'Frame',
    'Grid',
    'HtmlDocument',
    'Image',
    'Link',
    'NewsTicker',
    'Page', # to be removed
    'Paragraph',
    'Plot2D',
    'Portlet',
    'ProgressBar',
    'ReStructuredTextDocument',
    'Splitter',
    'Tabs',
    'Toolbar',
    'TreeView',
    'Uploader',
    ]
for name in elementtypes:
    code = '''
def %s(*args, **kwds):
    from %s import %s
    return %s(*args, **kwds)
''' % (name.lower(), name, name, name)
    try:
        exec code
    except:
        raise RuntimeError, 'faield to execute %s' % code


# alias
rstdoc = restructuredtextdocument

# actions

#  for credentials
def createCredential(**kwds):
    '''createCredential(username=..., ticket=...)
    '''
    from SimpleAction import SimpleAction
    return SimpleAction('credentialCreation', **kwds)


def updateCredential(**kwds):
    '''updateCredential(username=..., ticket=...)
    '''
    from SimpleAction import SimpleAction
    return SimpleAction('credentialUpdate', **kwds)


def removeCredential():
    from SimpleAction import SimpleAction
    return SimpleAction('credentialRemoval')


#  for controller access
def load(*args, **kwds):
    from Loading import Loading
    return Loading(*args, **kwds)


#  selector
def select(id=None, element=None):
    '''select(id=None, element=None) -> selector
    
This method returns an action to select a UI element.
The argument for this method would be Either the unique id
of the element or the element itself.

Examples::

  >>> select(id="okbuttonid")
  >>> select(element=okbutton)

A selector can be used to further construct action on the
selected element. For example, the following code constructs
an action to destroy a document

  >>> select(element=doc).destroy()
  
'''
    if id is not None:
        from SelectByID import SelectByID
        return SelectByID(id=id)
    if element is not None:
        from SelectByElement import SelectByElement
        return SelectByElement(element=element)
    raise NotImplementedError, "id=%s, element=%s" % (id, element)


#  alert
def alert(message):
    '''alert(message) -> action to pop up an alert window with the given message

Examples::

  >>> alert("please input your password")
  
'''
    from SimpleAction import SimpleAction
    return SimpleAction(actionname='alert', message=message)


# version
__id__ = "$Id$"

# End of file 
