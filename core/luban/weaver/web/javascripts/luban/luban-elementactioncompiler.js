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
//    * luban-actioncompiler.js


(function(luban, $) {

  // actioncompiler extension
  var actioncompiler_ext = {

    'onreplacecontent': function(action) {
      var e = action.element;
      var element = this.dispatch(e);

      element.empty();

      var newdoc = action.newcontent;
      this.docmill.render(newdoc, element);

      element.jqueryelem.trigger('resize');
    }

    ,'onaddclass': function(action) {
      var e = action.element;
      var element = this.dispatch(e);

      element.addClass(action.cls);
      
    }

    ,'onremoveclass': function(action) {
      var e = action.element;
      var element = this.dispatch(e);

      element.removeClass(action.cls);
      
    }

  };

  $.extend(luban.actioncompiler.prototype, actioncompiler_ext);

 })(luban, jQuery);


// End of file
