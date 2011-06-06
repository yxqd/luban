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
PACKAGE = interface


# directory structure

BUILD_DIRS = \
	descriptors \
	science \
	table \

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
	Accordion.py \
	Action.py \
	AppendElement.py \
	AppMenuBar.py \
	AttributeContainer.py \
	Button.py \
	CodeEditor.py \
	CodeViewer.py \
	Controller.py \
	Credential.py \
	CredentialFactory.py \
	Dialog.py \
	Dock.py \
	Document.py \
	DocumentFactory.py \
	Downloader.py \
	Element.py \
	ElementNotRoot.py \
	ElementActions.py \
	ElementActionExtensions.py \
	ElementContainer.py \
	File.py \
	Form.py \
	FormActions.py \
	FormCheckBox.py \
	FormField.py \
	FormFieldActions.py \
	FormPasswordField.py \
	FormRadioBox.py \
	FormSelectorField.py \
	FormSubmitButton.py \
	FormTextArea.py \
	FormTextField.py \
	Frame.py \
	Grid.py \
	GUID.py \
	HtmlDocument.py \
	Image.py \
	InsertBeforeElement.py \
	Link.py \
	LinkFactory.py \
	Loading.py \
	NewsTicker.py \
	Notification.py \
	Page.py \
	Paragraph.py \
	ParagraphFactory.py \
	Plot2D.py \
	Portlet.py \
	PortletFactory.py \
	PortletItem.py \
	ProgressBar.py \
	ReplaceElement.py \
	ReSTDocument.py \
	ReStructuredTextDocument.py \
	RemoveContent.py \
	ReplaceContent.py \
	SelectByID.py \
	SelectByElement.py \
	SimpleAction.py \
	SimpleContainer.py \
	SimpleElement.py \
	SimpleElementAction.py \
	Splitter.py \
	Submission.py \
	Tabs.py \
	TeleContainer.py \
	Toolbar.py \
	TreeView.py \
	Uploader.py \
	__init__.py \
	_accountant.py \
	descriptors.py \
	decorators.py \
	special_containers.py \


#include doxygen/default.def

export:: export-package-python-modules 


docs: export-doxygen-docs

# version
# $Id: Make.mm 1213 2006-11-18 16:17:08Z linjiao $

# End of file
