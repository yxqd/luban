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


  // constants
  var kilo = 1024;
  var mega = kilo * kilo;


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
    var input_name = "luban_upload_file: " + id;
    var input_attrs = {
      'id': id+"-input",
      "type": "file",
      name:input_name,
    };
    if (kwds.multiple) input_attrs['multiple'] = 'multiple';
    var input = tag('input', input_attrs);
    form.append(input);

    // .. status
    var statusdiv = tag('div'); div.append(statusdiv);
    statusdiv.addClass('status');

    // .. progress bar
    var pbar = tag('div'); div.append(pbar);
    pbar.width(input.width());
    pbar.progressbar().hide();
    if ($.browser.msie) {
	pbar.addClass("msie");
	pbar.progressbar('value', 100);
    }


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
      ,singleFileUploads: false
      // ,"url": C.url
      ,"url": '/upload'
      ,"formData": [
	{name: 'uploadid', value: id}
      ]
      // , maxChunkSize: 1000000
      ,"done": function(e, data) {
	$(this).children('.ui-progressbar').hide();
	var files = [];
	for (var i=0; i<data.result.length; i++)
	  files.push(data.result[i].name);
	var status = files.join(', ');
	status += " uploaded.";
	$(this).children('.status').text(status);
	var extra = {
	  'filename': files[0],
	  'filenames': files.join(',')
	};
	$(this).trigger("luban-uploadcomplete", extra);
	$(this).data('progress_timer', 0);
      }
      ,"fail": function(e,data) {
	var reason = data.failure_reason;
	if (reason == null)
	    reason = "Upload failed: your file could be too large";
	var extra = {'reason': reason};
	$(this).trigger("luban-uploadfail", extra);
	$(this).data('progress_timer', 0);
	$(this).children(".ui-progressbar").fadeOut();
	$(this).children(".status").text('');
	$(this).children("form").fadeIn();
      }
      ,"send": function (e,data) {
	var totalsize = 0;
	if (!$.browser.msie) {
	  for (var i = 0; i<data.files.length; i++)
	    totalsize += data.files[i].size;
	}
	if (kwds.maxsize && totalsize>kwds.maxsize) {
	  data.failure_reason = "file size exeeds limit: " + kwds.maxsize/mega + "MB";
	  return false;
	}
	$(this).data("totalsize", totalsize);
	var form = $(this).children("form");
	form.fadeOut();
	$(this).children('.status').text('Uploading...');
	$(this).children(".ui-progressbar").fadeIn();
	// start timer
	$(this).data('progress_timer', 1);
        if ($.browser.msie) return;
	repeatGetUploadProgress($(this).attr('id'));
      }
      /*
      ,"progress": function(e, data) {
	var p = parseInt(data.loaded/data.total * 100, 10);
	$(this).children('.ui-progressbar').progressbar('value', p);
      }
      */
    });

    div.bind('uploader_progress', function(e, data) {
      if (data == null) return;
      if ($.browser.msie) return; // IE not supported
      var last = $(this).data('uploaded-last') || 0;
      var uploaded = last + (data.increment||0);
      var uploaded2 = data.uploaded;
      if (uploaded2 == null) return;
      if (uploaded2>uploaded) uploaded = uploaded2;
      var totalsize = $(this).data('totalsize');
      var p = parseInt(uploaded/totalsize * 100, 10);
      $(this).data('uploaded-last', uploaded);
      $(this).children('.ui-progressbar').progressbar('value', p);
    });

    // label, name, parameters

    return ret;
  };
  function repeatGetUploadProgress(uploadid) {
    getUploadProgress(uploadid);
    if ($('#'+uploadid).data('progress_timer')) {
      var f = "luban.widgets.uploader.repeatGetUploadProgress('"+uploadid+"')";
      setTimeout(f, 1000);
    }
  }

  function getUploadProgress(uploadid) {
    var uploader = $('#'+uploadid);
    if (!(uploader.data('progress_timer'))) return;
    var callback = function (data) {
      uploader.trigger('uploader_progress', data);
    };
    $.get('/upload_progress', {'id': uploadid}, callback, 'json');
  }

  widgets.uploader = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  // this export method repeatGetUploadProgress to global namespace
  // for setTimeout to work
  widgets.uploader.repeatGetUploadProgress = repeatGetUploadProgress;
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
