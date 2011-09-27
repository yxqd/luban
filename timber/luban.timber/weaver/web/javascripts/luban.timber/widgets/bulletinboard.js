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
  dmp.onbulletinboard = dmp._onContainer;
  dmp.onbulletinboardannouncement = dmp._onElement;


  // actioncompiler handlers
  var lap=luban.actioncompiler.prototype;


  // bulletinboard
  //  factory
  ef.bulletinboard = function(kwds, docmill, parent) {
    var id = kwds.id;
    var containerdiv = tag('div', {id: id});
    containerdiv.addClass('luban-bulletinboard');

    var title = kwds.title;
    if (title != null && title != '') {
      var h3 = tag('h3');
      h3.addClass('luban-bulletinboard-title');
      h3.text(title);
      containerdiv.append(h3);
    }

    var bodydiv = tag('div'); containerdiv.append(bodydiv);
    bodydiv.addClass('luban-bulletinboard-body');

    var ret= containerdiv.lubanElement('bulletinboard');
    if (parent) {parent.add(ret);}
    return ret;
  };
  //  object
  widgets.bulletinboard = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  widgets.bulletinboard.prototype = new widgets.base ();
  widgets.bulletinboard.prototype.add = function (subelem) {
    var container = this.jqueryelem;
    var body = container.children('div.luban-bulletinboard-body');
    body.append(subelem.jqueryelem);
  };
  widgets.bulletinboard.prototype.setAttribute = function(attrs) {
    var je = this._je;

    var titlediv = je.children('.luban-bulletinboard-title');
    var title = attrs.title;
    if (title != null) {
      if (!title) {titlediv.remove();}
      else {
	if (titlediv.length===0) {
	  var h3 = tag('h3');
	  h3.addClass('luban-bulletinboard-title');
	  je.children('div.luban-bulletinboard-body').before(h3);
	  titlediv = h3;
	}
	titlediv.text(title);
      }
    }
  };


  // bulletinboardannouncement
  ef.bulletinboardannouncement = function(kwds, docmill, parent) {
    var id = kwds.id;
    var containerdiv = tag('div', {'id': id});
    containerdiv.addClass('luban-bulletinboardannouncement');

    var title = tag('h5');
    title.addClass('luban-bulletinboardannouncement-title');
    containerdiv.append(title);
    if (kwds.title) title.text(kwds.title);

    // icon???

    // date
    var date = tag('div');
    date.addClass("luban-bulletinboardannouncement-date");
    containerdiv.append(date);
    if (kwds.date) date.html("<b>Date: </b>" + kwds.date);

    // time
    var time = tag('div');
    time.addClass("luban-bulletinboardannouncement-time");
    containerdiv.append(time);
    if (kwds.time) time.html("<b>Time: </b>" + kwds.time);

    // place
    var place = tag('div');
    place.addClass("luban-bulletinboardannouncement-place");
    containerdiv.append(place);
    if (kwds.place) place.html("<b>Place: </b>" + kwds.place);

    // authorlist
    var authorlist = tag('div');
    authorlist.addClass("luban-bulletinboardannouncement-authorlist");
    containerdiv.append(authorlist);
    if (kwds.authorlist) authorlist.html("<b>By: </b>" + kwds.authorlist);

    // text
    var text = tag('div');
    text.addClass("luban-bulletinboardannouncement-text");
    containerdiv.append(text);
    if (kwds.text) text.html(kwds.text);

    // callbacks
    // click
    var onclick = kwds.onclick;
    containerdiv.click( function() {
	if (onclick)
	  {docmill.compile(onclick); return false;}
      } );
    var ret = containerdiv.lubanElement('bulletinboardannouncement');
    if (parent) {parent.add(ret);}
    return ret;
  };
  //  object
  widgets.bulletinboardannouncement = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  widgets.bulletinboardannouncement.prototype = new widgets.base ();
  widgets.bulletinboardannouncement.prototype.getParent = function() {
    // see bulletinboard.add and bulletinboard factory
    var item = this._je;
    var body = item.parent();
    var bulletinboard = body.parent();
    return bulletinboard.lubanElement();
  };
  widgets.bulletinboardannouncement.prototype.setAttribute = function(attrs) {
    throw "luban.timber/elements/bulletinboard: not implemented yet";
  };


 })(luban, jQuery);


// End of file
