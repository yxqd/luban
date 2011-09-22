// -*- JavaScript -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                       (C) 2008-2011 All Rights Reserved
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
  dmp.onuploader = dmp._onElement;


  // uploader
  ef.uploader = function (kwds, docmill, parent) {
    // create the elements
    var id = kwds.id;
    // .. the div container
    var div = tag('div', {'id': id});
    // .. luban wrapper
    var ret = div.lubanElement('uploader');
    // .. add me to my parent
    if (parent) {parent.add(ret);}
    // .. class
    var Class = kwds.Class;
    div.addClass(Class);
    div.addClass('luban-uploader');

    // .. label
    var labelelem = tag('div'); div.append(labelelem);
    labelelem.addClass('label');

    // .. form in the div
    var form = tag('form'); div.append(form);
    // .. input in the form
    var input = tag('input', {'id': id+"-input", "type": "file", name:"myfile"}); // multiple?
    form.append(input);

    // .. status
    var statusdiv = tag('div'); div.append(statusdiv);
    statusdiv.addClass('status');

    // .. progress bar
    var pbar = tag('div'); div.append(pbar);
    pbar.progressbar().hide();

    // events
    var onsubmit = kwds.onsubmit;
    // onsubmit must be a simple load action
    // if (onsubmit.luban_type!='loading') {throw 'uploader.onsubmit must be a load action';}
    // build the url of the handler on the server side
    // var actor = onsubmit.actor; var routine = onsubmit.routine; var data = onsubmit.params;
    // var C = luban.Controller;
    // var credArgs = {};
    // var credArgs = C.getCredentialArgs();
    // data = C.prependActorStr(data);
    // var parameters = $.extend({}, {'actor':actor, 'routine':routine}, data, credArgs);
    //
    var name = kwds.name;
    var label = kwds.label;
    labelelem.text(label);

    // oncomplete
    var oncomplete = kwds.oncomplete, oncomplete_callback;
    if (oncomplete) {
      oncomplete_callback = luban.compileCallback(oncomplete);
      $(div).bind('luban-uploadcomplete', oncomplete_callback);
    }
    // onfail
    var onfail = kwds.onfail, onfail_callback;
    if (onfail) {
      onfail_callback = luban.compileCallback(onfail);
      $(div).bind('luban-uploadfail', onfail_callback);
    }

    //
    $(div).fileupload({
      dataType: 'json'
      // ,"url": C.url
      ,"url": '/upload'
      ,"done": function(e, data) {
	$(this).children('.ui-progressbar').hide();
	var file = data.result[data.result.length-1];
	var status = file.name + " uploaded.";
	$(this).children('.status').text(status);
	var extra = {
	  'filename': file.name
	};
	$(this).trigger("luban-uploadcomplete", extra);
      }
      ,"fail": function(e,data) {
	var extra = {
	  'reason': "unknown"
	};
	$(this).trigger("luban-uploadfail", extra);
      }
      ,"start": function (e,data) {
	var form = $(this).children("form");
	form.fadeOut();
	$(this).children('.status').text('Uploading...');
	$(this).children(".ui-progressbar").fadeIn();
      }
      ,"progress": function(e, data) {
	var p = parseInt(data.loaded/data.total * 100, 10);
	$(this).children('.ui-progressbar').progressbar('value', p);
      }
    });

    // label, name, parameters

    return ret;
  };

  widgets.uploader = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  // self check
  widgets.uploader.selfcheck = function() {
    var required;
    try {
      // required = $.fn.uploadify;
	required = 1;
    } catch (e) {
      //throw;
      return true;
    }
    return required == null;
  };
  widgets.uploader.prototype = new widgets.base ();

  // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  // the following should be obsolete sooon
  // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  // jquery like syntax to make a div a uploader button
  //  name: name of the uploader
  //  action: the url of the controller that takes action on the uploaded stuff
  //  parameters: parameters to controller
  $.fn.uploader = function(label, name, action, parameters, oncomplete) {

    // "this" is the division for the button
    var div = $(this);

    // create the subelments
    var table = tag('table');
    div.append(table);
    var tbody = tag('tbody');
    table.append(tbody);
    var tr = tag('tr');
    tbody.append(tr);
    var buttontd = tag('td');
    tr.append(buttontd);
    var buttondiv = tag('div', {'class': 'luban-uploader-button-container'});
    buttontd.append(buttondiv);
    var button = tag('div', {'class': 'luban-uploader-button'});
    buttondiv.append(button);
    var statustd = tag('td');
    tr.append(statustd);
    var status = tag('div');
    statustd.append(status);

    button.text(label);

    // the interval callback
    var interval;

    var ajaxupload = new Ajax_upload(button,
    {action: action,
     data: parameters,
     name: name,
     onSubmit : function(file, ext){
	// change button text, when user selects file
	status.text('Uploading');

	// If you want to allow uploading only 1 file at time,
	// you can disable upload button
	this.disable();

	// Uploding -> Uploading. -> Uploading...
	interval = window.setInterval(function(){
	    var text = status.text();
	    if (text.length < 13){
	      status.text(text + '.');
	    } else {
	      status.text('Uploading');
	    }
	  }, 200);
      },
     onComplete: function(file, response){
	window.clearInterval(interval);

	// enable upload button
	this.enable();

	// show filename
	status.text("'"+ file +"' uploaded");

	// run callback
	if (oncomplete)
	  {oncomplete();}
      }
    });

  };


})(luban, jQuery);


// End of file
