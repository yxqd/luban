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


"""
actor base class for one demo panel.

see aokuang.core.actors.loading.SimpleValue for an example of
how this is used.
"""


import luban


from luban.controller.Actor import Actor as base
class Actor(base):

    expose = True
    title = None
    description = None


    def createInterface(self, **kwds):
        title = self.title or self.name
        doc = luban.e.document(title = title)
        doc.append(self._createDemoAndCodeViewTabs())
        
        p = doc.restructuredtextdocument()
        p.Class = 'demo-description'
        p.text = '\n'.join(self.description)
        p.text+= '\n\n'
        p.text+= 'Please click on the "Code" tab to see how this demo is implemented.'
        return doc


    def _createDemoAndCodeViewTabs(self, **kwds):
        func = self.createDemoPanel
        deps = []
        dontcount = ['createDemoPanel', 'createInterface', 'perform']
        for name in dir(self.__class__):
            #
            if name in dontcount: continue
            if name.startswith('_'): continue
            #
            candidate = getattr(self, name)
            # not a class
            if isinstance(candidate, type):
                continue
            # make sure it is callable
            if hasattr(candidate, '__call__'):
                deps.append(candidate)
            continue
        return self._createTabsForDemoPanelAndCodeViewer(func, deps)


    def createDemoPanel(self, **kwds):
        """subclass should override this to 
        create the panel of the demo case this actor is about
        """
        raise NotImplementedError


    def _createTabsForDemoPanelAndCodeViewer(self, func, deps=None):
        '''create a "tabs" widget with one tab for demo, another tab for code

        func: the function that creates a document for the demo
        deps: the functions that "func" depends on. we need to show code for
          all of them to give a complet view. It is good that func and deps
          are in the same actor.
        '''
        tabs = luban.e.tabs()
        demotab = tabs.tab(label='Demo')
        from luban import uuid
        demotab.id = uuid.uuid()
        demotab.Class = 'demo'
        funcname = func.__func__.__name__
        demotab.onselect = luban.a.select(element=demotab).replaceContent(
            newcontent=luban.a.load(actor=self.name, routine=funcname))
        
        codetab = tabs.tab(label='Code')
        codetab.Class = 'code'

        demotab.append(func())

        lines = getSourceLines(func)
        blocks = [lines]

        if deps:
            for dep in deps:
                blocks.append( getSourceLines(dep) )

        codedoc = createCodeDoc(blocks)
        codetab.append(codedoc)
        # codetab.onselect = select(element=codetab).replaceContent(codedoc)
        return tabs
            
                
def createCodeDoc(blocks):
    lines = []
    for block in blocks:
        if not block: continue
        # add to lines
        lines += [l.rstrip() for i,l in block]
        lines += ['    '] * 2

    text = '\n'.join(['::', '']+ [' '+ l for l in lines])
    hdoc = luban.e.restructuredtextdocument(text=text)
    return hdoc


def getSourceLines(f):
    import inspect
    lines, lineno = inspect.getsourcelines(f)

    if not len(lines): raise RuntimeError("no source?")

    if lines[0].strip()[0] == '@':
        # there is a decorator
        for i, l in enumerate(lines[1:]):
            if l.strip().startswith('def'):
                index = i + 1
                break
            continue
        lines = lines[index:]

    # 
    r = []
    for line in lines:
        l = lineno, line
        r.append(l)
        lineno += 1
        continue

    return r


# End of file 
