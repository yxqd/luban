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

d = \
{
  "": {
     "stylesheets": [
        "jquery/ui/smoothness/ui.all.css",
        "jquery/jquery.tooltip.css",

        "luban.css"
        ],
     "jslibs":      [
        "jquery/jquery.js",
        "jquery/jquery.rightClick.js",
        "jquery/jquery.dimensions.js",
        "jquery/jquery.bgiframe.js",
        "jquery/jquery.tooltip.js",
        "jquery/ui/ui.core.js",
        "luban/luban-core.js",
        "luban/luban-controller.js",
        "luban/luban-actioncompiler.js",
        "luban/luban-compiler-preloader.js",
        "luban/luban-documentmill.js",
        "luban/luban-widgets-basic.js",

        "other/editarea_0_8_1_1/edit_area/edit_area_full.js"
        ]
  },
  "dialog": {
     "stylesheets": [
        ],
     "jslibs":      [
        "jquery/ui/ui.draggable.js",
        "jquery/ui/ui.resizable.js",
        "jquery/ui/ui.dialog.js"
        ]
  },
  "table": {
     "stylesheets": [
        "tabulator/datePicker.css",
        "tabulator/tabulator.css",
        "tabulator/tabulator-color.css"
        ],
     "jslibs":      [
        "jquery/date.js",
        "jquery/jquery.datePicker.js",
        "jquery/tabulator.js",
        "jquery/elementFactory.js",
        "jquery/tableFactory.js"
        ]
  },
  "treeview": {
     "stylesheets": [
        "jquery/jsTree/tree_component.css"
        ],
     "jslibs":      [
        "jquery/jsTree/_lib/css.js",
        "jquery/jsTree/source/tree_component.js"
        ]
  },
  "tabs": {
     "stylesheets": [
        ],
     "jslibs":      [
        "jquery/ui/ui.tabs.js"
        ]
  },
  "appmenubar": {
     "stylesheets": [
        "jquery/jquery.jdMenu.css"
        ],
     "jslibs":      [
        "jquery/jdMenu-1.4.1/jquery.jdMenu.js",
        "jquery/jdMenu-1.4.1/jquery.positionBy.js"
        ]
  },
  "accordion": {
     "stylesheets": [
        ],
     "jslibs":      [
        "jquery/ui/ui.accordion.js"
        ]
  },
  "progressbar": {
     "stylesheets": [
        ],
     "jslibs":      [
        "jquery/ui/ui.progressbar.js"
        ]
  },
  "plot2d": {
     "stylesheets": [
        ],
     "jslibs":      [
        "jquery/jquery.flot.js"
        ]
  },
  "codeeditor": {
     "stylesheets": [
        ],
     "jslibs":      [
        ]
  }
}


def generate(project):
    from luban.weaver.web._utils import jsonEncode
    return jsonEncode(d)


# version
__id__ = "$Id$"

# End of file 
