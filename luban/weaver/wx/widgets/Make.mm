# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin    
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = luban
PACKAGE = weaver/wx/widgets

# directory structure

BUILD_DIRS = \
	science \
	wxmpl \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	Button.py \
	ButtonWithIcon.py \
	CheckBox.py \
	Choice.py \
	CommonInterface.py \
	Dialog.py \
	Form.py \
	FormField.py \
	HtmlPanel.py \
	ListBox.py \
	MainFrame.py \
	MainWinApp.py \
	Menu.py \
	MenuBar.py \
	MenuItem.py \
	Notebook.py \
	Panel.py \
	ProgressBar.py \
	RadioBox.py \
	Sizer.py \
	Splitter.py \
	StaticText.py \
	TextField.py \
	PasswordField.py \
	HistogramPlotPanel.py \
	Accordion.py \
	Link.py \
	MainView.py \
	Table.py \
	TreeView.py \
	TreeViewContainer.py \
	__init__.py \
	ext.py \
	globalID.py \



#include doxygen/default.def

export:: export-package-python-modules 

# version
# $Id: Make.mm 1205 2006-11-15 16:23:10Z linjiao $

# End of file
