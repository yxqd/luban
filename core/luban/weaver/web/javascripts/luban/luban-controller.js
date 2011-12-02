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


// controller object
C = luban.Controller = {
  'url': null, // controller's url: eg http://your.web.site/main.py
  'cookie_settings': {
    'use_cookie': false,
    'path': '/cgi-bin/', // path of cookie
    'expires': 1
  },
  'parameter_prefix': ''
};


// extend jquery
(function ($, luban) {

  // aliases
  var ef = luban.elementFactory;
  var C  = luban.Controller;
  var widgets = luban.widgets;


  // helpers declaration
  var argsStr;



  // replace the content of "this" widget
  // data: a dict
  //   html: new html content
  //   includes: paths of js scripts to include
  //   script: js script to run
  $.fn.replaceContent = function(data) {
    // clear
    $(this).empty();

    C.execUIUpdateInstructions(data);
  };


  // helper function
  // string of arguments in url
  luban.utils.argsStrInUrl = argsStr = function (args) {
    var assignments = [];
    for (var k in args) {
      var v = args[k];
      assignment = k+'='+v;
      assignments.push(assignment);
    }
    return assignments.join('&');
  };

  // prepend 'actor.' to keys
  function prependParameterPrefix(args) {
    var d = {};
    for (var k in args) {
      var k1 = C.parameter_prefix+k;
      d[k1] = String(args[k]);
    }
    return d;
  }
  C.prependParameterPrefix = prependParameterPrefix;


  // controller methods

  // call controller
  // specs
  //   actor: the name of the actor
  //   routine: the name of the routine
  //   callback: the call back function when the response of the server is received
  //   responsetype: the expected response type. default: json
  //   args: arguments for the routine
  //   kwds: the additional data to send to the server
  C.call = function (specs) {
    var actor = specs.actor;
    var routine = specs.routine;
    if (!routine) {routine='default';}
    var callback = specs.callback;
    var url = C.url;

    var responsetype = specs.responsetype;
    if (responsetype==null)
      {responsetype = 'json';}

    // call
    var args = [actor, routine];
    args = args.concat(specs.args);
    args = $.map(args, encodeURI); // encodeuri
    url += args.join('/');

    // kwd args
    var kwds = specs.kwds;
    if (kwds == null) {kwds = {};}

    // credential
    var credArgs = C.getCredentialArgs();

    // all
    var allkwdargs = $.extend({}, kwds, credArgs);

    var f = function(callback) {
      $.get(url, allkwdargs, callback, responsetype);
    };

    // for debug
    f.url = url; f.allkwdargs = allkwdargs;

    // C.runWithLoadingAlert(f, callback);
    f(callback);

    return;
  };

  // given instructions to change user interface, execute them
  C.execUIUpdateInstructions = function(data, textStatus) {
    if (data.lubanaction || data['0'] ) // array means a list of actions
      {return luban.docmill.compile(data);}
    return luban.docmill.render(data);
  };

  // load from controller and execute actions in the response
  // specs: the specification of the call
  //   actor: the name of the actor
  //   routine: the name of the routine
  //   args: the arguments for the routine
  //   kwds: a dictionary of additional parameters to send to the server
  C.load = function(specs, callback) {
    specs.callback = callback;
    var kwds = specs.kwds;
    specs.kwds = prependParameterPrefix(kwds);
    C.call(specs);
  };


 })(jQuery, luban);


// End of file
