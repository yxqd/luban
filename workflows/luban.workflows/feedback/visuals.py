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
    
    
    def dialog(self, context=None):
        dialog = luban.e.dialog(
            title="Send feedback", id='feedback-dialog', autoopen=True)
        dialog.onclose = luban.a.select(element=dialog).destroy()
        form = self.form(context=context)
        dialog.append(form)
        return dialog


    def form(self, context=None):
        email = luban.session.get('email')
        if not email:
            raise RuntimeError("this form requires user email in session data")
        
        form = luban.e.form(id='feedback-form', Class='small-fields')

        text = (
            "Please let us know if you found any bugs in this interface, "
            "or if you have any suggestions/comments. "
            "Your inputs are much appreciated! "
            )
        form.paragraph(Class='hint', text=text)

        form.textarea(name='message', label = '')

        submitbutton = form.submitbutton(
            label='Submit', id='submit-button',
            Class=['bigbutton'])
        form.onsubmit = luban.a.load(
            'feedback',
            'onSubmit',
            kwds = luban.event.data,
            context = context,
            )

        return form


factory = Factory()


# End of file 
