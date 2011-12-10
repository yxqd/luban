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


// history, back button.
// requires:
//    * jquery.history.js
//    * luban-core.js
//    * luban-controller.js


(function(luban, $) {

  // extension of luban.init
  var hinit = function () {

    $.history.init(
      function (hash, init) {
	if(hash) {
	  var url = luban.Controller.url + hash.slice(1, hash.length);

	  // to tell the handler to return an action to replace frame
	  if (url.indexOf('?') == -1) url += '?';
	  else url += '&';
	  url += 'returntype=replaceinterface';

	  if (init) {
	    luban.init.frame = null;
	    var frame = {
	      luban_type: "frame"
	      ,lubanelement: true
	      ,title: ''
	    };
	    luban.docmill.render(frame);
	  }
	  var args = {};
	  var callback = function (data){
	    luban.docmill.compile(data);
	  };
	  var restype = "json";
	  var ret = $.get(url, args, callback, restype);
	} else {
	  if (!init) {
	    var w = window;
	    w.location = w.location.href;
	  }
	}
      }
      /* , {
	unescape: "/?&.="
       }
       */
    );

  };
  luban.init.funcs = [hinit].concat(luban.init.funcs);

  // actioncompiler extension
  var actioncompiler_ext = {
    'onsetrecoverer': function (action) {
      var args = [action.actor, action.routine];
      args = args.concat(action.args);

      var hash = '!' + args.join('/');

      var kwdargs = action.params;
      var kargstr = luban.utils.argsStrInUrl(kwdargs);
      if (kargstr) hash += '?' + kargstr;

      $.history.add(hash);

      var url = luban.Controller.url + hash;
      // google analytics
      if (window._gaq!=undefined) _gaq.push(['_trackPageview', url]);
      // statcounter
      if (window.sc_tracking_url!=undefined) {
        url = sc_tracking_url + "&u=" + escape(url);
        var img = new Image(0,0); img.src = url;
      }
    }
  };
  $.extend(luban.actioncompiler.prototype, actioncompiler_ext);


 })(luban, jQuery);


// End of file
