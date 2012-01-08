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

# login form
def createVisual(
    form=None, actor="login", routine='onsubmit',
    context=None,
    ):
    if not context:
        raise ValueError("must provide context id")
    
    form = form or luban.e.form(title='login')
    username = form.text(name='username', label='Username')
    password = form.password(name='password', label='Password')
    submit = form.submitbutton(label='login')
    form.onsubmit = luban.a.load(
        actor=actor, routine=routine,
        kwds = luban.event.data,
        context = context,
        )
    return form


class Factory:

    form = None
    actor = 'login',
    routine = 'onsubmit'

    def __call__(self, context):
        return createVisual(
            form = form,
            actor = actor, routine = routine,
            context = context)


# End of file 
