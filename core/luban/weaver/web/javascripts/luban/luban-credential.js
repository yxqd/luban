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

  // credential dictionary
  luban.Controller.credential = {};

  // actioncompiler prototype
  var actioncompiler_ext = {

    //  credential
    // createCredential
    'oncredentialcreation': function(params) {
      luban.Controller.createCredential(params);
    },

    // updateCredential
    'oncredentialupdate': function(params) {
      luban.Controller.updateCredential(params);
    },

    // remove credential
    'oncredentialremoval': function(action) {
      luban.Controller.removeCredential();
    }
  };

  $.extend(luban.actioncompiler.prototype, actioncompiler_ext);

  // documentmill prototype
  var documentmill_ext = {
    'oncredential': function(credential) {
      return this._onElement(credential);
    }
  };
  $.extend(luban.documentmill.prototype, documentmill_ext);

  // aliases
  var C = luban.controller;
  var ef = luban.elementFactory;
  var widgets = luban.widgets;

  // credential factory for widgets
  ef.credential = function (kwds) {
    C.createCredential(kwds);
    // a invisible div
    var div = $('<div></div>').hide();
    return div.lubanElement('credential');
  };
  widgets.credential = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  widgets.credential.prototype = new widgets.base();

  // credential factory for controller
  C.createCredential = function (kwds) {
    C.credential = {username: kwds.username, ticket: kwds.ticket};

    // save credential to cookie as well
    var cookie_settings = C.cookie_settings;
    if (cookie_settings.use_cookie) {
      try {
	$.cookie('credential.username', kwds.username, cookie_settings);
	$.cookie('credential.ticket', kwds.ticket, cookie_settings);
      } catch (e) {
	// cookie error
      }
    }
  };
  //
  C.updateCredential = C.createCredential;
  C.removeCredential = function() {
    C.credential = {};
    var cookie_settings = C.cookie_settings;
    if (cookie_settings.use_cookie) {
      try {
	$.cookie('credential.username', null, cookie_settings);
	$.cookie('credential.ticket', null, cookie_settings);
      } catch (e) {
	// cookie error
      }
    }
  };
  // create the credentail data to be send to the server
  C.getCredentialArgs = function() {
    var credential = C.credential;
    var username, ticket;
    if (!credential || !credential.username) {
      // try cookie
      //   if cookie is forbidden, just quit
      if (!C.cookie_settings.use_cookie) {return {};}
      //
      try {
	username = $.cookie('credential.username');
	ticket = $.cookie('credential.ticket');
      } catch (e) {
	// no way to get cookie
      }
      if (!username || !ticket)
	{ return {}; }
      credential.username = username;
      credential.ticket = ticket;
    }

    var ret = {};
    username = credential.username;
    if (username) {ret['sentry.username'] = username;}

    ticket = credential.ticket;
    if (ticket) {ret['sentry.ticket'] = ticket;}

    return ret;
  };

 })(luban, jQuery);


// End of file
