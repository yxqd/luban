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

    #
    regformid = "registration-form"

    # actor class
    from luban.controller.Actor import Actor as base
    class Actor(base):

        @luban.decorators.formprocesser(regformid)
        def onsubmit(
            self,
            username:luban.decorators.notemptystr=None,
            password:luban.decorators.notemptystr=None,
            password2:luban.decorators.notemptystr=None,
            firstname: luban.decorators.str=None,
            lastname: luban.decorators.str=None,
            email: luban.decorators.email=None,
            context:luban.decorators.notemptystr=None,
            **kwds
            ):

            select_form = luban.a.select(id=regformid, type='form')
            clear_form_errs = select_form.clearErrors()
            
            if password2 != password:
                showerr = select_form\
                            .find(name='password2', type='formfield')\
                            .showError(message='You may have mistyped your password')
                return [clear_form_errs, showerr]
            
            db = self.controller.db

            # first make sure email is unique
            qemail = db.query(User).filter_by(email=email)
            if qemail.count() > 0:
                showerr = select_form\
                            .find(name='email', type='formfield')\
                            .showError(message='email already registered')
                return [clear_form_errs, showerr]

            # make sure username is not 
            qusername = db.query(User).filter_by(username=username)
            if qusername.count() > 0:
                showerr = select_form\
                            .find(name='username', type='formfield')\
                            .showError(message='username already exists')
                return [clear_form_errs, showerr]
            
            user = User()
            user.username = username
            user.password = hashfunc(password)
            user.email = email
            user.firstname = firstname
            user.lastname = lastname
            
            db.add(user)
            db.commit()

            context = luban.session.pop(context)
            onsuccess = context['onsuccess']
            return onsuccess

        pass # end of Actor
    return Actor



class Factory:

    # customization done by overiding the following
    hashfunc = None

    
    def __call__(self):
        return createActor(hashfunc=self.hashfunc)

factory = Factory()

# End of file 
