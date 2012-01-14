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
  dmp.onsketchcanvas = dmp._onElement;


  // sketchcanvas
  //  factory
  ef.sketchcanvas = function(kwds, docmill, parent) {
    var id = kwds.id;
    var div = tag('div', {"id": id}); div.addClass('luban-sketchcanvas-container');

    // tools
    var tools = tag('div'); div.append(tools);
    tools.addClass("tools");

    tools.append('<a href="#'+id+'-canvas'+ '" data-download="png" style="float: right; width: 100px;">Download</a>');

    // add some tools
    $.each(
      ['#f00', '#ff0', '#0f0', '#0ff', '#00f', '#f0f', '#000', '#fff'], 
      function() {
	tools.append("<a href='#" + id + "-canvas' data-color='" + this + "' style='width: 10px; background: " + this + ";'></a> ");
      });

    tools.append("<span>&nbsp&nbsp&nbsp&nbsp&nbsp</span>");

    $.each(
      [3, 5, 10, 15],
      function() {
	tools.append("<a href='#" + id + "-canvas' data-size='" + this + "' style='background: #ccc'>" + this + "</a> ");
      });


    // canvas
    var opts = {"id": id+'-canvas', "width": kwds.width, "height": kwds.height};
    var canvas = tag("canvas", opts); div.append(canvas);

    //
    canvas.sketch();

    // 
    var savefn = createSaveFn(id, kwds.onsave);

    if (kwds.onsave) {
      var callback = luban.compileCallback(kwds.onsave);
      div.bind('luban-sketchcanvassave', callback);
    
      var savebtn = $('<a style="float: right; width: 100px;">Save</a>');
      savebtn.click(savefn);
      tools.append(savebtn);
    }

    // 
    var autosave = kwds.autosave;
    if (autosave>0) {
      if (autosave<5) autosave = 5; // don't make it too short
      var repeatsave = createRepeatSaveFn(id, savefn, autosave);
      setTimeout(repeatsave, autosave*1000);
    }

    var onclick = kwds.onclick;
    if (onclick != null && onclick != '') {
      div.click( function() { docmill.compile(onclick); return false; } );
    }
      
    var ret = div.lubanElement('sketchcanvas');
    if (parent) {parent.add(ret);}
    return ret;
  };
  //  object
  widgets.sketchcanvas = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  widgets.sketchcanvas.prototype = new widgets.base ();
  widgets.sketchcanvas.prototype.setAttribute = function(attrs) {
    var div = this._je;
  };

  function createRepeatSaveFn(id, savefn, interval) {
    function f() {
      var div = $('#'+id);
      if (!div) return;
      savefn();
      div.data('interval-handle', setTimeout(f, interval*1000));
    }
    $('#'+id).bind('luban-destroy', function(){
      var h = $(this).data('interval-handle');
      clearTimeout(h);
    });
    return f;
  };

  function createSaveFn(id, onsave) {
    var f = function(event) {
      var canvas = $('#'+id+' canvas');
      /*
      var ctx = canvas[0].getContext('2d');
      var data = ctx.getImageData(0,0, canvas.attr('width'), canvas.attr('height'));
      data = {'data': data.data};
      */
      var data = {'data': canvas[0].toDataURL('image/png')}; // or image/jpeg
      $('#'+id).trigger('luban-sketchcanvassave', data);
      return false;
    }
    
    return f;
  };

 })(luban, jQuery);


// End of file
