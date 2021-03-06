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
        actor="login", routine='onsubmit',
        context=None,
        ):
        if not context:
            raise ValueError("must provide context id")

        form = form or luban.e.form(title='login', id='login-form')
        username = form.text(name='username', label='Username')
        password = form.password(name='password', label='Password')
        submit = form.submitbutton(label='login')
        form.onsubmit = luban.a.load(
            actor=actor, routine=routine,
            kwds = luban.event.data,
            context = context,
            )
        return form

factory = Factory()


# End of file 
