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
//    * luban-controller.js


(function(luban, $) {

  luban.actioncompiler.prototype = {
    
    'onreplacecontent': function(action) {
      var e = action.element;
      var element = this.dispatch(e);
      element.empty();
      
      var newdoc = action.newcontent;
      this.docmill.render(newdoc, element);

      element.jqueryelem.trigger('resize');
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

    'onreplaceelement': function(action) {
      var e = action.element;
      var element = this.dispatch(e);
      var newdoc = action.newelement;

      // if element is the root (frame), special treatment is needed
      if (element.type() === 'frame')
	return element.replaceBy(newdoc, this.docmill);
      
      var parent = element.getParent();

      var newelementrendered = this.docmill.render(newdoc, parent);
      
      newelementrendered._je.insertBefore(element._je);
      element.destroy();
    },

    'onremovecontent': function(action) {
      var e = action.element;
      var element = this.dispatch(e);
      element.empty();
    },

    'onappendelement': function(action) {
      var container = this.dispatch(action.container);
      this.docmill.render(action.element, container);
    },

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

      case 'show':
	return element.show();
	
      case 'hide':
	return element.hide();
	
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

      case 'setAttribute': 
	return this.onsimpleelementaction_setAttribute(action);

      case 'getAttribute': 
	return element.getAttribute(action.params.name);

      default:
	var etype = element.type();
	var method = 'on'+etype+action.actionname;
	method = method.toLowerCase();
	return eval('this.'+method+'(action);');
      }
    },

    'onsimpleelementaction_setAttribute': function(action) {

      var element = action.element;
      element = this.dispatch(element);

      var params = this._compileparams(action.params);
      // set id
      var id = params.id;
      if (id!=null) {element.setID(id);}
	
      return element.setAttribute(params);
    }

  };

 })(luban, jQuery);


// End of file
