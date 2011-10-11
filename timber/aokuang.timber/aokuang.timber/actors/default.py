# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import luban


from luban.controller.Actor import Actor as base
class Actor(base):

    expose = 1

    
    def default(self):
        return self.frame()
    

    def frame(self, **kwds):
        import luban
        frame = luban.e.frame(title="aokuang: luban API demo")
        sp = frame.splitter(orientation='horizontal')
        left = sp.section(name='left', id='menu-container')
        right = sp.section(name='right', id='demo-container')
        
        left.append(self.createMenu())
        
        doc = right.document(title = "Luban API demo")
        doc.paragraph(text="Please choose an item from the left")
        return frame


    def createMenu(self, **kwds):
        doc = luban.e.document()
        accordion = doc.accordion()
        for category, items in menu:
            section = accordion.section(label=category)
            portlet = section.portlet()
            for i, item in enumerate(items):
                portletitem = portlet.item(label=item)
                portletitem.id = id(portletitem)
                newcontent = luban.a.load(
                    actor = self.name.replace('default', item),
                    routine='createInterface',
                    )
                portletitem.onselect =  luban.a.select(id="demo-container")\
                    .replaceContent(newcontent=newcontent)

                # when changing category, 
                # select the first item
                if i==0:
                    section.onselect = luban.a.select(element=portletitem)\
                        .select()
                    
                continue
            
            continue
        return doc
    

# list of items in aokuang.core


menu = [
    ('actions',
     ['loading',
      'alert',
      ]),
    
    ('basic widgets', 
     ['document',
      'paragraph',
      'button',
      'image',
      'elementbase', 
      ]),

    ('form and form fields',
     ['form',
      'formtextfield',
      'formselectorfield',
      'formradiobox',
      'formcheckbox',
      'formfield_common',
      ]),

    ('menu-like',
     ['portlet',
      'toolbar',
      ]),
    
    ('organizers',
     ['splitter',
      'grid',
      'accordion',
      'tabs',
      ]),
    
    ('documents',
     ['htmldocument',
      'restructuredtextdocument',
      ]),
    
    ('misc',
     ['codeviewer',
      'uploader',
      'slides',
      'bulletinboard',
      ]),
    ]


# End of file 

