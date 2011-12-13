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
        frame = self.frame()
        return luban.a.establishInterface(frame)


    def frame(self, **kwds):
        import luban
        frame = luban.e.frame(title="aokuang: luban API demo")
        sp = frame.splitter(orientation='horizontal')
        left = sp.section(name='left', id='menu-container')
        right = sp.section(name='right', id='demo-container')
        left.append(self.createMenu())
        return frame


    def createMenu(self, **kwds):
        doc = luban.e.document(title="select an item from the following")
        choices = self._findChoices()
        for choice in choices:
            b = doc.button(label=choice, id=choice)
            newcontent = luban.a.load(
                actor = self.name.replace('start', choice),
                routine='createInterface',
            )
            b.onclick = luban.a.select(id="demo-container")\
                .replaceContent(newcontent=newcontent)
            continue
        return doc
    

    def _findChoices(self):
        f = __file__
        import os
        d = os.path.dirname(f)
        entries = os.listdir(d)
        choices = []
        for entry in entries:
            if entry.startswith('_'):
                continue
            path = os.path.join(d, entry)
            if os.path.isdir(path):
                choices.append(entry)
                continue
            continue
        return choices



# End of file 

