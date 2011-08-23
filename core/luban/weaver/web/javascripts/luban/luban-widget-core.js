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

/*
 * This module forms the core to make it possible for luban to extend to various
 * widgets.
 * It implements a machinary to load a widget extension and check its validity.
 *
 * Requirements for a widget
 * - A widget must be implemented in luban.widgets namespace.
 * - A documentmill handler must be implementd for this widget
 * - The widget could have a "selfcheck" method to check whether it was loaded
 *   correctly
 */


// requires:
//    * luban-core.js


(function(luban, $) {

  // aliases
  var ef = luban.elementFactory;
  var widgets = luban.widgets;
  var tag = luban.utils.tag;

  // helpers
  // check if a widget extension is loaded ok.
  // it is always attached to a "download" object with has a "widget" property
  // giving the name of the widget.
  // the check is done by checking
  //   * whether the document mill handler is defined
  //   * whether the widget factory is defined
  //   * whether the selfcheck method of the widget object passes
  function widget_extension_check() {
    var w = this.widget;

    var f=eval('luban.docmill.on'+w);
    var wc=eval('luban.widgets.'+w);
    if (f==null || wc==null) {return 1;}
    if (wc.selfcheck==null) {return null;}
    return wc.selfcheck();
  }

  //
  luban.widgets.implementationRegistry = {};
  luban.widgets.loadWidgetsImplementation = function( widgets, callback ) {
    //
    var lw = luban.widgets, lu = luban.utils;
    var jdm = new lu.jsDownloadManager();
    //
    var check = widget_extension_check;

    var pass = function() {return 0;};

    for (var i in widgets) {
      var j;

      var w= widgets[i];
      var files = lw.getWidgetLibFiles(w);

      //
      for (j in files.css) {lu.loadCSS(files.css[j]);}

      //
      var impl_js_sig = '/widgets/'+w+'.js';

      for (j in files.js) {
	var js = files.js[j], c;
	if (js.search(impl_js_sig)!=-1) {c = check;}
	else {c = pass;}
	var d = {url: js, 'check': c, widget: w};
	jdm.addDownload(d);
      }
    }
    jdm.start(callback);
  };

  luban.widgets.getWidgetLibFiles = function (widget) {
    var def_impl_js = 'luban/widgets/'+widget+'.js', found;
    var jsbase = luban.configuration.javascripts_base;

    var impl = luban.widgets.implementationRegistry[widget];
    if (!impl) {
      impl = luban.widgets.implementationRegistry[widget] = {
	'javascripts': [jsbase+'/'+def_impl_js],
	'stylesheets': []
      };
    }

    // look for default implementation file and establish the list of
    // js files to load
    var jslist=[], js;
    for (var i in impl.javascripts) {
      js = impl.javascripts[i];
      jslist.push(js);
      if (js.search('/'+widget+'.js')!=-1) {found = 1;}
    }
    // if not found load it
    if (!found) {
      js = jsbase+'/'+def_impl_js;
      jslist.push(js);
    }

    return {'js': jslist, 'css': impl.stylesheets};
  };


 })(luban, jQuery);


// End of file
