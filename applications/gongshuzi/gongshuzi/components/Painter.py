# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from luban.content import select, load, alert
from luban.content.ElementContainer import ElementContainer


from pyre.components.Component import Component as base


class Painter(base):
    

    class Inventory( base.Inventory):
        pass


    def __init__(self, name='painter'):
        super(Painter, self).__init__(name=name, facility = 'painter')
        return


    def _createProjectServeStatusIndicator(self, status, port):
        if status == 'alive':
            url = 'http://localhost:%s/cgi-bin/main.py' % port
            return [
                'active at <a class="alive" href="%s" target="_blank">%s</a>' % (url, url),
                ]
        return [
            '<p class="darkred">not started.</p>',
            '<p>To start, click menu "Project->serve"</p>',
            ]


    def _createActorList(self, actors, session_id, selected=None):
        self._debug.log('actors=%s, session_id=%s, selected=%s' % (
            ','.join([a.id for a in actors]), session_id, selected and selected.id,))

        if selected: selected = selected.id
        
        from luban.content.Portlet import Portlet
        p = Portlet(id='actor-list')
        for actor in actors:
            item = self._createActorItemInActorList(actor, session_id)
            if selected:
               if selected == actor.id: item.selected = True
            p.add(item)
            continue
        return p


    def _createActorItemInActorList(self, actor, session_id, selected=None):
        from luban.content.PortletItem import PortletItem
        id = self._actoritemid(actor)
        item = PortletItem(label = actor.actorname, id=id)
        item.onclick = load(
            actor='gongshuzi', routine='switchActor',
            session_id = session_id,
            focus = refStrFromRecord(actor),
            )
        if selected: item.selected = selected
        return item
    

    def _createActorEditor(self, actor, session_id):
        from luban.content.CodeEditor import CodeEditor
        editor = CodeEditor()
        editor.syntax = 'python'
        editor.text = actor.content
        editor.onsave = select(element=editor).notify(
            'save',
            actor='actorcodeeditor', routine='processUpdate',
            session_id = session_id,
            actor_id = actor.id,
            )
        editor.onchange = select(element=editor).notify(
            'change',
            actor='actorcodeeditor', routine='processUpdate',
            session_id = session_id,
            actor_id = actor.id,
            )
        return editor


    def _createProjectSettingsTable(self, session, project, settings):
        from luban.content.table import Model,  View, Table
        class model(Model):

            property = Model.descriptors.str(name='property')
            value = Model.descriptors.str(name='value')

            row_identifiers = ['property']

        view = View(
            columns = [
                View.Column(label='Property', measure='property'),
                View.Column(label='Value', editable=True, measure='value'),
                ],
            editable = True,
            )

        data = [
            ('port', settings.port),
            ]

        table = Table(model=model, data=data, view=view, id='projectsettings-table')

        table.oncellchanged = select(element=table).notify(
            event='row-changed',
            actor='projectsettings', routine='processUpdate',
            session_id = session.id,
            project_id = project.id,
            settings_id = settings.id,
            )
        return table
        
    
    def _createPropertyTable(self, target, record_id, session_id, excludes=[]):
        iterprops = self._iterPropertyKVpairs(target)
        
        from luban.content.table import Model,  View, Table
        class model(Model):

            property = Model.descriptors.str(name='property')
            value = Model.descriptors.str(name='value')
        
            row_identifiers = ['property']
        
        view = View(
            columns = [
                View.Column(label='Property', measure='property'),
                View.Column(label='Value', editable=True, measure='value'),
                ],
            editable = True,
            )

        data = [(k,v) for k,v in iterprops if k not in excludes]

        table = Table(model=model, data=data, view=view, id='propertyeditor-table')

        table.oncellchanged = select(element=table).notify(
            event='row-changed',
            actor='propertyeditor', routine='processUpdate',
            session_id = session_id,
            record_id = record_id,
            )

        return table
    
    
    def _createTreeView(self, visual, clerk, session_id):
        from luban.content.TreeView import TreeView
        painter = self
        class _:

            def __init__(self, clerk):
                self.clerk = clerk
                return

            
            def render(self, visual):
                return self.onVisual(visual)
            

            def onVisual(self, visual):
                treeviewid = painter._treeviewid(visual)
                treeview = TreeView(id=treeviewid)
                treeview.draggable=True
                treeview.onnodemoving=select(element=treeview).notify(
                    event = 'nodemoving',
                    actor='objtree', routine='movenode',
                    session_id = session_id,
                    objtype = visual.name, objid = visual.id,
                    )
                
                inst = visual.visualinstance
                if not inst or not inst.id: return treeview
                
                inst = inst.dereference(self.clerk.db)
                self.currentNode = treeview
                self.dispatch(inst)
                
                return treeview
            

            def dispatch(self, record):
                
                clerk = self.clerk
                
                # find the original data object
                Object = clerk.orm.getObject(record.__class__)
                #
                opts = painter._treeviewNodeParams(record, session_id)
                
                if isinstance(self.currentNode, TreeView):
                    me = self.currentNode.setRoot(**opts)
                else:
                    if issubclass(Object, ElementContainer):
                        me = self.currentNode.branch(**opts)
                    else:
                        me = self.currentNode.leaf(**opts)
                        return me
                    
                contents = record.contents.dereference(clerk.db)
                for name, element in contents:
                    self.currentNode = me
                    self.dispatch(element)
                    continue
                return me

        return _(clerk).render(visual)


    def _createPreviewForActor(self, actor, clerk, session_id):
        return self._createActorEditor(actor, session_id)


    def _createPreviewForVisual(self, visual, clerk, session_id):
        inst = visual.visualinstance
        if not inst or not inst.id: return
        inst = inst.dereference(clerk.db)
        return self._createPreviewForElementR(inst, clerk, session_id)


    def _createPreviewForElementR(self, element, clerk, session_id):
        painter = self
        class _:

            def __init__(self, clerk):
                self.clerk = clerk
                return
            

            def render(self, element):
                klass = element.__class__.__name__
                handler = 'on'+klass
                if not hasattr(self, handler):
                    handler = 'default'
                handler = getattr(self, handler)
                return handler(element)


            def default(self, element):
                clerk = self.clerk
                
                preview = painter._createPreviewForElement(
                    element, clerk,
                    session_id=session_id)
                
                if not hasattr(element, 'contents'): return preview

                preview.contents = []
                for name, subelement in element.contents.dereference(clerk.db):
                    preview.contents.append(self.render(subelement))
                    continue
                return preview

        return _(clerk).render(element)


    def _createPreviewForElement(self, element, clerk, selected = False, session_id = None):

        Object = clerk.orm.getObject(element.__class__)
        if element.name == 'frames':
            # frame is special
            # we cannot create a frame since it will wipe everything out
            from luban.content.Document import Document as elementfactory
        else:
            # other elements are ok
            elementfactory = Object
            
        preview = elementfactory()

        excluded = ['time_created', 'creator', 'id', 'globalpointer']
        for colname in element.getColumnNames():
            if colname in excluded: continue
            value = element.getColumnValue(colname)
            attrname = colname2attrname(colname, Object)
            preview.setAttribute(attrname, value)
            continue

        preview.id = self._previewid(element)
        preview.onclick = load(
            actor='gongshuzi',
            routine='switchElement',
            session_id = session_id,
            focus = refStrFromRecord(element),
            )
            
        preview.Class += ' preview'
        if selected: preview.Class += ' selected'
        return preview


    def _treeviewNodeParams(self, record, session_id):
        label = self._treeviewnodelabel(record)
        id = self._treeviewnodeid(record)
        onclick = load(
            actor='gongshuzi',
            routine='switchElement',
            focus = refStrFromRecord(record),
            session_id = session_id,
            event_origin = 'treeview',
            )
        opts = {
            'id': id,
            'label': label,
            'onclick': onclick,
            }
        return opts
    

    #
    def _iterPropertyKVpairs(self, attributeContainer):
        proptypes = [
            'str',
            'int',
            'float',
            # hackish support
            'list',
            ]
        for descriptor in attributeContainer.getDescriptors():
            type = descriptor.type
            if type not in proptypes:
                continue
            name = descriptor.name
            value = descriptor.__get__(attributeContainer)
            if type == 'list':
                value = '\n'.join(value)
            yield name, value
            continue

        return


    # misc
    def _treeviewnodelabel(self, record):
        return record.name + '#' + record.id


    def _treeviewid(self, record):
        return self._elementid('treeview', record)
    def _treeviewnodeid(self, record):
        return self._elementid('treeviewnode', record)
    def _previewid(self, record):
        return self._elementid('preview', record)
    def _accordionid(self, record):
        return self._elementid('accordion', record)
    def _accordionsectionid(self, record):
        return self._elementid('accordionsection', record)


    def _actoritemid(self, actor):
        return self._elementid('portletitem', actor)


    def _elementid(self, element, record):
        if not isinstance(element, basestring):
            # assume element is the ui element instance for the record
            element = element.__class__.__name__.lower()
        from dsaw.db._reference import reference
        refstr = str(reference(record.id, record.__class__))
        refstr = refstr.replace('###', '-----')
        return element + '-' + refstr


    def _decodeelementid(self, s, element):
        'decode the element id to return a reference object'
        if not isinstance(element, basestring):
            # assume element is the ui element instance for the record
            element = element.__class__.__name__.lower()
        s = s[len(element)+1:]
        s = s.replace('-----', '###')
        return s


def refStrFromRecord(r):
    from dsaw.db._reference import reference
    return str(reference(r.id, r.name))


from gongshuzi.dom.orm import colname2attrname


# version
__id__ = "$Id$"

# End of file 
