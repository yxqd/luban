.. _philosophy-indepth:

More details about luban philosophy
===================================

Many existing efforts of unifying UI programming. 
our approach is a minimalist one.
successful in building vnf.


Intuitive, responsive, and clean graphical user interface is essential for most
software applications.
Building graphical user interface is hard, however. Without extreme care, a user interface application can easily become unnecessarily complex and convoluted, and as a result, unmaintainable. Building web-based graphical user interface is even harder; a web GUI project needs developers not only know how to program with front end technologies such as html, javascript, ajax, and/or flash, but also know how to program with server side technologies such as php, and/or perl, python, and that renders management of a web UI project expensive. With the emergence of cloud computing, we will see many software packages turning to cloud and demand web or mobile-device user interfaces, while the traditional desktop user interface still has its large user base. A much simplified route of developing desktop/web/mobile-device user interface is needed. This work intends to provide an abstraction for specification of user interface, to reduce the chaos and agony in building user interface applications, to dramatically lower the barrier of creating sophisticated user interface, and to make it much easier to maintain and evolve user interface by separating specifications from implementations.

User interfaces, however many fancy effects they have, can be reduced to simple descriptive specifications of abstract user interface elements. The abstraction of user interface allows UI developers to supply only specifications, in a language-independent way, for a hierarchical construction of UI elements and also for actions to carry out when users interact with the interface (events). This abstract specification can then be rendered into various media-specific code pieces that present user interfaces to users. 

The existing prototype in opal/luban (http://luban.danse.us) demonstrates that with a simple set of UI elements, actions, and rules, full fledged web UIs can be created from specifications in simple python syntax and results in a code base that is easy to maintain and extend 
(Please watch a demo of one workflow in a web service powered by opal/luban: http://www.youtube.com/watch?v=wqy4HwkAqro&fmt=22, 
and more demos are available at http://docs.danse.us/pyre/luban/sphinx/Demos.html#demo-sites). 
UI developers only need to have a basic knowledge of python language to develop sophisticated web UI. Complexities of building/using javascript/ajax libraries and handling communications between client and server are hidden from UI developers.

The existing prototype also allows users to build one specification of user interface, and generate web AND native desktop interface. This is demonstrated in this demo http://docs.danse.us/pyre/luban/sphinx/tutorials/video/gongshuzidemo.html, 
although the desktop GUI generation implementation in the prototype is at this moment limited.



Elements
A UI element must have a name, 0 or more properties, 0 or more events, 0 or more
methods. 



In this research we propose to conduct research on the semantics of generic UI specification formally, extend our implementation to mobile-device applications and desktop applications, further reduce the complexity of UI building by providing a UI builder (prototype: http://docs.danse.us/pyre/luban/dev/sphinx/Gongshuzi.html), and provide more mechanisms for UI specification such as xml and other text-based structural documents.
