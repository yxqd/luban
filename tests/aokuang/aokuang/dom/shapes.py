
class AbstractShape: pass


class Box(AbstractShape):

    x = y = z = 1.0

    def __str__(self):
        return 'box(x=%s, y=%s, z=%s)' % (self.x,self.y,self.z)


class Cylinder(AbstractShape):

    r = h = 1.0
    
    def __str__(self):
        return 'cylinder(r=%s, h=%s)' % (self.r,self.h)


    def customizeLubanObjectDrawer(self, drawer):
        drawer.mold.sequence = ['r', 'h']
        

all = [Box, Cylinder]
