// -*- JavaScript -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                       (C) 2008-2009 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


// requires:
//    * luban-core.js


(function(luban, $) {

  // aliases
  var ef = luban.elementFactory;
  var widgets = luban.widgets;
  var tag = luban.utils.tag;


  // documentmill handler
  var dmp = luban.documentmill.prototype;
  dmp.onformradiobox = dmp._onElement;

  //
  var formfield = widgets.formfield;
  var formfield_setAttribute = widgets.formfield_setAttribute;
  var formfield_getAttribute = widgets.formfield_getAttribute;
  var formatElementName = widgets.formatElementName;


  // formradiobox
  ef.formradiobox = function(kwds, docmill, parent) {
    // create skeleton
    var div = formfield(kwds, docmill), input_container = div.find('.input-container');
    div.addClass('luban-formradiobox');

    if (kwds.tip) {
      var tip = kwds.tip;
      div.attr('title', tip);
      div.tooltip({showURL: false});
    }

    // save. need it in setEntries
    div.data('name', kwds.name);

    // the luban element
    var ret = div.lubanElement('formradiobox');
    if (parent) {parent.add(ret);}

    // create inputs
    ret.setEntries(kwds.entries);

    // set value
    var selection = kwds.selection;
    if (selection != null) ret.setAttribute({value: selection});

    // event handlers
    input = div.find('input');
    var onchange = kwds.onchange;
    if (onchange) {
      widgets.create_onchange_event_handler_for_input(onchange, input, ret);
    }

    return ret;
  };

  widgets.formradiobox = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  widgets.formradiobox.prototype = new widgets.base ();
  widgets.formradiobox.prototype.getInputContainer = function() {
    return this._je.find('.input-container');
  };
  widgets.formradiobox.prototype.getInputWidgets = function(checked) {
    if (checked)
      {return this._je.find('input:checked');}
    return this._je.find('input');
  };
  widgets.formradiobox.prototype.setAttribute = function (attrs) {
    var je = this._je;
    formfield_setAttribute(je, attrs);

    var entries = attrs.entries;
    if (entries) this.setEntries(entries);

    var value = attrs.value;
    if (value != null) {
      var checked = this.getInputWidgets('checked');
      if (value!=checked.val()) {
	checked.removeAttr('checked');
	je.find("input[value='"+value+"']").attr('checked', 'checked');
      }
    }

  };
  widgets.formradiobox.prototype.setEntries = function (entries, selection) {
    var input_container = this.getInputContainer();
    input_container.empty();

    var name = this._je.data('name');
    var args =  {
      'name': formatElementName(name),
      'type': 'radio'
    };

    for (var i in entries) {
      var entry = entries[i];
      var args1 = $.extend({}, args);
      var value = entry[0], description = entry[1];
      args1['value']=value;
      var div1 = tag('div'); div1.addClass('luban-radiobutton-container');
      input_container.append(div1);
      var input = tag('input', args1);
      var text = tag('label'); text.text(description);
      div1.append(input);
      div1.append(text);
    }

  };
  widgets.formradiobox.prototype.getAttribute = function (name) {
    var je = this._je;
    var ret = formfield_getAttribute(name);
    if (ret) {return ret;}
    if (name=='value') {
      var checked = this.getInputWidgets('checked');
      return checked.val();
    }
  };


 })(luban, jQuery);


// End of file
