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

    C.runWithLoadingAlert(f, callback);

    return;
  };

  // run a function (which has a callback function when the function finishes)
  // with "loading ..." alert shown on the window
  C.runWithLoadingAlert = function (func, callback) {
    var callback1 = function () {
      // shut down the loading alert
      C.notifyLoadingDivToEnd(func);

      // start callback function
      callback.apply({}, arguments);
    };
    // start the loading alert
    C.notifyLoadingDivToStart(func);
    // call the function with new callback
    func(callback1);
    return;
  };

  C.notifyLoadingDivToStart = function (func) {

    var loadingdiv = C.getLoadingDiv();

    var f = function () {

      // if this loading is already finished, this function won't be triggered

      // so, if we reach here, this means the loading is not yet finished,
      // we need to remove the stored timeout, because this timeout is happening
      delete loadingdiv.data('timeouts')[func];

      // and it is the latest loading event. should take over the "loading..."
      // alert if it is running.
      if (loadingdiv.data('running')) {
	loadingdiv.data('owner', func);
	return;
      }

      // this means the loading alert is not running. we need to get it running
      // first claim the owner ship of the loading alert
      loadingdiv.data('owner', func);

      // then start the alert
      C.startLoadingAlert();

      // hack
//       var f1 = function() {C.notifyLoadingDivToEnd(func)};
//       setTimeout(f1, 5000);
    };

    // this should only start after a moment after the user click
    var timeout = setTimeout(f, 700);
    // store this timeout so that we can cancel it if the loading finished before
    // the time runs out
    loadingdiv.data('timeouts')[func] = timeout;
  };

  C.notifyLoadingDivToEnd = function (func) {
    var loadingdiv = C.getLoadingDiv();

    // if this func is the owner of the loading alert, we should stop the alert
    var owner = loadingdiv.data('owner');
    if (owner==func) {
      C.stopLoadingAlert();
      return;
    }

    // otherwise, we should clear the timeout if it is there
    var timeouts = loadingdiv.data('timeouts');
    var timeout = timeouts[func];
    if (timeout) {clearTimeout(timeout);}
    delete timeouts[func];
  };
  C.startLoadingAlert = function() {
    var loadingdiv = C.getLoadingDiv();

    loadingdiv.data('running', 1);
    var wh=$(window).height(), ww=$(window).width();
    loadingdiv.css('left', ww/2-20);
    loadingdiv.css('top', wh/2);
    loadingdiv.show();
  };
  C.stopLoadingAlert = function() {
    var loadingdiv = C.getLoadingDiv();

    // hide the visual
    loadingdiv.hide();
    loadingdiv.data('running', 0);
    loadingdiv.data('owner', null);
  };

  C.getLoadingDiv = function () {
    var id = 'luban-----loadingdiv';
    var div = $('#'+id);

    // this should not happend
    if (div.length>1) {throw "?";}

    // if not found, creat it
    if (div.length===0) {

      // create the div
      div = $('<div id="'+id+'"/>');
      //div.text('loading...');
      div.hide();

      // attach to page
      $('body').append(div);

      //
      div.data('timeouts', {});
      div.data('owner', null);
      div.data('running', 0);
    }
    return div;
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
