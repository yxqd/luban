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
  var lap = luban.actioncompiler.prototype;


  // form-related action handlers
  lap.onformfieldshowerrormessage = function(action) {
    return this.onformfieldshowerror(action);
  };
  lap.onformfieldshowerror = function(action) {
    var params = action.params;
    var message = params.message;
    element = this.dispatch(action.element);
    element._je.find('.error').text(message);
    element._je.find('.error-sign').show();
    element._je.find('.error-sign').click();
  };


  // common utility functions for default implementation of form fields
  // formfield
  widgets.formfield = function( kwds, docmill) {
    var id = kwds.id;

    var div = tag('div', {'id': id});

    div.addClass('luban-formfield');
    // the next line is for backward compatibility
    div.addClass('formfield');
    if (kwds.Class) {div.addClass(kwds.Class);}

    var div1 = tag('div'); div.append(div1); div1.addClass('label-container');

    if (kwds.required) {
      var span = tag('span'); span.addClass("formfieldRequired"); div1.append(span);
      span.text('&nbsp;');
    }

    var labeldiv = tag('div'); div1.append(labeldiv);
    var label = tag('label', {'for': id}); labeldiv.append(label);
    if (kwds.label) {
      label.text(kwds.label);
    } else {
      labeldiv.hide();
    }

    var help = kwds.help;
    if (help == null) {help = '';}
    var helpa = tag('a');
    div.append(helpa);

    helpa.addClass('help');
    // this is for backward compatibility
    helpa.addClass('formfieldHelp');
    if (help) {
      helpa.text(help);
    } else {
      helpa.hide();
    }
    var table = tag('table'); div.append(table);
    var tbody = tag('tbody'); table.append(tbody);
    var row = tag('tr'); tbody.append(row);
    var cell1 = tag('td'); row.append(cell1); cell1.addClass('input-container');
    var cell2 = tag('td'); row.append(cell2);

    var p = tag('span'); p.text('!'); cell2.append(p);
    p.addClass('error-sign');

    var error = kwds.error;
    var errordiv = tag('div'); div.append(errordiv);
    errordiv.addClass('error');
    if (error) {
      errordiv.text(error);
      errordiv.hide();
    }
    else {
      errordiv.hide();
      p.hide();
    }
    errordiv.click(function() {$(this).hide();});
    p.click(function() {
	//var offset = $(this).offset();
	var pos = $(this).position();
	//errordiv.offset(offset);
	//errordiv.css('top', offset.top-10);
	//errordiv.css('left', offset.left+17);
	errordiv.css('top', pos.top-10);
	errordiv.css('left', pos.left+17);
	errordiv.toggle('fast');
      });

    var onclick = kwds.onclick;
    if (onclick)
      { div.click( function() { docmill.compile(onclick); return false; } ); }

    return div;
  };
  widgets.create_onchange_event_handler_for_input = function(onchange, input, element) {
   // init 'oldvalue' data
   element._je.data('oldvalue', element.getAttribute('value'));
   // luban onchange event
   var callback = luban.compileCallback(onchange);
   input.bind('luban-formfieldchange', callback);
   // onchange handler will prepare data and trigger luban onchange handler
   input.change(
     function (event) {
       var old = element._je.data('oldvalue'), newval = element.getAttribute('value');
       element._je.data('oldvalue', newval);
       var data = {
	 'old': old,
	 'new': newval
       };
       $(this).trigger('luban-formfieldchange', data);
     }
   );
  };
  widgets.create_onfocus_event_handler_for_input = function(onfocus, input) {
   // luban onfocus event
   var callback = luban.compileCallback(onfocus);
   input.bind('luban-formfieldfocus', callback);
   // onfocus handler will prepare data and trigger luban onfocus handler
   input.focus(
     function (event) {
       var data = {};
       $(this).trigger('luban-formfieldfocus', data);
     }
   );
  };
  widgets.create_onblur_event_handler_for_input = function(onblur, input) {
   // luban onblur event
   var callback = luban.compileCallback(onblur);
   input.bind('luban-formfieldblur', callback);
   // onblur handler will prepare data and trigger luban onblur handler
   input.blur(
     function (event) {
       var data = {};
       $(this).trigger('luban-formfieldblur', data);
     }
   );
  };
  widgets.create_event_handlers_for_input = function(spec, input) {
    var onchange = spec.onchange;
    if (onchange) {
      widgets.create_onchange_event_handler_for_input(onchange, input);
    }

    var onfocus = spec.onfocus;
    if (onfocus) {
      widgets.create_onfocus_event_handler_for_input(onfocus, input);
    }

    var onblur = spec.onblur;
    if (onblur) {
      widgets.create_onblur_event_handler_for_input(onblur, input);
    }
  };
  widgets.formfield_setAttribute = function(formfield, attrs) {
    var id = attrs.id;
    var label;
    if (id!=null) {
      label = formfield.find('label');
      label.attr('for', id);
    }

    var name = attrs.name;
    if (name!=null) {
      var inputs = formfield.find('input');
      inputs.attr('name', widgets.formatElementName(name));
    }

    var Class = attrs.Class;
    if (Class) {
      formfield.removeClass();
      formfield.addClass('formfield');
      formfield.addClass(Class);
    }

    var helpdiv = formfield.children('.help');
    var help = attrs.help;
    if (help != null) {
      if (help) {
	helpdiv.text(help).show();
      } else {
	helpdiv.hide();
      }
    }

    var errordiv = formfield.children('.error');
    var error = attrs.error;
    if (error != null) {
      if (error) {
	errordiv.text(error).show();
      } else {
	errordiv.hide();
      }
    }

    var labelcontainerdiv = formfield.children('div.label-container');
    var labeldiv = labelcontainerdiv.children('div');
    label = attrs.label;
    if (label != null) {
      if (label) {
	labeldiv.text(label).show();
      } else {
	labeldiv.hide();
      }
    }
  };


  widgets.formfield_getAttribute = function(formfield, name) {
    if (name=='Class') {return formfield.attr('class');}
    if (name=='help') {
      var helpdiv = formfield.children('div.help');
      return helpdiv.text();
    }
    if (name=='error') {
      var errordiv = formfield.children('div.error');
      return errordiv.text();
    }
    if (name=='label') {
      var labelcontainerdiv = formfield.children('div.label-container');
      var labeldiv = labelcontainerdiv.children('div');
      return labeldiv.text();
    }
    return null;
  };


  // helpers
  // prepend 'actor.' to keys
  widgets.formatElementName = function (s) {
    return s;
    // return 'actor.'+s;
  };

 })(luban, jQuery);


// End of file
