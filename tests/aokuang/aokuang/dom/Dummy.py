

class Dummy(object):

    
    def __init__(self, **kwds):
        for k, v in kwds.iteritems():
            setattr(self, k, v)
        return

    s = 'str'
    x = 3.0
    i = 1
    b = True
    vec = [1.,2.,3.]
    mat = [ [1.,0.,0,2],
            [0,1,0,0],
            [0,0,1,0],]

    # boolean array: still need to think if this is really necessary
    boolarr = [True, False, True]




from dsaw.model.Inventory import Inventory as InvBase
class Inventory1(InvBase):

    s = InvBase.d.str(name='s')
    x = InvBase.d.float(name='x')
    i = InvBase.d.int(name='i')
    b = InvBase.d.bool(name='b', default=True)
    vec = InvBase.d.array(
        name='vec', elementtype='float', shape=None,
        )
    mat = InvBase.d.array(
        name='mat', elementtype='float', shape=(3,4),
        elementvalidator=InvBase.v.nonnegative,
        )
    boolarr = InvBase.d.array(
        name='boolarr', elementtype='bool', shape=None,
        )
