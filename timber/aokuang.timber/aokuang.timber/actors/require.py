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


def emailform():
    frame = luban.e.frame(title='input email')
    form = frame.form(title='email')
    form.text(label='email', name='email')
    form.submitbutton(label='submit')
    form.onsubmit = luban.a.load(
        actor='require', routine='onemailsubmission', 
        kwds=luban.event.data)
    return frame
email_requirement = luban.decorators.Requirement

def check_email():
    email = luban.session.get('email')
    return not email
email_requirement.check_requirement = check_email
email_requirement.fullfill_requirement = emailform


from luban.controller.Actor import Actor as base
class Actor(base):

    expose = 1

    def onemailsubmission(self, email=None, **kwds):
        luban.session['email'] = email
        onsuccess = luban.session['onsuccess']
        return onsuccess

    @luban.decorators.require(email_requirement, luban.a.load(actor='require', routine='showinfo', replaceinterface=1))
    def showinfo(self, *args, **kwds):
        email = luban.session['email']
        frame = luban.e.frame(title='aokuang.timber: requirement')
        frame.paragraph(text = 'email: %s' % email)
        return frame
        
    
# End of file 

