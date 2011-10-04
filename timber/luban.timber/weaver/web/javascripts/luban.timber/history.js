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

  // initializer extension
  luban.init.funcs.push(function () {

    $.history.init(
      function (hash) {
	if(hash) {
	  $('.luban-frame').load(hash);
	}
      }
    );

  });

  // actioncompiler extension
  var actioncompiler_ext = {

  };
  $.extend(luban.actioncompiler.prototype, actioncompiler_ext);


 })(luban, jQuery);


// End of file
