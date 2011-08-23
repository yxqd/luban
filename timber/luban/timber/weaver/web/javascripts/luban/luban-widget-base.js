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
 * base of luban widgets
 * This is an extension of luban.widgets.base defined in luban-core.js
 */

// requires:
//   luban-core


(function (luban, $) {

  // luban.widgets.base extension
  var lwb_ext = {
    // find descendents by name
    'find': function (name, type) {
      var rt = this.jqueryelem;
      if (name) rt = rt.find('[luban-element-name='+name+']');
      if (type) rt = rt.find('[luban-element-type='+type+']');
      rt = rt.lubanElement();
      return rt;
    },
    // find descendents and return their ids
    'findDescendentIDs': function(params) {
      var type = params.type;
      var found = this.jqueryelem.find('[luban-element-type='+ type + ']');
      var ids = [];
      for (var i=0; i<found.length; i++) {
	ids.push($(found[i]).attr('id'));
      }
      return ids;
    },
    // retrieve data related to the specified event
    'getEventData': function (event) {
      return this.jqueryelem.data(event+'-data');
    },
    // save data related to the specified event
    'setEventData': function (event, data) {
      return this.jqueryelem.data(event+'-data', data);
    },

    // broadcast event to all my descendents
    'broadcastEvent': function(event) {
      this._je.find('[luban-element-type]').trigger(event);
    },

    // empty my content
    'empty': function (event) {
      this.broadcastEvent('destroy');
      this._je.empty();
      //throw 'widgets.base.empty:' + this.type() +' notimplementederror';
    },

    'disable': function () {
      this.jqueryelem.find('input').attr('disabled', 'disabled');
      this.jqueryelem.find('select').attr('disabled', 'disabled');
      this.jqueryelem.find('textarea').attr('disabled', 'disabled');
    },
    'enable': function () {
      this.jqueryelem.find('input').removeAttr('disabled');
      this.jqueryelem.find('select').removeAttr('disabled');
      this.jqueryelem.find('textarea').removeAttr('disabled');
    },
    'destroy': function() {
      this.broadcastEvent('destroy');
      this.jqueryelem.trigger('destroy');
      this.jqueryelem.remove();
    },
    'focus': function() {
      this.jqueryelem.focus();
    },

    // set id:
    'setID': function(id) {
      this.jqueryelem.attr('id', id);
    },

    // set tip
    'setTip': function(tip) {
      if (tip) {
	var je = this._je;
	// set attribute "title". this could conflict other use of "title" attribute
	je.attr('title', tip);
	je.tooltip({
	  showURL: false
        });
      }
    }

  };

  $.extend(luban.widgets.base.prototype, lwb_ext);

 })(luban, jQuery);


// End of file
