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
        return frame


    def createMenu(self, **kwds):
        doc = luban.e.document()
        accordion = doc.accordion()
        for category, items in menu:
            section = accordion.section(label=category)
            portlet = section.portlet()
            for item in items:
                portletitem = portlet.item(label=item)
                newcontent = luban.a.load(
                    actor = self.name.replace('default', item),
                    routine='createInterface',
                    )
                portletitem.onclick =  luban.a.select(id="demo-container")\
                    .replaceContent(newcontent=newcontent)
                continue
            
            # section.onselect = 

            continue
        return doc
    

# list of items in aokuang.core
core = [
    'loading',
    ]


menu = [
    ('actions',
     ['loading',
      ]),
    
    ('basic widgets', 
     ['document',
      'paragraph',
      'button',
      'image',
      ]),

    ('menu-like',
     ['portlet',
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
      ]),
    ]


# End of file 

