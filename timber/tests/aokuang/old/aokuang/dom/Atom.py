
class Atom:

    def __init__(self, **kwds):
        for k,v in kwds.iteritems():
            setattr(self, k, v)


    symbol = 'H'




from dsaw.model.Inventory import Inventory as InvBase
class Inventory1(InvBase):
    
    symbol = InvBase.d.str(
        name='symbol', default='H',
        validator=InvBase.v.choice(['H', 'He', 'Li', 'Be', 'B', 'C']),
        )
