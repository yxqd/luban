(function(luban, $) {

   // we will need to extend the "actioncompiler" of luban
   // first build an extension object
   var actioncompiler_ext = {

     'onhideelement': function(action) {
       // action is the object that contains all specifications of the action

       // ask the action compiler to compile the element selector
       var element = this.dispatch(action.element);
       // get the jquery element
       var jqe = element.jqueryelem; // the jquery element
       // speed
       var speed = action.speed;
       // use jquery to do the work
       jqe.hide(speed);
     }

     ,'onshowelement': function(action) {
       // action is the object that contains all specifications of the action

       // ask the action compiler to compile the element selector
       var element = this.dispatch(action.element);
       // get the jquery element
       var jqe = element.jqueryelem; // the jquery element
       // speed
       var speed = action.speed;
       // use jquery to do the work
       jqe.show(speed);
     }

   };
   // and merge it into luban actioncompiler
   $.extend(luban.actioncompiler.prototype, actioncompiler_ext);

 })(luban, jQuery);

