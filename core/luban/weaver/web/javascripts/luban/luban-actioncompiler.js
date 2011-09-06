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
//    * luban-controller.js


(function(luban, $) {

  // aliases
  var deepCopy = luban.utils.deepCopy;
  var isArray = luban.utils.isArray;


  luban.actioncompiler = function (docmill) {
    if (docmill == null) {docmill = new luban.documentmill();}
    this.docmill = docmill;
  };

  luban.actioncompiler.prototype = {

    'compile': function(actions) {
      // ***********************************************
      // Do we really care to support a list of actions?
      // ***********************************************
      // check if it is an action of a list
      if (isArray(actions)) {
	var ret = [];
	for (var i in actions) {
	  var action = actions[i];
	  ret.push(this.compile1(action));
	}
	return ret;
      } else {
	return this.compile1(actions);
      }
    },

    'compile1': function (action) {
      if (action==null) {return;}
      if (!action.luban_type) {
	// if action does not have a "type" attribute,
	// we assume that it is not a luban action, but a normal value (str, number, etc)
	return action;
      }
      //
      action = deepCopy(action);
      var toload = this.preloader.findThingsToLoad(action);
      if (toload) {
	var self = this;
	var loading_actions = toload.loading_actions;
	var runloaded = false;
	if (loading_actions && loading_actions.length)
	  { runloaded = loading_actions[loading_actions.length-1][0] == action; }
	var callback = function (loaded) {
	  if (runloaded) {
	    self.compile(loaded);
	  } else {
	    self.compile1(action);
	  }
	};
	this.preloader.load(toload, callback);
      } else {
        return this.dispatch(action);
      }
    },

    'dispatch': function (action) {
      var type = action.luban_type;
      var code = 'this.on'+type+"(action)";
      return eval(code);
    },

    'onselectbyidandtype': function(action) {
      var id = action.id;
      if (!id) {
        // assume that no id means the frame
        return $('div.luban-frame').lubanElement();
      }
      var je = $('#'+id);
      if (je.length === 0) {
	throw "not such element: id="+id;
      }
      return je.lubanElement();
    },

    'onsimpleaction': function(action) {
      var name = action.actionname;
      var method = 'on'+name.toLowerCase();
      return eval('this.'+method+'(action.params)');
    },

    'ongetattr': function(action) {
      var entity = action.entity;
      if (entity.luban_type=='event') {
	entity = this.docmill.render(entity);
	return entity[action.name];
      }
      return null;
    },

    //
    'onalert': function(params) {
      params = this._compileparams(params);
      alert(params.message);
    },


    // helpers
    '_compileparams': function(params) {
      var ret = {};
      for (var key in params) {
	var value = params[key];
	value = this.compile1(value);
	if (value!=null) {ret[key] = value;}
      }
      return ret;
    }
  };

 })(luban, jQuery);


// End of file
