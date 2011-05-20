#!/usr/bin/env python


import web

urls = (
    '/login', 'login',
    )


import luban.content as lc


class login:


    def __init__(self):
        from luban.weaver.web import create as createWeaver
        self.weaver = createWeaver(
            controller_url = 'login',
            statichtmlbase='static')
        return


    def welcome(self):
        # the overall frame
        frame = lc.frame(title='my application')
        # a document in the frame
        doc = frame.document(title='Please login')
        # form
        form = doc.form(title='form')
        username = form.text(label='Username', name='username', id='username-input')
        password = form.password(label='Password', name='password', id='password-input')
        submit = form.submitbutton(label='submit')
        # when submit, post form data with addtional parameter routine='onsubmit'
        form.onsubmit = lc.select(element=form).submit(routine='onsubmit')
        # weave to produce html
        return self.weaver.weave(frame)


    def onsubmit(self, input):
        # inputs
        username = input['actor.username']
        password = input['actor.password']
        # gather errors
        errors = {}
        # username
        if not username:
            errors['username'] = 'username can not be empty'            
        elif username not in users:
            errors['username'] = 'username not found'
        # password
        if not password:
            errors['password'] = 'password can not be empty'
        # if there are errors, show them
        if errors:
            actions = [lc.select(id='%s-input'%k).formfield(
                'showError', message=v) for k,v in errors.iteritems()]
        else:
            authorized = authenticate(username, password)
            if authorized:
                # if user is authorized, welcome him/her
                doc = lc.document(title='Welcome')
                actions = lc.select(id='').replaceContent(doc)
            else:
                # otherwise, show error
                actions = lc.select(id='password-input').formfield(
                    'showError', message='wrong password')
        # render to json
        return self.weaver.weave(actions)


    def GET(self):
        return self.welcome()

    
    def POST(self):
        i = web.input()
        # dispatch according to routine
        routine = i.pop('routine')
        routine = getattr(self, routine)
        return routine(i)


# just a demo
users = {
    'demo': 'demo'
    }
def authenticate(username, password):
    return password == users[username]


app = web.application(urls, globals())


if __name__ == '__main__': app.run()
