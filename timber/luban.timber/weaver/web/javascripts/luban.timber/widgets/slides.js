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
  dmp.onslides = function(slides) {
    var type = slides.luban_type;
    var factory = luban.elementFactory[type];
    var elem = factory(slides, this, this._parent);

    var contents = slides.contents;
    if (contents == null) {return elem;}

    for (var i in contents) {
      var slide = contents[i];

      this._parent = elem;
      var subelem = this.dispatch(slide);

    }

    var navdivid = slides.id + '-nav';
    var navdiv = tag("div", {id: navdivid}); elem._je.append(navdiv);
    navdiv.addClass('nav');

    if (!this.toinsert) elem.initWidget();

    // bind event handler
    return elem;
  };
  dmp.onslide = function(slide) {
    var parent = this._parent;
    var slideelem = createSlideElement(slide);
    parent.add(slideelem);

    var contents = slide.contents;
    if (contents != null) {

      for (var i in contents) {
	this._parent = slideelem;
	var subdoc = contents[i];
	if (typeof(subdoc) == 'string') {
	  slideelem._je.append(subdoc);
	} else {
	  this.dispatch(subdoc);
	}
      }

    }
    return slideelem;
  };

  // actioncompiler handlers
  var lap=luban.actioncompiler.prototype;

  // create html element from slide specification
  function createSlideHtmlElement(slide) {
    var id = slide.id;
    var div = tag('div', {id:id});
    div.addClass('luban-slide'); div.addClass('slide');

    // the image (enclosed by <a>)
    var d = {title: slide.caption};
    if (slide.url) d.href = slide.url;
    var a = tag('a', d);
    div.append(a);
    var img = tag('img', {'src': luban.configuration.images_base + '/' + slide.image});
    a.append(img);

    var caption = tag('div'); div.append(caption);
    caption.addClass('caption');
    var captionp = tag('p'); caption.append(captionp);
    captionp.text(slide.caption);

    return div;
  }
  // create luban element from slide specification
  function createSlideElement(slide) {
    var e = createSlideHtmlElement(slide);
    return e.lubanElement('slide');
  }

  // slides
  //  factory
  ef.slides = function(kwds, docmill, parent) {
    var id = kwds.id;
    var div = tag('div', {id: id});
    div.addClass('luban-slides');
    var ret= div.lubanElement('slides');

    // save some data
    div.data('timeout', kwds.timeout);

    if (parent) {parent.add(ret);}
    return ret;
  };
  //  object
  widgets.slides = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  widgets.slides.prototype = new widgets.base ();

  // turn a plain html element tree to a "slides" widget
  widgets.slides.prototype.initWidget = function() {
      this._je.cycle({
	'fx': 'scrollRight' // 'fade'
	,'slideExpr': '.luban-slide'
	,'pager': this._je.children('.nav')
	,pause: 1
	,timeout: this._je.data('timeout')
	});
  };

  // slide
  ef.slide = function(kwds, docmill, parent) {
    return ret;
  };
  //  object
  widgets.slide = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  widgets.slide.prototype = new widgets.base ();

 })(luban, jQuery);


// End of file
