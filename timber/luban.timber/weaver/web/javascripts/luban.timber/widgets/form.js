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
  dmp.onform = dmp._onContainer;

  // action renderer
  var lap = luban.actioncompiler.prototype;
  lap.onformclearerrors = function(action) {
    var form = this.dispatch(action.element);
    return form.clearErrors();
  };
  lap.onformsubmission = function(action) {
    var form = this.dispatch(action.element);
    return form._je.submit();
  };

  // form
  ef.form = function (kwds, docmill, parent) {
    var Class = kwds.Class;
    var id = kwds.id;
    var form = tag('form', {'id': id});

    var ret = form.lubanElement('form');
    if (parent) { parent.add(ret); }

    form.addClass(Class);
    form.addClass('luban-form');

    var fieldset = tag('fieldset'); form.append(fieldset);

    var title = kwds.title;
    var legend = tag('legend'); fieldset.append(legend);
    if (title) {
      legend.text(title);
    } else {
      legend.hide();
    }
    var onsubmit = kwds.onsubmit;
    if (onsubmit != null && onsubmit != '') {
      create_onsubmit_handler(kwds, form);
    } else {
      form.submit(function () {return false;});
    }

    var onclick = kwds.onclick;
    if (onclick) {
      form.click( function() { docmill.compile(onclick); return false; } );
    }
    return ret;
  };

  var create_onsubmit_handler = function(spec, form) {
   var callback = luban.compileCallback(spec.onsubmit);
   form.bind('luban-formsubmit', callback);
   form.submit(
     function (event) {
       var data = $(this).serializeArray();
       // data is now an array of {name: , value:}
       // convert to dict
       data = _arr2dict(data);
       data = JSON.stringify(data);
       data = {'data': data};
       $(this).trigger('luban-formsubmit', data);
       return false;
     }
   );
  };

  var _arr2dict = function(arr) {
    var d = {};
    for (var i=0; i<arr.length; i++) {
      var e = arr[i];
      d[e.name] = e.value;
    }
    return d;
  };

  widgets.form = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  widgets.form.prototype = new widgets.base ();
  widgets.form.prototype.empty = function() {
    this.broadcastEvent('destroy');
    this._je.find('fieldset').empty();
  };
  widgets.form.prototype.add = function (subelem) {
    this._je.find('fieldset').append(subelem._je);
  };
  widgets.form.prototype.clearErrors = function (subelem) {
    // clear error boxes in the form
    this._je.find('.error').hide();
    this._je.find('.error-sign').hide();
  };
  widgets.form.prototype.setAttribute = function(attrs) {
    var form = this._je;
    var fieldset = form.children('fieldset');

    var title = attrs.title;
    var legend = fieldset.children('legend');
    if (title) {
      legend.text(title).show();
    } else {
      if (title=='')
	{ legend.text(title).hide(); }
    }

    var Class = attrs.Class;
    if (Class) {
      form.removeClass();
      form.addClass(Class);
    }
  };


 })(luban, jQuery);


// End of file
