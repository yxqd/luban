#!/usr/bin/env python


import web

urls = (
    '/main', 'main',
    )


import luban.content as lc


class main:


    def __init__(self):
        from luban.weaver.web import create as createWeaver
        import weaver_library
        self.weaver = createWeaver(
            controller_url = 'main',
            statichtmlbase = 'static',
            library = weaver_library,
            )
        return


    def welcome(self):
        from visuals.frame import visual
        frame = visual()
        return self.weaver.weave(frame)


    def onbutton2(self, input=None):
        p = lc.paragraph(text=['new paragraph'])
        action = lc.select(id='doc1').append(p)
        return self.weaver.weave(action)


    def GET(self):
        i = web.input()
        if i: return self._handleInput()
        return self.welcome()


    def _handleInput(self):
        i = web.input()
        routine = i.pop('routine')
        routine = getattr(self, routine)
        return routine(i)


app = web.application(urls, globals())


if __name__ == '__main__': app.run()
