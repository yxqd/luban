#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                      California Institute of Technology
#                       (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import wx
#from ext import bindCallbacks
from luban.weaver.wx.widgets.CommonInterface import CommonInterface

from vimm.Renderers import RenderOptions, SimpleRenderer, LINES, BALLSTICK, \
     BALLS, CYLINDERS
#from luban.weaver.wx.widgets.science.Canvas import Canvas
from vimm.Canvas import Canvas

from vimm.CoordEditor import CoordEditor
from vimm.Animation import Animation
from vimm.Measurements import Measurements
from vimm.Sketcher import Sketcher
from vimm.CrystalBuilder import CrystalBuilder, CrystalDatabase, Supercell,\
     SlabBuilder, AddUC
from vimm.NanoBuilder import NanoBuilder
from vimm.AlkaneBuilder import AlkaneBuilder
from vimm.OrbitalViewer import OrbitalViewer
from vimm.BondAdjustor import BondAdjustor


borderStyles = {
    "sunken": wx.BORDER_SUNKEN,
    'default': wx.BORDER_DEFAULT,
    }

#events = {
#    'click': wx.EVT_BUTTON , 
#    }

#ids = {
#    'OK': wx.ID_OK,
#    'Cancel': wx.ID_CANCEL,
#    }

class MatterBuilder(wx.Panel, CommonInterface):
    
    
    def __init__(self, parentWindow, borderStyle=None, id=None):

        CommonInterface.__init__(self, parentWindow)

        if id is None: id = -1

        if borderStyle is None:
            borderStyle = 'default'
        style = borderStyles[ borderStyle ]
        wx.Panel.__init__(self, parentWindow, style = style)
        
        self.canvas = Canvas(self, -1)
        #self.canvas.SetSize((height, width))
        # replace this with structure, then translate to atoms
        self.material = None
        self.renderOptions = RenderOptions(CYLINDERS)
    
        from luban.content.AppMenuBar import AppMenuBar
        menubar = AppMenuBar()
        fileMenu = menubar.menu(label='File')
        
        from luban.content import select
        open = fileMenu.item(label='Open', 
                          onclick = self.load_file())
        save = fileMenu.item(label='Save', 
                          onclick = self.save_as())
        saveAs = fileMenu.item(label='Save As', 
                          onclick = self.save_as())    
        povray = fileMenu.item(label='EXport Povray', 
                          onclick = self.render_povray())  
        
        editMenu = menubar.menu(label='Edit')
        screenshot = fileMenu.item(label='Screenshot', 
                          onclick = self.dump())
        setBackground = fileMenu.item(label='Set Background Color', 
                          onclick = self.set_bg_color())
        editCoordinates = fileMenu.item(label='Edit Coordinates', 
                          onclick = self.edit_coord())   
         
#        viewMenu = menubar.menu(label='View')
#        animate = fileMenu.item(label='Animate', 
#                          onclick = self.animate())
#        lines = fileMenu.item(label='Lines', 
#                          onclick = self.set_render_lines())
#        ballAndStick = fileMenu.item(label='Ball and Stick', 
#                          onclick = self.set_render_ballstick())   
#        balls = fileMenu.item(label='Balls', 
#                          onclick = self.set_render_balls()) 
#        cylinders = fileMenu.item(label='Cylinders', 
#                          onclick = self.set_render_cylinders()) 
#        unitCell = fileMenu.item(label='Unit Cell', 
#                          onclick = self.set_unit_cell()) 
#        cellLabels = fileMenu.item(label='Cell Labels', 
#                          onclick = self.set_cell_labels()) 
#        atomLabels = fileMenu.item(label='Atom Labels', 
#                          onclick = self.set_atom_labels()) 
#        hideHydrogens = fileMenu.item(label='Hide Hydrogens', 
#                          onclick = self.set_hide_h()) 
#        
#        toolsMenu = menubar.menu(label='Tools')
#        measureDistances = fileMenu.item(label='Measure Distances', 
#                          onclick = self.measurements())
#        viewOrbitals = fileMenu.item(label='View Orbitals', 
#                          onclick = self.view_orbs())
#        adjustBonds = fileMenu.item(label='Adjust Bonds', 
#                          onclick = self.adjust_bonds()) 
#        crystalBuilder = fileMenu.item(label='Crystal Builder', 
#                          onclick = self.build_xtal())    
#        crystalDatabase = fileMenu.item(label='Crystal Database', 
#                          onclick = self.xtal_db())
#        buildSupercell = fileMenu.item(label='Build Supercell', 
#                          onclick = self.build_super())
#        buildSlab = fileMenu.item(label='Build Slab', 
#                          onclick = self.build_slab())
#        addUnitCell = fileMenu.item(label='Add Unit Cell', 
#                          onclick = self.add_uc())  
#        buildNanotube = fileMenu.item(label='Build Nanotube', 
#                          onclick = self.build_nano())
#        buildAlkane = fileMenu.item(label='Build Alkane', 
#                          onclick = self.build_alka())  
#        sketcher = fileMenu.item(label='Sketcher', 
#                          onclick = self.sketch())             
    #    menu2 = fileMenu.menu(label='menu2')
    #
    #    from luban.content import load
    #    item2 = menu2.item(label='item2')
    #    document.add(menubar)
    #
    #    item3 = menu2.item(label='item3')
        #doc.add(menubar)
        page.add(menubar)

    
    def load_file(self, *args):
        fname = None
        d = wx.FileDialog(self,"Open","","","*",wx.OPEN)
        if d.ShowModal() == wx.ID_OK:
            fname = d.GetFilename()
            dir = d.GetDirectory()
            fullfilename = os.path.join(dir,fname)
        d.Destroy()
        self.load_file_nodialog()#fullfilename)
        return
    
    def load_file_nodialog(self,fname=None):
        if fname:
            from vimm.Material import Material
#            from matter.Structure import Structure
            if isinstance(fname, Material):
                self.material = fname
#            elif isinstance(fname, Structure):
#                self.material = vimmLib.loadStructure(fname)
            else:
                self.material = vimmLib.load_file(fname, "GUI")
            if self.material:
                self.SetTitle("Vimm: %s" % self.material.name)
                self.render(1)
        return
    
    def save_as(self,*args):
        fname = None
        d = wx.FileDialog(self,"Save","","","*",wx.SAVE)
        if d.ShowModal() == wx.ID_OK:
            fname = d.GetFilename()
            dir = d.GetDirectory()
            fullfilename = os.path.join(dir,fname)
        d.Destroy()
        fullfilename = 'VimmFile.png'
        if fname:
            vimmLib.save_file(fullfilename, self.material, "GUI")
        return
    
    def render_povray(self,*args):
        povOutput = None
        d = wx.FileDialog(self,"Save","","","*",wx.SAVE)
        if d.ShowModal() == wx.ID_OK:
            povOutput = d.GetFilename()
            dir = d.GetDirectory()
            fullfilename = os.path.join(dir,povOutput)
        d.Destroy()
        fullfilename = 'VimmPovRayFile.png'
        if fullfilename:
            # Still to do:
            # - Background color
            # - Is the camera position reversed?
            from vimm.POVRay import Scene
            if self.material:
                shapes = SimpleRenderer(self.material.geo,self.renderOptions)
                shapes = shapes.povray()
                r,g,b = self.renderOptions.get_fg_color()
                scene = Scene(self.material.name)
                #scene.set_bgcolor(r/255.,g/255.,b/255.)
                x,y,z = self.canvas.camera.get_position()
                lx,ly,lz = self.canvas.camera.get_look_at()
                scene.set_camera((-x,y,-z),
                                 (lx,ly,lz))
                for shape in shapes:
                    scene.add(shape)
                scene.write_pov(outputFile = fullfilename)
                scene.render(outputFile = fullfilename)
                scene.display()
        return
        
    def dump(self,*args): pass#self.canvas.dump()

    def set_bg_color(self,*args):
#        d = wx.ColourDialog(self)
#        d.GetColourData().SetChooseFull(True)
#        if d.ShowModal() == wx.ID_OK:
#            data = d.GetColourData()
#            r,g,b = data.GetColour().Get()
#            color = r/255.,g/255.,b/255.
#            self.canvas.OnColor(color)
#            fg_r=255-r
#            fg_g=255-g
#            fg_b=255-b
#            fg_color=fg_r/255.,fg_g/255.,fg_b/255.
#            self.renderOptions.set_fg_color(fg_color)
#            self.render()
        return
    
    def edit_coord(self, *args):
        coord_editor = CoordEditor(self, -1)
        coord_editor.Show()
        return

    def animate(self, *args):
        animate_frame = Animation(self, -1)
        animate_frame.Show()
        return

    def set_render_lines(self, *args):
        self.renderOptions.set_mode(LINES)
        self.render()
        return

    def set_render_ballstick(self, *args):
        self.renderOptions.set_mode(BALLSTICK)
        self.render()
        return

    def set_render_balls(self, *args):
        self.renderOptions.set_mode(BALLS)
        self.render()
        return

    def set_render_cylinders(self, *args):
        self.renderOptions.set_mode(CYLINDERS)
        self.render()
        return

    def set_unit_cell(self, *args):
        self.renderOptions.show_unit_cells(self.viewmenu.IsChecked(self.ID_UNIT_CELL))
        self.render()
        return
        
    def set_cell_labels(self, *args):
        self.renderOptions.show_cell_labels(self.viewmenu.IsChecked(self.ID_CELL_LABELS))
        self.render()
        return
        
    def set_atom_labels(self, *args):
        self.renderOptions.show_atom_labels(self.viewmenu.IsChecked(self.ID_ATOM_LABELS))
        self.render()
        return
        
    def set_hide_h(self, *args):
        self.renderOptions.hide_hydrogens(self.viewmenu.IsChecked(self.ID_HIDE_H))
        self.render()
        return
    
    def measurements(self, *args):
        self.canvas.set_measure(True)
        self.measurement_window = Measurements(self, -1)
        self.measurement_window.Show()
        return
    
    def view_orbs(self, *args):
        if hasattr(self.material.geo, 'orbs'):
            ov = OrbitalViewer(self,-1)
            ov.Show()
        else:
            d = wx.MessageDialog(self,
                "Orbitals do not exist in this file",
                "Cannot View Orbitals",
                wx.ICON_ERROR)
            d.ShowModal()
            d.Destroy()
        return
    
    def adjust_bonds(self, *args):
        bondd = BondAdjustor(self,-1)
        bondd.ShowModal()
        return    
    
    def build_xtal(self, *args):
        xtlb = CrystalBuilder(self,-1)
        xtlb.ShowModal()
        return

    def xtal_db(self, *args):
        xtlb = CrystalDatabase(self,-1)
        xtlb.ShowModal()
        return

    def build_super(self, *args):
        xtlb = Supercell(self,-1)
        xtlb.ShowModal()
        return

    def build_slab(self, *args):
        xtlb = SlabBuilder(self,-1)
        xtlb.ShowModal()
        return

    def add_uc(self, *args):
        xtlb = AddUC(self,-1)
        xtlb.ShowModal()
        return

    def build_nano(self, *args):
        nanob = NanoBuilder(self,-1)
        nanob.ShowModal()
        return

    def build_alka(self, *args):
        alkab = AlkaneBuilder(self,-1)
        alkab.ShowModal()
        return

#    def zbuild(self,*args):
#        zbuilder = ZBuilder(self,-1)
#        zbuilder.Show()
#        return

    def sketch(self, *args):
        self.canvas.set_sketching(True)
        self.sketcher_window = Sketcher(self, -1)
        self.sketcher_window.Show()
        return


    def setAttribute(self, **kwds):
        if 'title' in kwds:
            title = kwds['title']
            self.titlewidget.SetLabel(title)
        return
    
    
    pass # end of Panel



# version
__id__ = "$Id$"

# End of file 
