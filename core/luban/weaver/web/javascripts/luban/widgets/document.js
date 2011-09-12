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

  // declare temp local helper funcs
  var createSkeleton;

  // aliases
  var ef = luban.elementFactory;
  var widgets = luban.widgets;
  var tag = luban.utils.tag;

  
  // documentmill handler
  var dmp = luban.documentmill.prototype;
  dmp.ondocument = dmp._onContainer;
  
  
  // document
  ef.document = function (kwds, docmill, parent) {
    var id = kwds.id;
    
    // create the overall container
    var div = tag('div', {'id': id});

    //
    var lubanelem = div.lubanElement('document');
    if (parent) { parent.add(lubanelem); }
    
    return createSkeleton(kwds, docmill, parent, div);
  };

  // this is basically the factory of luban document,
  // it creates the title section and body section of the document
  // given the container div.
  createSkeleton = function(kwds, docmill, parent, div) {
    var ret = div.lubanElement('document');
    
    var Class = kwds.Class;

    // keep the args that create this document. maybe should make this universal
    ret._setCtorArgs(kwds);
    
    // 
    div.addClass(Class);
    div.addClass('luban-document');

    // now create me
    // title
    var title = ret._createTitle(kwds);
    div.append(title);

    // body
    var body = ret._createBody(kwds);
    div.append(body);

    // events
    var onclick = kwds.onclick;
    if (onclick) 
      {ret.jqueryelem.click( function() { docmill.compile(onclick); return false; } );}

    //
    return ret;
  };

  widgets.document = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  widgets.document.prototype = new widgets.base ();
  widgets.document.prototype.title_class = 'luban-document-title';  
  widgets.document.prototype.title_text_class = 'luban-document-title-text';
  widgets.document.prototype.body_class = 'luban-document-body';
  widgets.document.prototype.getTitleText = function() {
    return this._getTitleTextContainer().text();
  };
  widgets.document.prototype.add = function (subelem) {
    var t;
    if (typeof(subelem) == 'string') {
      t = subelem;
    } else {
      t = subelem.jqueryelem;
    }
    var body = this._getBody();
    body.append(t);
    
  };
  widgets.document.prototype.empty = function() {
    this.broadcastEvent('destroy');
    this._getBody().empty();
  };
  widgets.document.prototype.setAttribute = function(attrs) {
    var div = this._je;
    var ctorargs = this._getCtorArgs();
    
    // title
    var title = attrs.title;
    if (title!=null) {
      var titlecontainer = this._getTitleTextContainer();
      if (title) {
	titlecontainer.text(title).show();
      } else {
	titlecontainer.text(title).hide();
      }
      // make sure saved ctor args is up to date
      this._getCtorArgs().title = title;
    }

    // Class
    var Class = attrs.Class;
    if (Class) {
      div.removeClass();
      div.addClass(Class);
    }

  };

  // private methods
  widgets.document.prototype._createBody = function(opts) {
    var div = tag('div');
    div.addClass(this.body_class);
    return div;
  };
  widgets.document.prototype._getBody = function () {
    return this._je.children('.'+this.body_class);
  };
  widgets.document.prototype._createTitle = function(opts) {
    // h1
    var h1 = tag('h1');
    var title = opts.title;
    if (title) {
      h1.text(title);
    } else {
      h1.hide();
    }
    h1.addClass(this.title_text_class);

    titlediv = h1;

    titlediv.addClass(this.title_class);

    return titlediv;
  };
  widgets.document.prototype._getTitleSection = function () {
    return this._je.children('.'+this.title_class);
  };
  widgets.document.prototype._getTitleTextContainer = function () {
    var s = this._getTitleSection();
    return s;
  };
  // ctor args
  widgets.document.prototype._getCtorArgs = function() {
    var div = this._je;
    return div.data('luban-element-ctor-args');
  };
  widgets.document.prototype._setCtorArgs = function(args) {
    var div = this._je;
    div.data('luban-element-ctor-args', args);
  };

 })(luban, jQuery);


// End of file
