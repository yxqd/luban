#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2009  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import wx
from . import widgets


class Weaver(object):

    def __init__(self, action_compiler=None):
        if action_compiler is None:
            from .ActionCompiler import ActionCompiler
            action_compiler = ActionCompiler()
        self.action_compiler = action_compiler
        return


    def _iconpath(self, icon):
        import os
        return os.path.join('../content/images/icons', icon)


    def render(self, document, container=None, appglobals=None):
        info.log( "start rendering" )

        self._globals = appglobals
        self.action_compiler.setGlobals(appglobals)
        
        widget = self._render(document, container_widget=container)
        
        info.log( "rendering done." )
        return widget


    def compile(self, action, this=None):
        return self.action_compiler.compile(action, this=this)


    # handlers

    def onAccordion(self, accordion):
        parent = self._container_widget

        wxaccordion = widgets.accordion(parent)
        
        maxwidth = 0
        maxheight = 0
        for child in accordion.contents:

            foldpanel, wxsection = self._render(child, container_widget=wxaccordion)

            width = wxsection.GetSize()[0]
            if width > maxwidth:
                maxwidth = width
            height = wxsection.GetSize()[1]
            if height > maxheight:
                maxheight = height

            wxaccordion.append(wxsection, foldpanel)

        # callbacks
        onchange = accordion.onchange
        def _(evt):
            # 
            selectedpanelid = evt.GetTag().id

            # clicks is the list of clicks happened to the accordion
            clicks = wxaccordion.clicks
            clicks.append(selectedpanelid)

            # old section could be None if this click is the first click ever happen
            if len(clicks) == 1: oldsection = ''
            else: oldsection = clicks[-2]

            # new section
            newsection = clicks[-1]

            # prepare data for this event
            data = {
                'oldsection': oldsection,
                'newsection': newsection,
                }
            wxaccordion.setEventData('changed', data)

            #
            self.compile(onchange)

            # need to pass this event on
            evt.Skip()
            return
        
        wxaccordion.bindcallbacks({'click':_})

        id = accordion.id
        if id: self._registerWidget(id, wxaccordion)

        # set the accordion's size as slightly larger than the largest section
        wxaccordion.SetSize(wx.Size(maxwidth + 20, \
                            maxheight + 30*len(accordion.contents)))

        return wxaccordion


    def onAccordionSection(self, section):
        parent = self._container_widget
        foldpanel = parent.AddFoldPanel(section.label, collapsed=True)
        foldpanel.id = section.id
        section.title=None
        self._container_widget = foldpanel
        foldpanel.root = parent.root
        doc = self.onDocument(section)
        return (foldpanel, doc)


    def onFrame(self, frame):
        wxapp = self._container_widget
        
        id = frame.id
        
        title = frame.title
        wxframe = widgets.mainFrame(title=title)

        if id:
            self._registerWidget(id, wxframe)
            # empty id means frame as well
            self._registerWidget('', wxframe)
        
        # temp hack
        # directly add a menubar
        #wxmenubar = widgets.menubar(wxframe)
        #wxframe.SetMenuBar( wxmenubar )
        #wxframe.menubar = wxmenubar

        # attach to wxapp
        wxapp.frame = wxframe

        # sizer
        wxsizer = widgets.sizer(orientation='vertical')
        wxframe.SetSizer(wxsizer)
        
        # contents
        contents = frame.contents
        for item in contents:
            wxwidget = self._render(item, container_widget=wxframe)
            if not wxsizer.wasAlreadyAdded(wxwidget):
                wxsizer.add(wxwidget, 1)
            continue

        #wxframe.SetSizerAndFit(wxsizer)
        #wxframe.SetSizer(wxsizer)
        wxsizer.Fit(wxframe)
        
        return wxframe


    def onMatterBuilder(self, matterBuilder):
        parent = self._container_widget
        
        id = matterBuilder.id
        wxmatterBuilder = widgets.matterBuilder(parent)

        if id:
            self._registerWidget(id, wxmatterBuilder)
            # empty id means frame as well
            self._registerWidget('', wxmatterBuilder)

        # sizer
        wxsizer = widgets.sizer(orientation='vertical')
        wxmatterBuilder.SetSizer(wxsizer)
        
        # contents
        contents = matterBuilder.contents
        for item in contents:
            wxwidget = self._render(item, container_widget=wxmatterBuilder)
            if not wxsizer.wasAlreadyAdded(wxwidget):
                wxsizer.add(wxwidget, 1)
            continue

        #wxframe.SetSizerAndFit(wxsizer)
        #wxframe.SetSizer(wxsizer)
        wxsizer.Fit(wxmatterBuilder)
        
        return wxmatterBuilder


    def onDocument(self, document):
        debug.log( 'working on %s' % document)
        parent = self._container_widget
        
        debug.log('parent=%s' % parent)
        wxpanel = widgets.panel(parent)
        wxsizer = widgets.sizer(orientation='vertical')
        wxpanel.SetSizer(wxsizer)
        
        wxelements = []
        
        id = document.id
        if id: self._registerWidget(id, wxpanel)

        # title
        title = document.title
        if title:
            wxtext = widgets.text( wxpanel, title)
            font1 = wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL, True, 'Comic Sans MS')
            wxtext.SetFont(font1)
            wxsizer.add(wxtext, border = 8, flag = wx.BOTTOM)
            wxpanel.titlewidget = wxtext
        
        contents = document.contents
        for item in contents:
            wxelement = self._render(item, container_widget=wxpanel)
            wxelements.append(wxelement)
            continue

        # add elements to sizer
        if wxelements:
            for e in wxelements:
                if not wxsizer.wasAlreadyAdded(e):
                    wxsizer.add(e, border = 5, flag = wx.TOP | wx.BOTTOM)
            
        #we need to remember how deep we are in the sizer hierarchy
        #if we don't remember, all sizers will try to fit
        #to the parent window. In wx, sizer is not a window,
        #it is not a widget.
        #wxpanel.SetSizer(wxsizer)
        wxsizer.Fit(wxpanel)
                
        return wxpanel
    
    def onHtmlDocument(self, htmlDocument):
        debug.log( 'working on %s' % htmlDocument)
        parent = self._container_widget
        
        debug.log('parent=%s' % parent)
        wxhtmlpanel = widgets.htmlpanel(parent)
#        wxsizer = widgets.sizer(orientation='vertical')
#        wxpanel.SetSizer(wxsizer)
        
        wxelements = []
        
        id = wxhtmlpanel.id
        if id: self._registerWidget(id, wxhtmlpanel)
        
        text = htmlDocument.text[0]
        wxhtmlpanel.SetPage(text)
        
#        contents = htmlDocument.contents
#        for item in contents:
#            wxelement = self._render(item, container_widget=wxhtmlpanel)
#            wxelements.append(wxelement)
#            continue

        # add elements to sizer
#        if wxelements:
#            for e in wxelements:
#                if not wxsizer.wasAlreadyAdded(e):
#                    wxsizer.add(e, border = 5, flag = wx.TOP | wx.BOTTOM)
            
        #we need to remember how deep we are in the sizer hierarchy
        #if we don't remember, all sizers will try to fit
        #to the parent window. In wx, sizer is not a window,
        #it is not a widget.
        #wxpanel.SetSizer(wxsizer)
#        wxsizer.Fit(wxpanel)
                
        return wxhtmlpanel


    def onSplitter(self, splitter):
        parent = self._container_widget
        children = splitter.contents
        
        orientation = splitter.orientation

        wxpanel = widgets.panel(parent)
        wxentiresizer = widgets.sizer(orientation=orientation)

        for item in children:
            wxchild = self._render(item, container_widget=wxpanel)
            # size is the ratio of the sizes of the sections.
            # a size of 3 means that section is 3 times as big as the others
            size = item.size
            if not (size):
                size = 1
            else:
                size = int(size)
                
            #wxsizer = widgets.sizer()
            #wxsizer.add(wxchild, -1)
            #wxentiresizer.add(wxsizer, size)
            wxentiresizer.add(wxchild, size)
            continue

        #wxpanel.SetSizerAndFit(wxentiresizer)
        wxpanel.SetSizer(wxentiresizer)
        wxentiresizer.Fit(wxpanel)

        id = splitter.id
        if id: self._registerWidget(id, wxpanel)

        return wxpanel


    def onSplitSection(self, section):
        section.title = None
        return self.onDocument(section)


    def onTabs(self, tabs):
        parent = self._container_widget
        wxtabs = widgets.notebook( parent, size=(1300,1300) ) 

        for child in tabs.contents:
            label, doc = self._render(child, container_widget=wxtabs)
            wxtabs.add(label, doc)

        id = tabs.id
        if id: self._registerWidget(id, wxtabs)

        parent.GetSizer().add(wxtabs, flag=wx.EXPAND)
        return wxtabs


    def onTab(self, tab):
        # need to return both tab.label and the document
        tab.title = None
        return (tab.label, self.onDocument(tab))


    def onParagraph(self, paragraph):
        parent = self._container_widget
        width, height = parent.GetSizeTuple()
        
        text = paragraph.text
        txt = '\n'.join(text)
        wxtext = widgets.text( self._container_widget, txt)
        #wxtext.Wrap(int(width*0.95))

        #
        id = paragraph.id
        if id: self._registerWidget(id, wxtext)
        
        return wxtext
    

    def onPortlet(self, portlet):
        parent = self._container_widget
        mainframe = parent.root

        title = portlet.title

        # also create a panel
        wxportlet = widgets.panel(parent)
        wxelements = [] # for sizer
        wxsizer = widgets.sizer(orientation='vertical')
        wxportlet.SetSizer(wxsizer)
        
        # add title to it
        wxtext = widgets.text(wxportlet, title)
        wxelements.append(wxtext)
        
        #
        for child in portlet.contents:
            wxportletitem = self._render(child, container_widget=wxportlet)
            wxportletiemsizer = widgets.sizer()
            wxportletiemsizer.add(wxportletitem, -1)
            wxelements.append(wxportletiemsizer)
            continue

        # add elements to sizer
        if wxelements:
            for e in wxelements:
                if not wxsizer.wasAlreadyAdded(e):
                    wxsizer.add(e)

        #wxsizer.Layout()
        # wxportlet.SetAutoLayout(1)
        # wxportlet.SetSizer(wxsizer)
        wxsizer.Fit(wxportlet)

        #
        id = portlet.id
        if id: self._registerWidget(id, wxportlet)
        
        return wxportlet


    def onPortletItem(self, portletitem):
        parent = self._container_widget

        tip = portletitem.tip or ''
        label = portletitem.label

        # callback
        onclick = portletitem.onclick
        def _(evt): self.compile(onclick)

        # also create a button
        button = widgets.button(parent, label=label, callbacks={'click': _})
        
        return button


    def onAppMenuBar(self, menubar):
        parent = self._container_widget
        mainframe = parent.root

        wxmenubar = widgets.menubar(mainframe)
        mainframe.SetMenuBar( wxmenubar )
        for child in menubar.contents:
            wxrendered = self._render(child, container_widget=wxmenubar)
            mainframe.GetMenuBar().Append(wxrendered, child.label)

        id = menubar.id
        if id: self._registerWidget(id, wxmenubar)

        return wxmenubar


    def onAppMenu(self, menu):
        parent = self._container_widget
        label = menu.label

        wxmenu = widgets.menu(parent, label)

        # callback
        #onclick = menu.onclick
        #def _(evt): self.compile(onclick)

        for child in menu.contents:
            wxrendered = self._render(child, container_widget=wxmenu)
            try:
                wxmenu.append(wxrendered)
            except:
                wxmenu.appendMenu(wxrendered)

        id = menu.id
        if id: self._registerWidget(id, wxmenu)

        return wxmenu


    def onAppMenuItem(self, menuitem):
        parent = self._container_widget
        mainframe = parent.root

        # callback
        onclick = menuitem.onclick
        def _(evt): self.compile(onclick)

        wxmenuitem = widgets.menuitem(parent, text=menuitem.label, 
                          tip=menuitem.tip, callbacks={'click':_})

        id = menuitem.id
        if id: self._registerWidget(id, wxmenuitem)

        return wxmenuitem

    def onDialog(self, dialog):
        debug.log( 'working on %s' % dialog )
        parent = self._container_widget

        id = dialog.id
        title = dialog.title or ''

        wxdialog= widgets.dialog(parent)
        if id: self._registerWidget(id, wxdialog)
        wxsizer = widgets.sizer(orientation='vertical')
        wxdialog.SetSizer(wxsizer)

        #
        wxelements = []
        
        # title
        wxtext = widgets.text(wxdialog, title)
        font1 = wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL, True, 'Comic Sans MS')
        wxtext.SetFont(font1)
        wxelements.append(wxtext)

        # contents
        contents = dialog.contents
        from luban.content.FormSubmitButton import FormSubmitButton
        for item in contents:
            #can eventually do this for dialogs with submit buttons
#            if isinstance(item, FormSubmitButton):
#                item.onclick = form.onsubmit
#                item.form = form
            wxelement = self._render(item, container_widget=wxdialog)
            wxelements.append(wxelement)
            continue

        # add to sizer
        if wxelements:
            for e in wxelements:
                if not wxsizer.wasAlreadyAdded(e):
                    wxsizer.add(e)
        
        #wxform.SetSizerAndFit(wxsizer)
        #wxform.SetSizer(wxsizer)
        # wxform.SetAutoLayout(1)
        wxsizer.Fit(wxdialog)
        return wxdialog

    def onForm(self, form):
        debug.log( 'working on %s' % form )
        parent = self._container_widget

        id = form.id
        title = form.title or ''
        onsubmit = form.onsubmit

        wxform = widgets.form(parent)
        if id: self._registerWidget(id, wxform)
        wxsizer = widgets.sizer(orientation='vertical')
        wxform.SetSizer(wxsizer)

        #
        wxelements = []
        
        # title
        wxtext = widgets.text(wxform, title)
        font1 = wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL, True, 'Comic Sans MS')
        wxtext.SetFont(font1)
        wxelements.append(wxtext)

        # contents
        contents = form.contents
        from luban.content.FormSubmitButton import FormSubmitButton
        for item in contents:
            if isinstance(item, FormSubmitButton):
                item.onclick = form.onsubmit
                item.form = form
            wxelement = self._render(item, container_widget=wxform)
            wxelements.append(wxelement)
            continue

        # add to sizer
        if wxelements:
            for e in wxelements:
                if not wxsizer.wasAlreadyAdded(e):
                    wxsizer.add(e)
        
        #wxform.SetSizerAndFit(wxsizer)
        #wxform.SetSizer(wxsizer)
        # wxform.SetAutoLayout(1)
        wxsizer.Fit(wxform)
        return wxform


    def onFormTextField(self, field):
        debug.log( 'working on %s' % field )
        name = field.name
        value = field.value
        
        parent = self._container_widget

        wxpanel = self.onFormField(field)
        wxsizer = wxpanel.GetSizer()
        wxelements = wxpanel.elements

        # the text box
        wxtextField = widgets.textfield(wxpanel, value=value, name=name)
        formparent = wxtextField.findFormParent()
        formparent.addInputWidget(wxtextField)
        formparent.addInputContainer(wxpanel)
        wxelements.append(wxtextField)
        
        #
        id = field.id
        if id: self._registerWidget(id, wxpanel)

        # add to sizer
        if wxelements:
            for e in wxelements: wxsizer.add(e)
        
        wxpanel.SetSizer(wxsizer)
        wxsizer.Fit(wxpanel)
        return wxpanel


    def onFormPasswordField(self, field):
        debug.log( 'working on %s' % field )
        name = field.name
        value = field.value
        
        parent = self._container_widget

        wxpanel = self.onFormField(field)
        wxsizer = wxpanel.GetSizer()
        wxelements = wxpanel.elements

        # the password box
        wxpasswordField = widgets.passwordfield(wxpanel, value=value, name=name)
        formparent = wxpasswordField.findFormParent()
        formparent.addInputWidget(wxpasswordField)
        formparent.addInputContainer(wxpanel)
        wxelements.append(wxpasswordField)
        
        #
        id = field.id
        if id: self._registerWidget(id, wxpanel)

        # add to sizer
        if wxelements:
            for e in wxelements: wxsizer.add(e)
        
        wxpanel.SetSizer(wxsizer)
        wxsizer.Fit(wxpanel)
        return wxpanel


    def onFormSelectorField(self, selector):
        debug.log( 'working on %s' % selector )
        parent = self._container_widget
        wxpanel = self.onFormField(selector)
        wxsizer = wxpanel.GetSizer()
        wxelements = wxpanel.elements

        #
        entries = selector.entries
        descriptions = [d for v, d in entries]
        wxchoice = widgets.choice(
            wxpanel, choices=descriptions, name=selector.name)
        if selector.selection:
            wxchoice.SetSelection(int(selector.selection))
        formparent = wxchoice.findFormParent()
        formparent.addInputWidget(wxchoice)
        formparent.addInputContainer(wxpanel)
        wxelements.append(wxchoice)

        # add to sizer
        if wxelements:
            for e in wxelements: wxsizer.add(e)
        
        wxpanel.SetSizer(wxsizer)
        wxsizer.Fit(wxpanel)
        return wxpanel


    def onFormRadioBox(self, radio):
        debug.log( 'working on %s' % radio )
        parent = self._container_widget
        wxpanel = self.onFormField(radio)
        wxsizer = wxpanel.GetSizer()
        wxelements = wxpanel.elements

        #
        entries = radio.entries
        descriptions = [d for v, d in entries]
        wxradiobox = widgets.radiobox(
            wxpanel, choices=descriptions, name=radio.name)
        if radio.selection:
            wxradiobox.SetSelection(int(radio.selection))
        formparent = wxradiobox.findFormParent()
        formparent.addInputWidget(wxradiobox)
        formparent.addInputContainer(wxpanel)
        wxelements.append(wxradiobox)

        # add to sizer
        if wxelements:
            for e in wxelements: wxsizer.add(e)
        
        wxpanel.SetSizer(wxsizer)
        wxsizer.Fit(wxpanel)
        return wxpanel


    def onFormTextArea(self, field):
        debug.log( 'working on %s' % field )
        name = field.name
        value = field.value
        
        parent = self._container_widget
        
        wxpanel = self.onFormField(field)
        wxelements = wxpanel.elements
        wxsizer = wxpanel.GetSizer()
        
        # the text box
        wxtextField = widgets.textfield(
            wxpanel,
            name=name,
            value=value, size=(600,200), style=wx.TE_MULTILINE)
        formparent = wxtextField.findFormParent()
        formparent.addInputWidget(wxtextField)
        formparent.addInputContainer(wxpanel)
        wxelements.append(wxtextField)
        
        #
        id = field.id
        if id: self._registerWidget(id, wxpanel)

        # add to sizer
        if wxelements:
            for e in wxelements: wxsizer.add(e)
        
        wxpanel.SetSizer(wxsizer)
        wxsizer.Fit(wxpanel)

        return wxpanel


    def onFormCheckBox(self, field):
        debug.log( 'working on %s' % field )
        name = field.name
        #value = field.value
        checked = field.checked
        
        parent = self._container_widget

        wxpanel = self.onFormField(field)
        wxsizer = wxpanel.GetSizer()
        wxelements = wxpanel.elements

        # the text box
        wxcheckBox = widgets.checkbox(wxpanel, value=checked, name=name)
        formparent = wxcheckBox.findFormParent()
        formparent.addInputWidget(wxcheckBox)
        formparent.addInputContainer(wxpanel)
        wxelements.append(wxcheckBox)
        
        #
        id = field.id
        if id: self._registerWidget(id, wxpanel)

        # add to sizer
        if wxelements:
            for e in wxelements: wxsizer.add(e)
        
        wxpanel.SetSizer(wxsizer)
        wxsizer.Fit(wxpanel)
        return wxpanel


    def onButton(self, button):
        parent = self._container_widget

        onclick = button.onclick
        def _(evt): self.compile(onclick, this=parent)
        callbacks={'click': _}

        icon = button.icon
        iconpath = None
        if icon:
            iconpath = self._iconpath(icon)
            
        wxbutton = widgets.buttonWithIcon(
            parent,
            callbacks=callbacks,
            label=button.label,
            iconpath=iconpath)
        
        wxbutton.SetToolTipString(button.tip)

        id = button.id
        if id: self._registerWidget(id, wxbutton)

        return wxbutton


    def onFormSubmitButton(self, button):
        parent = self._container_widget

        onclick = button.onclick
        def _(evt): self.compile(onclick, this=parent)
        callbacks={'click': _} 
        wxbutton = widgets.button(
            parent,
            callbacks=callbacks,
            label=button.label )
        
        id = button.id
        if id: self._registerWidget(id, wxbutton)

        return wxbutton


    def onFormField(self, field):
        required = field.required
        label = field.label
        error = field.error
        help = field.help
        name = field.name
        
        parent = self._container_widget

        # a panel dedicated for this field
        wxpanel = widgets.formfield(parent, name=name)
        wxelements = []
        wxsizer = widgets.sizer(orientation='vertical')
        wxpanel.SetSizer(wxsizer)

        # the label
        wxlabel = widgets.text(wxpanel, label)
        wxelements.append(wxlabel)

        # the error
        error = error or ''
        wxerror = widgets.text(wxpanel, error)
        wxpanel.errorwidget = wxerror
        wxelements.append(wxerror)
        if not error:
            wxerror.Hide()

        # the help
        if help:
            wxhelp = widgets.text(wxpanel, help)
            wxelements.append(wxhelp)

        wxpanel.elements = wxelements
        return wxpanel


    def onTreeView(self, treeview):
        parent = self._container_widget

        wxtreeviewcontainer = widgets.treeviewContainer( parent )
        
        wxsizer = widgets.sizer(orientation='vertical')
        wxtreeviewcontainer.SetSizer(wxsizer)

        # set label
        title = widgets.text(wxtreeviewcontainer, treeview.label)
        wxsizer.add(title)

        wxtree = widgets.treeview(wxtreeviewcontainer)
        wxsizer.add(wxtree)
        wxsizer.Fit(wxtreeviewcontainer)

        # allow dragging
        if treeview.draggable:
            wxtree.bind()

        # bind dragging event
        ondrag = treeview.onnodemoving
        if ondrag:
            def _(evt): self.compile(ondrag)
            wxtree.bindcallbacks(callbackfunc=_)
            
        # create root branch
        if treeview.root:
            rootbranch = wxtree.addRoot(treeview.root.label)
            if treeview.root.id: self._registerWidget(treeview.root.id, rootbranch)
            for item in treeview.root.contents:
                wxrendered = self._render(item, container_widget = wxtreeviewcontainer)

        # register the tree
        id = treeview.id
        if id: self._registerWidget(id, wxtreeviewcontainer)

        #
        wxtree.ExpandAll()
        wxtree.CollapseAll()

        return wxtreeviewcontainer
   

    def onTreeViewBranch(self, branch):
        parent = self._container_widget

        # parent node and tree instance
        if isinstance(parent, wx.Panel):
            # parent is the tree container
            tree = parent.tree
            parentbranch = tree.root
        else:
            parentbranch = parent
            tree = parentbranch.tree()
            
        # callback
        onclick = branch.onclick
        def callback(): self.compile(onclick)
        branch.onclick_compiled = callback

        # add this to the tree
        wxbranch = tree.addNode(parentbranch, branch)

        # loop over the childe nodes
        for item in branch.contents:
            wxrendered = self._render(item, container_widget = wxbranch)

        # register
        id = branch.id
        if id: self._registerWidget(id, wxbranch)

        return wxbranch


    def onTreeViewLeaf(self, leaf):
        parent = self._container_widget

        # parent node and tree instance
        if isinstance(parent, wx.Panel):
            # parent is the tree container
            tree = parent.tree
            parentbranch = tree.root
        else:
            parentbranch = parent
            tree = parentbranch.tree()
            
        # callback
        onclick = leaf.onclick
        def callback(): self.compile(onclick)
        leaf.onclick_compiled = callback
        
        # add this to the tree
        wxleaf = tree.addNode(parentbranch, leaf)
        
        #
        id = leaf.id
        if id: self._registerWidget(id, wxleaf)
        
        return wxleaf


    def onToolbar(self, toolbar):
        parent = self._container_widget

        # using a horizontal sizer rather than a real wx Toolbar

        wxtoolbar = widgets.panel(parent)
        wxsizer = widgets.sizer(orientation = 'horizontal')

        for item in toolbar.contents:
            wxrendered = self._render(item, container_widget=wxtoolbar)
            wxsizer.add(wxrendered)

        wxtoolbar.SetSizer(wxsizer)
        wxsizer.Fit(wxtoolbar)

        id = toolbar.id
        if id: self._registerWidget(id, wxtoolbar)

        return wxtoolbar


    def onToolbarSpacer(self, spacer):
        parent = self._container_widget
        # these pixel sizes ok?
        wxspacer = wx.Size(20, 30) 
        return wxspacer


    def onLink(self, link):
        parent = self._container_widget

        onclick = link.onclick
        def _(evt): self.compile(onclick)

        wxlink = widgets.link(parent, callbacks={'click':_}, label=link.label)

        wxlink.SetToolTipString(link.tip)

        id = link.id
        if id: self._registerWidget(id, wxlink)

        return wxlink


    def onPlot2D(self, plot):
        parent = self._container_widget

        #onclick = link.onclick
        #def _(evt): self.compile(onclick)

        wxhistplotter = widgets.histogramPlotter(
            parent, 
            )
        wxhistplotter.makePylabUsable()

        id = plot.id
        if id: self._registerWidget(id, wxhistplotter)

        # the data
        curves = plot.curves

        # loop over curves and add each one
        curve0 = curves[0]
        from histogram import histogram
        h = histogram('h', [('x', curve0.x)], data=curve0.y)
        #wxhistplotter.plotter.plot(h)
        #wxhistplotter.update(h)
        
        return wxhistplotter


    def onTable(self, table):
        parent = self._container_widget

        data = table.data

        from luban.content.Link import Link
        for row in data:
            for cell in row:
                if isinstance(cell, Link):
                    #cell.onclick_compiled = lambda evt: self.compile(_.clicked_cell.onclick)
                    cell.onclick_compiled = _compiled(cell.onclick, self.compile)
            continue
        
        wxtable = widgets.table(
            parent=parent,
            model=table.model, view=table.view, data=table.data)
        
        # callbacks -- store which cell changed
        oncellchanged = table.oncellchanged
        row_identifiers = table.model.row_identifiers
        def _(evt):

            # the coordinates
            col = evt.GetCol(); row = evt.GetRow()

            # prepare data
            data = {}
            # 1. data to identify this row
            for name in row_identifiers:
                data[name] = wxtable.getCellValue(row=row, colname=name)
                continue
            # 2. data changed
            colname = wxtable.getColName(colno=col)
            data[colname] = wxtable.GetCellValue(row, col)

            wxtable.setEventData('row-changed', data)
            self.compile(oncellchanged)
            return

        import wx.grid
        wxtable.Bind(wx.grid.EVT_GRID_CELL_CHANGE, _)

        id = table.id
        if id: self._registerWidget(id, wxtable)

        return wxtable


    def onProgressBar(self, progressbar):
        parent = self._container_widget

        # onfinished
        onfinished = progressbar.onfinished
        def finished(evt):
            self.compile(onfinished)

        # onchecking
        onchecking = progressbar.onchecking
        def checking(evt):
            self.compile(onchecking)

        # skip is interval, in milliseconds
        skip = progressbar.skip
        if not skip:
            skip = 500 

        # progressbar panel
        wxprogressbar = widgets.progressbar(parent, checking=checking,
                                            finished=finished, skip=skip)

        wxsizer = widgets.sizer(orientation='vertical')
        wxprogressbar.SetSizer(wxsizer)
        
        # status label
        status = progressbar.status
        wxtext = widgets.text(wxprogressbar, status)
        wxsizer.add(wxtext)
        wxprogressbar.status = wxtext

        # progress bar
        wxgauge = wx.Gauge(wxprogressbar)
        wxgauge.SetValue(progressbar.percentage)
        wxsizer.add(wxgauge)
        wxprogressbar.gauge = wxgauge

        # start the timer and bind onchecking and onfinished
        wxprogressbar.startTimer()

        wxsizer.Fit(wxprogressbar)

        # register id
        id = progressbar.id
        if id: self._registerWidget(id, wxprogressbar)

        return wxprogressbar


    def _registerWidget(self, id, widget):
        globals = self._globals
        W = globals['W']
        W.register(id, widget)
        return


    def _render(self, document, container_widget):
        self._container_widget = container_widget
        return document.identify(self)


    pass # end of Renderer


def _compiled(action, compiler):
    def _(evt):
        return compiler(action)
    return _

from ._journals import *

# version
__id__ = "$Id$"

# End of file 

