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


def createActor(hashfunc=None, db=None, User=None):

    if hashfunc is None:
        import hashlib
        hashfunc = lambda p: hashlib.md5(p.encode()).hexdigest()
        
    from luban.controller.Actor import Actor as base
    class Actor(base):

        @luban.decorators.formprocesser('login')
        def onsubmit(
            self,
            username:luban.decorators.notemptystr=None,
            password:luban.decorators.notemptystr=None,
            context:luban.decorators.notemptystr=None,
            ):

            q = db.query(User).filter_by(username=username)
            if q.count() == 0:
                actions = [luban.a.select(id='login').clearErrors()]
                showerror = luban.a.select(id='login')\
                            .find(name='username', type='formfield')\
                            .showError(message='username does not exist')
                actions.append(showerror)
                return actions
                               
            user = q.one()
            
            hashed = hashfunc(password)

            if user.password == hashed
            
            return luban.session[context]['onsuccess']

        pass

    return Actor



class Factory:

    # customization done by overiding the following
    hashfunc = None
    db = None
    User = None

    
    def __call__(self):
        return createActor(hashfunc=self.hashfunc, db=self.db, User=self.User)


# End of file 
