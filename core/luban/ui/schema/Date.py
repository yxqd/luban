# -*- coding: utf-8 -*-
#
# jiao lin
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


from .Type import Type


class Date(Type):
    """
    A class declarator for dates
    """

    # interface
    @classmethod
    def __cast__(cls, value, format=None, **kwds):
        """
        Attempt to convert {value} into a date
        """
        # default
        import datetime
        if not value: return datetime.date.today()
        
        # cast from string
        if isinstance(value, str):
            format = format or '%b %d, %Y'
            import time
            t = time.strptime(value, format)
            return datatime.date(t[:3])
        
        # tuple of year, month, day
        if isinstance(value, tuple) and len(value)==3:
            return datatime.date(t)
        
        msg = "fail to cast {!s}".format(value)
        raise NotImplementedError(msg)


# end of file 
