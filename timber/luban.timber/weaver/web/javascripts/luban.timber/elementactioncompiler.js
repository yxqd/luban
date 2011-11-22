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

    'onelementsetattribute': function(action) {
      var e = action.element;
      var element = this.dispatch(e);

      var params = this._compilekwdargs(action.attrs);
      // set id
      var id = params.id;
      if (id!=null) {element.setID(id);}

      return element.setAttribute(params);
    },

    'onelementgetattribute': function(action) {
      var e = action.element;
      var element = this.dispatch(e);
      var name = action.name;

      return element.getAttribute(name);
    },

    'oninsertbeforeelement': function(action) {
      var e = action.element;
      var element = this.dispatch(e);

      var parent = element.getParent();

      var newdoc = action.newelement;
      var newelementrendered = this.docmill.render(newdoc, parent);

      newelementrendered._je.insertBefore(element._je);

      element.jqueryelem.trigger('resize');
    },

    'oninsertafterelement': function(action) {
      var e = action.element;
      var element = this.dispatch(e);

      var parent = element.getParent();

      var newdoc = action.newelement;
      var newelementrendered = this.docmill.render(newdoc, parent);

      newelementrendered._je.insertAfter(element._je);

      element._je.trigger('resize');
    },

    'onreplaceelement': function(action) {
      var e = action.element;
      var element = this.dispatch(e);
      var newdoc = action.newelement;

      // if element is the root (frame), special treatment is needed
      if (element.type() === 'frame')
	return element.replaceBy(newdoc, this.docmill);

      var parent = element.getParent();
      var next = element._je.next();
      element.destroy();

      var newelementrendered = this.docmill.render(newdoc, parent);

      next.before(newelementrendered._je);
    },

    'onremovecontent': function(action) {
      var e = action.element;
      var element = this.dispatch(e);
      element.empty();
    },

    'onappendelement': function(action) {
      var container = this.dispatch(action.element);
      this.docmill.render(action.newelement, container);
    },

    'onhideelement': function(action) {
      var element = this.dispatch(action.element);
      element.hide();
    },

    'onshowelement': function(action) {
      var element = this.dispatch(action.element);
      element.show();
    },

    // XXX: the following comes from 0.2 and needs migration
    'onsimpleaction': function(action) {
      var name = action.actionname;
      var method = 'on'+name.toLowerCase();
      return eval('this.'+method+'(action.params)');
    },

    'onsimpleelementaction': function(action) {
      var element = action.element;
      element = this.dispatch(element);
      switch(action.actionname) {

      case 'find':
	return element.find(action.params.name, action.params.type);

      case 'findDescendentIDs':
	return element.findDescendentIDs(action.params);

      case 'disable':
	return element.disable();

      case 'enable':
	return element.enable();

      case 'destroy':
	return element.destroy();

      case 'focus':
	return element.focus();

      case 'addClass':
	return element.addClass(action.params.Class);

      case 'removeClass':
	return element.removeClass(action.params.Class);

      default:
	var etype = element.type();
	var method = 'on'+etype+action.actionname;
	method = method.toLowerCase();
	return eval('this.'+method+'(action);');
      }
    }

  };

  $.extend(luban.actioncompiler.prototype, actioncompiler_ext);

 })(luban, jQuery);


// End of file
