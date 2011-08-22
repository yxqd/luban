# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



class Table2Dict:


    def onTable(self, table):
        ret = {}
        ret['type'] = 'table'
        ret['id'] = table.id
        if table.Class:
            ret['Class'] = table.Class
        if table.onclick:
            ret['onclick'] = table.onclick.identify(self)
        if table.hidden:
            ret['hidden'] = table.hidden
        ret['model'] = self.onTableModel(table.model)
        ret['view'] = self.onTableView(table.view)
        ret['data'] = self.onTableData(table.data)
        if table.oncellchanged:
            r = table.oncellchanged.identify(self)
            ret['oncellchanged'] = r
        return ret


    def onTableData(self, data):
        ret = []
        for row in data:
            row1 = []
            for cell in row:
                if isinstance(cell, Element):
                    cell = cell.identify(self)
                row1.append(cell)
                continue
            ret.append(row1)
            continue
        return ret


    def onTableModel(self, model):
        ret = {}
        measures = model.iterDescriptors()
        for measure in measures:
            name = measure.name
            type = measure.type
            default = measure.default
            ret[name] = {
                'type': type,
                'name': name,
                #'default': default,
                }
            continue
        ret['row_identifiers'] = model.row_identifiers
        return ret


    def onTableView(self, view):
        return self._onElement(view)


    def onTableViewColumn(self, col):
        return self._onElement(col)



from luban.ui.elements.Element import Element

# version
__id__ = "$Id$"

# End of file 
