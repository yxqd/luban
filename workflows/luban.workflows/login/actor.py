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


def createActor(hashfunc=None):

    if hashfunc is None:
        import hashlib
        hashfunc = lambda p: hashlib.md5(p.encode()).hexdigest()

    # get models
    from ..models import model_registry
    User = model_registry.User

    # actor class
    from luban.controller.Actor import Actor as base
    class Actor(base):

        @luban.decorators.formprocesser('login-form')
        def onsubmit(
            self,
            username:luban.decorators.notemptystr=None,
            password:luban.decorators.notemptystr=None,
            context:luban.decorators.notemptystr=None,
            **kwds
            ):
            db = self.controller.db
            q = db.query(User).filter_by(username=username)
            select_form = luban.a.select(id='login-form', type='form')
            if q.count() == 0:
                actions = [select_form.clearErrors()]
                showerror = select_form\
                            .find(name='username', type='formfield')\
                            .showError(message='username does not exist')
                actions.append(showerror)
                return actions
                               
            user = q.one()
            
            hashed = hashfunc(password)

            if user.password == hashed:
                return luban.session[context]['onsuccess']

            actions = [select_form.clearErrors()]
            showerror = select_form\
                        .find(name='password', type='formfield')\
                        .showError(message='incorrect password')
            actions.append(showerror)
            return actions

        pass

    return Actor



class Factory:

    # customization done by overiding the following
    hashfunc = None

    
    def __call__(self):
        return createActor(hashfunc=self.hashfunc)

factory = Factory()

# End of file 
