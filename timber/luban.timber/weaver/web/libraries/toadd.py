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


from .default import *

base['stylesheets'] += (
    'jquery/jquery.tooltip.css',
    )
    
base['javascripts'] += (
    'other/sprintf.js',
    'jquery/excanvas.min.js',
    'jquery/jquery.tooltip.js',
    'jquery/jquery.rightClick.js',
    'other/editarea/edit_area/edit_area_full.js', # hack. edit_area does not seem to work when dynamically loaded
    )


dialog = {
    'javascripts':
    (
    'jquery/ui/ui.dialog.js',
    ),
    }


uploader = {
    'javascripts':
    (
    'jquery/ajaxupload.3.0.js',
    ),
    }


table = {
    'stylesheets':
    (
    'tabulator/datePicker.css',
    'tabulator/tabulator.css',
    'tabulator/tabulator-color.css',
    ),
    'javascripts':
    (
    'jquery/date.js',
    'jquery/jquery.datePicker.js',
    'jquery/tabulator.js',
    'jquery/elementFactory.js',
    'jquery/tableFactory.js',
    )
    }

treeview = {
    'javascripts':
    (
    'jquery/jsTree/jquery.tree.js',
    ),
    }

newsticker = {
    'javascripts':
    (
    'jquery/jquery.newsticker.js',
    ),
    }

appmenubar = {
    'stylesheets':
    (
    'jquery/jquery.jdMenu.css',
    ),
    'javascripts':
    (
    'jquery/jdMenu-1.4.1/jquery.jdMenu.js',
    'jquery/jdMenu-1.4.1/jquery.positionBy.js',
    ),
    }

accordion = {
    'javascripts':
    (
    'jquery/ui/ui.accordion.js',
    ),
    }

progressbar = {
    'javascripts':
    (
    'jquery/ui/ui.progressbar.js',
    ),
    }

plot2d = {
    'javascripts':
    (
    'jquery/jquery.flot.js',
    'jquery/jquery.flot.selection.js',
    ),
    }

codeeditor = {
    }

codeviewer = {
    'stylesheets':
    (
    'other/prettifier/prettify.css',
    ),
    'javascripts':
    (
    'other/prettifier/prettify.js',
    ),
    }

matterbuilder = {
    'javascripts':
    (
    'other/o3djs/base.js',
    'other/o3djs/math.js',
    'other/o3djs/error.js',
    'other/o3djs/dump.js',
    'other/o3djs/primitives.js',
    'other/o3djs/texture.js',
    'other/o3djs/event.js',
    'other/o3djs/quaternions.js',
    'other/o3djs/rendergraph.js',
    'other/o3djs/debug.js',
    'other/o3djs/io.js',
    'other/o3djs/util.js',
    'other/o3djs/picking.js', 
    'other/o3djs/effect.js',
    'other/o3djs/material.js',
    'other/o3djs/element.js',
    'other/o3djs/shape.js',
    'other/o3djs/pack.js',     
    'other/o3djs/arcball.js',
    'other/o3djs/serialization.js',
    'other/o3djs/scene.js',
    'other/viewer/atomInfo.js',
    'other/viewer/lattice16.js',
    ),
    }


# version
__id__ = "$Id$"

# End of file 
