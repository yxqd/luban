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
from ..decorators import requirements


def createActor(feedback_recipient="feedback@example.com", gmail_account=None):

    if not gmail_account:
        raise RuntimeError("must provide gmail_account")

    #
    from .._utils import email
    email.gmail_account = gmail_account
    
    from luban.controller.Actor import Actor as base
    class Actor(base):

        @luban.decorators.formprocesser(
            'feedback-form',
            )
        def onSubmit(
            self,
            message: luban.decorators.notemptystr=None,
            context = None,
            **kwds
            ):
            email = luban.session['email']
            if not email:
                raise RuntimeError("should not reach here")

            dialog = luban.e.dialog(id='in-processing-dialog', autoopen=True)
            dialog.onclose = luban.a.select(element=dialog).destroy()
            dialog.paragraph(text="Sending ... Thank you for your patience.")

            subject = 'user feedback for application'
            content = message
            dialog.oncreate = luban.a.load(
                self.name, 'sendEmail',
                subject, content,
                context = context,
                )

            return [
                luban.a.select(id='feedback-dialog').destroy(),
                luban.a.select(id='').append(newelement=dialog),
                ]


        @luban.decorators.require(requirements.email)
        def sendEmail(self, subject, content, context=None, **kwds):
            #
            sender = luban.session['email']
            
            #
            recipients = [feedback_recipient]

            #
            from .._utils.email import send
            send(subject, recipients, content, sender)

            # actions after user click ok button
            destroydialog = luban.a.select(id='in-processing-dialog').destroy()

            # thankk you and ok
            newcontent = luban.e.document(title="Thank you for your input!")
            newcontent.Class = 'horizontal-center'
            okbutton = newcontent.button(
                label='OK',
                Class = 'bigbutton',
                )
            okbutton.onclick = [destroydialog]

            context = luban.session.pop(context)
            onsuccess = context['onsuccess']
            if onsuccess: okbutton.onclick.append(onsuccess)

            return luban.a.select(id='in-processing-dialog').replaceContent(
                newcontent = newcontent)

    return Actor



class Factory:

    # customization done by overiding the following
    feedback_recipient = None
    gmail_account = None
    
    def __call__(self):
        return createActor(
            feedback_recipient = self.feedback_recipient,
            gmail_account = self.gmail_account,
            )

factory = Factory()

# End of file 
