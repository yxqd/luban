// -*- JavaScript -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                       (C) 2008-2010 All Rights Reserved  
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
  dmp.onchart = dmp._onElement;


  //  factory
  ef.chart = function(kwds, docmill, parent) {
    var div = tag('div', {'id': kwds.id});
    div.addClass('luban-chart');
    
    var kls = kwds.Class;
    if (kls) {div.addClass(kls);}
    
    var ret = div.lubanElement('chart');
    if (parent) {parent.add(ret);}

    var captiondiv = tag('div'); div.append(captiondiv);
    captiondiv.addClass('caption');
    if (kwds.caption) {
      captiondiv.text(kwds.caption);
    }

    var canvasid = kwds.id+'-canvas';
    var canvas = tag('div', {id: canvasid});
    canvas.addClass('luban-chart-canvas');
    div.append(canvas);

    var opts = {
    width: canvas.width()-30,
    height: canvas.height()-25,
    xmin: kwds.xrange[0],
    xmax: kwds.xrange[1],
    ymin: kwds.yrange[0],
    ymax: kwds.yrange[1],
    zmin: kwds.zrange[0],
    zmax: kwds.zrange[1]
    };
    var curve0 = kwds.curves[0];
    var data = pv.range(curve0.x.length).map(function(x) {
	return {x: curve0.x[x], y: curve0.y[x], z: curve0.z[x]};
      });
    createPlotPanel(canvasid, data, opts);
    
    return ret;
  };
  //  object
  widgets.chart = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  widgets.chart.prototype = new widgets.base ();
  


  function createPlotPanel(canvas, data, opts) {

    /* Sizing and scales. */
    var w = opts.width,
      h = opts.height,
      x = pv.Scale.linear(opts.xmin, opts.xmax).range(0, w),
      y = pv.Scale.linear(opts.ymin, opts.ymax).range(0, h);

    var maxzmag = Math.max(Math.abs(opts.zmin), Math.abs(opts.zmax));
    
    /* The root panel. */
    var vis = new pv.Panel()
      .canvas(canvas)
      .width(w)
      .height(h)
      .bottom(20)
      .left(20)
      .right(10)
      .top(5);
    
    /* Y-axis and ticks. */
    vis.add(pv.Rule)
      .data(y.ticks())
      .bottom(y)
      .strokeStyle(function(d) d ? "#eee" : "#000")
      .anchor("left").add(pv.Label)
      .visible(function(d) d > opts.ymin && d < opts.ymax)
      .text(y.tickFormat);

    /* X-axis and ticks. */
    vis.add(pv.Rule)
      .data(x.ticks())
      .left(x)
      .strokeStyle(function(d) d ? "#eee" : "#000")
      .anchor("bottom").add(pv.Label)
      .visible(function(d) d > opts.xmin && d < opts.xmax)
      .text(x.tickFormat);

    /* The dot plot! */
    vis.add(pv.Panel)
      .data(data)
      .add(pv.Dot)
      .left(function(d) x(d.x))
      .bottom(function(d) y(d.y))
      //.strokeStyle(function(d) c(d.z))
      .strokeStyle(function(d) "brown")
      .fillStyle(function() this.strokeStyle().alpha(.2))
      //.size(function(d) Math.abs(d.z)/maxzmag*20+1)
      .radius(function(d) y(Math.abs(d.z)) + 1)
      .title(function(d) d.z.toFixed(1));
    vis.render();
  }

 })(luban, jQuery);

// End of file
