.. _API:

API
===

UI elements
-----------

Common Interface
^^^^^^^^^^^^^^^^

.. .. inheritance-diagram:: luban.content.Accordion luban.content.Action luban.content.AppendElement luban.content.AppMenuBar luban.content.AttributeContainer luban.content.Button luban.content.CodeEditor luban.content.Controller luban.content.Credential luban.content.CredentialFactory luban.content.descriptors luban.content.Document luban.content.DocumentFactory luban.content.Element luban.content.ElementActionExtensions luban.content.ElementActions luban.content.ElementContainer luban.content.ElementNotRoot luban.content.Form luban.content.FormActions luban.content.FormCheckBox luban.content.FormField luban.content.FormFieldActions luban.content.FormPasswordField luban.content.FormSelectorField luban.content.FormSubmitButton luban.content.FormTextArea luban.content.FormTextField luban.content.GUID luban.content.HtmlDocument luban.content.Link luban.content.LinkFactory luban.content.Loading luban.content.Notification luban.content.Frame luban.content.Paragraph luban.content.ParagraphFactory luban.content.Plot2D luban.content.Portlet luban.content.PortletFactory luban.content.PortletItem luban.content.ProgressBar luban.content.RemoveContent luban.content.ReplaceContent luban.content.ReSTDocument luban.content.ReStructuredTextDocument luban.content.SelectByElement luban.content.SelectByID luban.content.SimpleAction luban.content.SimpleContainer luban.content.SimpleElementAction luban.content.Splitter luban.content.Submission luban.content.Tabs luban.content.TeleContainer luban.content.Toolbar luban.content.TreeView 
   :parts: 1

This section explains the common interface of UI elements.

All ui elements can be instantiated by ::

  >>> from luban.content.<Element> import <Element>
  >>> element = <Element>( prop1=value1, prop2 = value2, ...)

where <Element> should be replaced by whatever element type you are
trying to instantiate from.

For example, to create a form::

  >>> from luban.content.Form import Form
  >>> element = Form( prop1=value1, prop2 = value2, ...)

Each UI element type has some properties, and those properties
can be either set using the constructor as shown above, or just using
normal python attribute-setting syntax::

  >>> element.prop1 = value1

The common properties that every element type has are

* id: the unique id of the element.
* name: the name of the element. it should be unique among siblings.
* hidden: if true, the element is hidden
* Class: class of the element. useful for styling

A luban user interface is a hierarchy of UI elements. 
This hierarchy can be created step by step by creating the elements
higher in the hierarchy and adding children elements using
the parent's "add" method.
For example, the following code create a "document" element
and a "paragraph" element and add the "paragraph" element as a child::

  >>> from luban.content.Document import Document
  >>> doc = Document()
  >>> from luban.content.Paragraph import Paragraph
  >>> p =Paragraph()
  >>> doc.add(p)

For convenience,
some element containers might have member methods to create
subelements directly. For example, the above code piece is equivalent
to::

  >>> from luban.content.Document import Document
  >>> doc = Document()
  >>> p = doc.paragraph()

The convention for these member methods is 
that the signature of the member method to create a
subelement
is the same as that of the constructor of that subelement type. 
For example, to create a Paragraph instance, the constructor is::

  >>> p = Paragraph(id=..., text=...)

The 'paragraph' method of the Document type has the same signature, and you
can create a paragraph of a document by ::

  >>> p =doc.paragraph(id=..., title=...)

Please note that elements created from factory methods of element container
are automatically added into the container, and you should not use add
method to add the new element to the container again.

A common method of any element container is "credential"::

  >>> element.credential(username=..., ticket=...)

It creates a credential and attach it to the UI element container.
You should only create
one credential for the UI element tree you are creating. Otherwise,
which of the multiple credentials you created is used is undetermined.

To sum it up, the common properties of all elements are:

* id: unique id of the element
* name: name of the element. it should be unique among siblings
* Class: class of the element. most useful for styling
* hidden: if true, the element is hidden

The common methods are:

* add (for element container to add an element)
* credential (creates a credential)

The common event handlers are:

* onclick: event handler that triggers when a mouse click happens on this element
* oncreate (experimental): event handler that triggers when the widget
  is created on the interface
* onkeypress (experimental): event handler that triggers when user stroke a key and this element is on focus'

In the following, UI elements are grouped into several categories.
For each element type, description of what it is and its properties
are presented.

 
Root node
^^^^^^^^^

%{
widget_doc('Frame.Frame')
%}


Simple containers
^^^^^^^^^^^^^^^^^
Simple containers can have normal elements as their contents.

%{
widget_doc('Document.Document')
%}


%{
widget_doc('Dialog.Dialog')
%}


:mod:`Form`
"""""""""""
Form is a container of form fields and a submit button.

Note: A form cannot have another form as its descendent.

Properties

* title: title of the form
* onsubmit: The action or a list of actions to be taken when this form is submitted


Factory methods for creating sub-elements

* paragraph
* text: creates a text field
* password: creates a password field
* selector: creates a selector field
* radio: creates a radio box
* textarea: creates a text area
* checkbox: creates a check box
* submitbutton: creates a submit button

Class information of Form:

.. inheritance-diagram:: luban.content.Form
   :parts: 1

.. .. automodule:: luban.content.Form
   :members:
   :undoc-members:

.. _common_interface_for_form_fields:

Common interface for form fields
''''''''''''''''''''''''''''''''

Properties

* name: name of the field
* label: label of the field
* help: help of the field
* error: error of the field
* value: value of the field
* tip: tip of the field
* onchange: event handler when input changes for this field
* onfocus: event handler when this field gets focus
* onblur: event handler when this field losts focus

Note that all form fields must have an ancestor that is a form for the form-submit action
to work. Otherwise you need to use "onclick" handler to construct your own form-serialization
and submission actions.

Class information of FormField, their common ancestor:

.. inheritance-diagram:: luban.content.FormField
   :parts: 1

.. .. automodule:: luban.content.FormField
   :members:
   :undoc-members:

:mod:`FormTextField`
''''''''''''''''''''''''
Properties: see :ref:`common_interface_for_form_fields`


:mod:`FormPasswordField`
''''''''''''''''''''''''''''
Properties: see :ref:`common_interface_for_form_fields`


:mod:`FormTextArea`
'''''''''''''''''''''''
Properties: see :ref:`common_interface_for_form_fields`


:mod:`FormCheckBox`
'''''''''''''''''''''''
Properties: see :ref:`common_interface_for_form_fields`

* checked: boolean to indicate whether the check box is checked


:mod:`FormSelectorField`
''''''''''''''''''''''''''''
Properties: see :ref:`common_interface_for_form_fields`

* entries: enumerated list of 2-tuples. Each 2-tuple is (value, text). For example::

    [(0, 'Tiger'), (1, 'Monkey'), (2, 'Lion')]

* selection: int -- default selection index

:mod:`FormRadioBox`
'''''''''''''''''''''''

FormRadioBox is a group of radio buttons.

Properties: see :ref:`common_interface_for_form_fields`

* entries: enumerated list of strings -- choices to select from
* selection: int -- default selection's index


FormSubmitButton`
'''''''''''''''''''''''''''

Properties:

* label: label of the field
* help: help of the field


An example of using some of these Form Fields is::

        import luban.content
        form = luban.content.form()
        textarea = form.textarea(label='text area')
        textfield = form.text(label='text field')
        passwordfield = form.password(label='password')
        selectorfield = form.selector(entries=enumerate(['first choice', 'second choice']),
                                      selection=0)
        submitbutton = form.submitbutton(label='submit')


Basic widgets
^^^^^^^^^^^^^
This section contains some other basic widgets.

%{
widget_doc('Paragraph.Paragraph')
%}


%{
widget_doc('Link.Link')
%}


%{
widget_doc('Button.Button')
%}


%{
widget_doc('Image.Image')
%}


%{
widget_doc('Portlet.Portlet')
%}

%{
widget_doc('PortletItem.PortletItem', '\'')
%}


%{
widget_doc('Downloader.Downloader')
%}



Organizers:
^^^^^^^^^^^^^^^^

%{
widget_doc('Accordion.Accordion')
%}

%{
widget_doc('Accordion.AccordionSection', '\'')
%}


%{
widget_doc('Tabs.Tabs')
%}

%{
widget_doc('Tabs.Tab', '\'')
%}


%{
widget_doc('Splitter.Splitter')
%}

%{
widget_doc('Splitter.SplitSection', '\'')
%}


%{
widget_doc('Grid.Grid')
%}


Text-based documents:
^^^^^^^^^^^^^^^^^^^^^

%{
widget_doc('HtmlDocument.HtmlDocument')
%}


%{
widget_doc('ReStructuredTextDocument.ReStructuredTextDocument')
%}


Graphics
^^^^^^^^

%{
widget_doc('Plot2D.Plot2D')
%}



Miscellaneous widgets
^^^^^^^^^^^^^^^^^^^^^

%{
widget_doc('CodeEditor.CodeEditor')
%}


%{
widget_doc('ProgressBar.ProgressBar')
%}


%{
widget_doc('Toolbar.Toolbar')
%}


%{
widget_doc('NewsTicker.NewsTicker')
%}


%{
widget_doc('AppMenuBar.AppMenuBar')
%}

%{
widget_doc('AppMenuBar.AppMenu', '\'')
%}

%{
widget_doc('AppMenuBar.AppMenuItem', '\'')
%}


:mod:`TreeView` (experimental)
""""""""""""""""""""""""""""""

A TreeView is an expandable/collapsible tree containing TreeViewBranch and TreeViewLeaf objects. 

Properties

* label: label of the treeview
* root: a TreeViewBranch -- the root branch
* draggable: boolean -- whether the leaves/branches are draggable
* onclick: The action or a list of actions to be taken when this item is clicked

Factory methods for creating sub-elements

* setRoot: creates a new TreeViewBranch and sets that as the root branch

Note: a treeview only has one root. All further branches and leaves must be under this root branch.


.. _treeviewbranch:

TreeViewBranch
''''''''''''''

TreeViewBranch is a branch in a TreeView and can only be added to TreeViews or other TreeViewBranch objects.

Properties

* label: text label of this branch
* icon: icon of this branch
* tip: tip of this branch
* onclick: The action or a list of actions to be taken when this item is clicked

Factory methods for creating sub-elements

* branch: create a new branch under this branch
* leaf: create a new leaf under this branch

TreeViewLeaf
''''''''''''

TreeViewLeaf is a leaf on a TreeViewBranch. It must be added to a TreeViewBranch.

Properties: See properties of :ref:`treeviewbranch`

Example usage of TreeView, TreeViewBranch, and TreeViewLeaf::

        import luban.content
        treeview = luban.content.treeview()
        root = treeview.setRoot(label='root')
        branch1 = root.branch(label='branch 1')
        leaf = branch1.leaf(label='leaf')

Class information for TreeView, TreeViewBranch TreeViewLeaf:

.. inheritance-diagram:: luban.content.TreeView
   :parts: 1

.. .. automodule:: luban.content.TreeViewLeaf
   :members:
   :undoc-members:


:mod:`Table`
""""""""""""""

A Table is a grid with columns of cells.

Properties:

* model: a Model class (see below)
* view: a View instance (see below)
* data: a list of lists -- contains the data in the table's cells
* oncellchanged: The action or a list of actions to be performed when a cell is edited

:mod:`Model`
''''''''''''

Model describes the data model this table is used to represent. 
In the model you describe the available "measures" of the model by
specifying their names and types and other properties
using descriptors (see example below).

Properties:

* row_identifiers: list of strings -- names of the columns that are needed to uniquely identify entries in the table. For example, if entries in both columns named 'a' and 'b' are needed before a certain row can be identified, row_identifiers would be ['a', 'b']

:mod:`View`
'''''''''''

A View contains several columns.

Properties:

* editable: boolean -- whether this table is editable or not (default=False)
* columns: list of Column instances 

:class:`Column`
'''''''''''''''

A Column describes a column in a table, and is contained in columns in View.

Properties:

* editable: boolean -- whether this column is editable or not (default=False)
* label: label of the column
* measure: string -- matches the name property of the measure descriptors in Model
* hidden: boolean -- whether this column is hidden or not

Example usage of Table::

        from luban.content.table import Table, Model, View

        # create a model class
        class model(Model):

            firstname = Model.descriptors.str(name='firstname')
            lastname = Model.descriptors.str(name='lastname')

        # create a view
        view = View( columns =  [ View.Column(label='First Name', measure='firstname'),
                                  View.Column(label='Last Name', measure='lastname', 
                                              editable=True) ],
                    editable=True)

        # enter data
        data = [('John', 'Smith'), 
                ('Jane', 'Doe')]

        # create the table
        table = Table(model=model, data=data, view=view)



%{
widget_doc('science.MatterBuilder.MatterBuilder')
%}



Special elements
^^^^^^^^^^^^^^^^
Credential
""""""""""

Properties:

* username
* ticket

Class information for Credential:

.. inheritance-diagram:: luban.content.Credential
   :parts: 1

.. .. automodule:: luban.content.Credential
   :members:
   :undoc-members:



Actions
-------


Accessing controller
^^^^^^^^^^^^^^^^^^^^

Calling the methods described below returns an Action instance. This Action instance can be assigned to the 'onclick' attribute of an element, for example.

load: load actions 
"""""""""""""""""""

  >>> load(actor=..., routine=..., **kwds)

actor is a string that is the name of the actor.
routine is a string that is the name of the method to call in the actor.


notify: notify controller that an event happens to an element
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This method must be called by a :ref:`selector <selector>` that selects an UI element.

  >>> selector.notify(event, actor=..., routine=..., **kwds)

event is a string that is the name of the event.
actor is a string that is the name of the actor.
routine is a string that is the name of the method in that actor to call.


submit: submit form and load actions
""""""""""""""""""""""""""""""""""""

  >>> formselector.submit(actor=..., routine=..., **kwds)

formselector should be a :ref:`selector <selector>` to select a form. 
actor should be a string that is the name of the actor.
routine is a string that is the name of the method to call in that actor.



.. _selector:
 
Selector
^^^^^^^^
select: select a ui element
""""""""""""""""""""""""""""
  >>> select(id=...)
  >>> select(element=...)

select returns the element instance as a selector, finding it by either its id, a property of the element, or the element instance (if the element python instance is available in local namespace). You can use this to select a certain element to then perform actions on it.

For example, if you had a document with name document and id 'document1'::

        import luban.content
        document = luban.content.document(title='title', id='document1')

You could select this document by calling either::

        select(id='document1')

or::

        select(element=document)

You can then call the actions described below on the selected element (below, called 'selector').


find: find a descendent element
"""""""""""""""""""""""""""""""
 >>> select(id=...).find(name=...)

"find" can find a descendent of an ancestor element given the name of the descendent. 
The ancestor element itself must be specified by using a selector method.
The name of the descendent must be unique among all the descendents.

Common actions for elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the below samples, selector refers to the selected element. Calling each of the methods described below returns an Action instance. This Action instance can be assigned to the 'onclick' attribute of an element, for example.


show/hide: show/hide this element
"""""""""""""""""""""""""""""""""


enable/disable: enable/disable this element
"""""""""""""""""""""""""""""""""""""""""""
This only has effects on form fields at this moment. 
You can enable/disable any individual form field.
You can also enable/disable any element container, which will enable/disable 
all form fields inside the container.



empty: empty my content
"""""""""""""""""""""""
  >>> selector.empty()

This removes all children of the selected element.

replaceContent: replace my content with new content
"""""""""""""""""""""""""""""""""""""""""""""""""""
  >>> selector.replaceContent(newcontent)

newcontent is some element that you wish to replace the selected element with.

This replaces the selected content with newcontent.

append: append an element (hierarchy) to my content
"""""""""""""""""""""""""""""""""""""""""""""""""""
  >>> selector.append(newelement)

Add a child element, newelement, to the selected element. For example, add another text field to a form, or add another button to a document.

destroy: destroy me
"""""""""""""""""""
  >>> selector.destroy()

This removes the selected element.


focus: set focus
""""""""""""""""

  >>> selector.focus()

This action switch the focus to the selected element.

setAttr: set attribute of me
""""""""""""""""""""""""""""

  >>> selector.setAttr(attr1=value1, attr2=value2)

Use this to set the properties of an element. This method works for most
attributes (NOT include event handlers such as onclick) of most element types. 
But the following are exceptions

* TreeView and its node types
* ProgressBar
* ReSTDocument (obsolete)
* ReStructuredTextDocument
* AppMenuBar


getAttr: get attribute of me
""""""""""""""""""""""""""""

  >>> selector.getAttr(attrname)

Use this to get the value of an attribute of an element. 

Currently, this action is only implemented for form field types (FormTextField, etc).


addClass: add a class
"""""""""""""""""""""

  >>> selector.addClass(newclass)


removeClass: remove a class
"""""""""""""""""""""""""""

  >>> selector.removeClass(klass)


Credential manipulation
^^^^^^^^^^^^^^^^^^^^^^^

createCredential
""""""""""""""""
  >>> from luban.content import createCredential
  >>> action = createCredential(username=..., ticket=...)


updateCredential
""""""""""""""""
  >>> from luban.content import updateCredential
  >>> action = updateCredential(username=..., ticket=...)


removeCredential
""""""""""""""""
  >>> from luban.content import removeCredential
  >>> action = removeCredential()




Special actions of gui elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All actions of this kind have a similar signature::

  >>> selector.<elementtype>(<actiontype>, **parameters)

For example, to call "showError" on a formfield, do::

  >>> selector.formfield('showError', message=...)

Here, the method name "formfield" indicates that the action is done to a form field, 
and the first argument "showError" indicates what action to take, and
the keyword "message" specifies the argument for the action.

In the following, each section is for one element type, and actions
for that element type are listed.

form
""""
The actions here are good for forms.

* clearErrors: remove all error alerts in the form.

formfield
"""""""""
The actions here are good for form fields.

* showError: Displays an error message. Takes a string parameter that is the message, and should be called on a selected FormField element.

  Example usage::

    >>> action = select(id='passwordfield').formfield('showError', message='error!')
        
  where passwordfield is the id of a FormPasswordField, for example. 


The following are good for formselectorfield.

* addOption: add a new option to the selector


treeview
""""""""
The actions here are good for TreeView.

* setRoot: set the root node. 

  Example usage::

   >>> action = select(id='treeview').treeview('setRoot', root=...)

* addBranch: add a new branch

  Example usage::

   >>> action = select(id='treeview').treeview('addBranch', referencenode=..., newnode=..., position=...)

 * referencenode: selector of reference node
 * newnode: new node
 * position: options are "before", "after", or <index> (an integer)

  * before/after: meaning the new node is before or after the reference node
  * <index>: This option means that the reference node will be the parent node into which
    the new node will be added.
    The number given would be the index of the insert position among the children of the reference node

* removeNode: remove a node

  Example usage::

   >>> action = select(id='treeview').treeview('removeNode', node=...)

 * node: the node to be removed. If not given, means to remove the current selected node

* selectNode: select a node

  Example usage::

   >>> action = select(id='treeview').treeview('selectNode', node=...)

 * node: the node to be selected.


table
"""""
* getIdentifiersForCheckedRows: get identifiers for checked rows.

  Example usage::

   >>> action = select(id='table').table('getIdentifiersForCheckedRows', colname='selected')


accordion
"""""""""


dialog
""""""

* open: open the dialog

  Example usage::
    
   >>> action = select(id='dialog').open()

* close: close the dialog

  Example usage::
    
   >>> action = select(id='dialog').close()
   

tab
""""
 * select: select this tab
   

portletitem
"""""""""""
 * select: select this portletitem
   

Other actions
^^^^^^^^^^^^^

Here are some addtional actions.

* alert: Displays a warning message. Takes a string parameter that is the message.

 Example usage::

        from luban.content import alert
        warning = alert('Warning!')
        button.onclick = warning

 where button is a luban.content.Button, for example.


director
--------

You can think of director as the "controller" in the MVC.


.. _retrieveVisual:

retrieveVisual
^^^^^^^^^^^^^^

::

  director.retrieveVisual(name)

loads the odb file <luban_project>/content/components/visuals/<name>.odb,
and calls the method "visual" using "director" itself as the argument,
and returns the result of the method call.


