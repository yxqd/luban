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


import luban.content as lc
from luban.content import select, load, alert


def panel(func):
    '''decorator to declare a member function to be one panel in the demo
    '''
    func.ispanel = True
    return func


def example(title=None, description=None, deps=None):
    '''decorator factory to generator decorator that declares
    a member function to be one example. Example is usually one level
    lower than panel. A panel can have 1+ examples.
    '''
    def _(func):
        func.title = title
        func.description = description
        func.deps = deps
        func.isexample = True
        return func
    return _


def quickpanel(title=None, description=None, examples=[]):
    def decorator(func):
        def _(self, director):
            # container = lc.document(title = title)
            container = lc.document()
            p = container.paragraph(text = description); p.Class = 'demo-description'
            accordion = lc.accordion(); container.add(accordion)
            accordion.Class = 'demo-panel'
            
            for i, example in enumerate(examples):
                doc = self.createExampleDocument(getattr(self, example), director)
                label = 'Demo %s: %s' % (i+1, doc.title)
                sec = accordion.section(label=label)
                for elem in doc.contents:
                    sec.add(elem)
                continue
            return container
        _.title = title
        panel(_)
        return _
    return decorator


from luban.components.Actor import Actor as base
class Actor(base):


    def default(self, director):
        title = 'luban demo: %s' % self.name
        p = lc.page(title = title)
        d = self.createDemoDocument(director)
        p.add(d)
        return p


    def createDemoDocument(self, director):
        container = lc.document()
        #
        doc = self._createSwitcher(director)
        doc.title = 'Demos'
        doc.collapsable = True
        doc.Class = 'demo-document'
        container.add(doc)
        #
        c = container.document(title='Introduction', collapsable=True)
        #
        d = lc.restructuredtextdocument(); c.add(d)
        d.text = self.introduction.splitlines()
        return container


    def createExampleDocument(self, method, director):
        assert method.isexample
        title = method.title
        description = method.description
        deps = method.deps
        if deps:
            for i, dep in enumerate(deps):
                # convert string to function
                if isinstance(dep, basestring):
                    deps[i] = getattr(self, dep)
                    
        return self._createExample(
            director=director, title=title, description=description,
            func=method, deps=deps)


    def _createSwitcher(self, director):
        import inspect

        # find routines that create panels
        routines = {}
        for k, v in self.__class__.__dict__.iteritems():
            # skip
            #  - private
            if k.startswith('_'): continue
            #  - non-method
            if not inspect.ismethod(v) and not inspect.isfunction(v): continue
            #  - signature
            sig = 'ispanel'
            if not hasattr(v, sig): continue
            if not getattr(v, sig): continue

            routines[k] = v
            continue

        # container
        container = lc.document()
        tabs = lc.tabs(); container.add(tabs)

        #
        if hasattr(self.__class__, 'demo_panels'):
            panels = self.__class__.demo_panels
        else:
            panels = routines.iterkeys()
        for i,k in enumerate(panels):
            # call method to get inner document
            method = getattr(self, k)
            # use inner document's title as tab's label
            label = method.title
            # create tab 
            tab = tabs.tab(label=label)
            # add the first document
            if i == 0:
                inner = method(director)
                tab.add(inner)
            else:
                tab.onselect = select(element=tab).replaceContent(
                    load(actor=self.name, routine=k)
                    )
            continue

        return container


    def _createExample(self, director=None, title=None, description=None, func=None, deps=None):
        doc = lc.document(title=title)
        doc.collapsable = True
        doc.Class = 'example-container'

        tabs = self._createTabsForDemoPanelAndCodeViewer(func, director, deps=deps)
        doc.add(tabs)
        
        if description:
            p = lc.restructuredtextdocument(); doc.add(p)
            p.Class = 'example-description'
            p.text = description
            p.text.append('')
            p.text.append('Please click on the "Code" tab to see how this demo is implemented.')

        return doc


    def _createTabsForDemoPanelAndCodeViewer(self, func, director, deps=None):
        '''create a "tabs" widget with one tab for demo, another tab for code

        func: the function that creates a docuemnt for the demo
        deps: the functions that "func" depends on. we need to show code for
          all of them to give a complet view. It is good that func and deps
          are in the same actor.
        '''
        tabs = lc.tabs()
        demotab = tabs.tab(label='Demo')
        demotab.Class = 'demo'
        funcname = func.im_func.func_name
        demotab.onselect = select(element=demotab).replaceContent(
            load(actor=self.name, routine=funcname))
        
        codetab = tabs.tab(label='Code')
        codetab.Class = 'code'

        demotab.add(func(director))

        lines = getSourceLines(func)
        blocks = [lines]

        if deps:
            for dep in deps:
                blocks.append( getSourceLines(dep) )

        codedoc = createCodeDoc(blocks)
        codetab.add(codedoc)
        # codetab.onselect = select(element=codetab).replaceContent(codedoc)
        return tabs
            
                
    pass # end of Actor



def createCodeDoc(blocks):
    lines = []
    for block in blocks:
        if not block: continue
        # add to lines
        lines += [l for i,l in block]
        lines += [''] * 2

    viewer = lc.codeviewer()
    viewer.syntax = 'python'
    viewer.text = '\n'.join(lines)
    return viewer
        
    hdoc = lc.htmldocument()
    hdoc.text = ['<pre>']+ lines + ['</pre>']
    return hdoc
        

def getSourceLines(f):
    import inspect
    lines, lineno = inspect.getsourcelines(f)

    if not len(lines): raise RuntimeError, "no source?"

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


# version
__id__ = "$Id$"

# End of file 
