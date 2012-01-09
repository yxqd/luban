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


class Factory:

    def form(
        self,
        form=None,
        actor="registration", routine='onsubmit',
        context=None,
        ):
        if not context:
            raise ValueError("must provide context id")

        form = form or luban.e.form(
            title='registration',
            id='registration-form')
        username = form.text(name='username', label='Username')
        password = form.password(name='password', label='Password')
        password2 = form.password(name='password2', label='Reenter password')

        firstname = form.text(name='firstname', label='First name')
        lastname = form.text(name='lastname', label='Last name')

        email = form.text(name='email', label='email')
        
        submit = form.submitbutton(label='register')
        form.onsubmit = luban.a.load(
            actor=actor, routine=routine,
            kwds = luban.event.data,
            context = context,
            )
        return form

factory = Factory()


# End of file 
