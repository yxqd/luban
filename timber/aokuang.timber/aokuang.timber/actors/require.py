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


def emailform(context=None):
    "frame to solicit from user his email"
    frame = luban.e.frame(title='input email')
    form = frame.form(title='email')
    form.text(label='email', name='email')
    form.submitbutton(label='submit')
    form.onsubmit = luban.a.load(
        actor='require', routine='onemailsubmission', 
        kwds=luban.event.data,
        context = context,
        )
    return frame

def check_email(*args, **kwds):
    "a simple test that check if user email is available"
    email = luban.session.get('email')
    return not email

email_requirement = luban.decorators.PortalRequirement()
email_requirement.check_requirement = check_email
email_requirement.fullfill_requirement = emailform


from luban.controller.Actor import Actor as base
class Actor(base):

    expose = 1

    def onemailsubmission(self, email=None, context=None, **kwds):
        """handle email submission and establish "credential"
        in this simple case, that is just the email
        """
        luban.session['email'] = email
        # context was set by the "require" decorator
        # below on the "showinfo" method
        context = luban.session.pop(context)
        onsuccess = context['onsuccess']
        return onsuccess
    

    @luban.decorators.require(
        # this is the requirement that before the real functinality can be invoked
        email_requirement
        )
    def showinfo(self, *args, **kwds):
        "real functionality after 'authentication' is done"
        email = luban.session['email']
        frame = luban.e.frame(title='aokuang.timber: requirement')
        frame.paragraph(text = 'email: %s' % email)
        return frame
        
    
# End of file 

