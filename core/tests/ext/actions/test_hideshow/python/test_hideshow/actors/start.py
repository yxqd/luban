
import luban
from luban.controller.Actor import Actor as base

class Actor(base):

    expose = 1

    def default(self):
        frame = luban.e.frame(title="test hideshow extension")
        container = frame.document(title="hide/show")
        
        doc = container.document(
            title = 'the document to show/hide', 
            id=luban.uuid())
        
        b1 = container.button(label = 'click to hide')
        b1.onclick = luban.a.select(element = doc).hide(speed='slow')
        
        b2 = container.button(label = 'click to show')
        b2.onclick = luban.a.select(element = doc).show(speed='slow')
        
        return luban.a.establishInterface(frame)

