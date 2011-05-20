
class ClientComputer:

    '''the client computer that can has browser(s) that can connect to the site

    it is actually a selenium server (so we can use selenium to control
    the browser)
    '''

    def __init__(self, ip, port, os):
        self.os = os
        self.ip = ip
        self.port = port
        return



class Client:

    'a client is a browser on a client computer'

    def __init__(self, computer, browser):
        self.computer = computer
        self.browser = browser
        return


    def __getattr__(self, key):
        return getattr(self.computer, key)

    
    def __str__(self):
        return '%s client (%s:%s): browser=%s' % (
            self.os, self.ip, self.port, self.browser)



class Server:

    '''the web application server information.

    this includes the hostname of the webserver, and the mapping of
    application name to application address
    '''

    def __init__(self, host, appmap):
        self.host = host
        self.appmap = appmap
        return


class Fixture:

    'a test fixture that has a computer with a bunch of browsers, and a target web server'
    
    def __init__(self, computer, browsers, server):
        self.computer = computer
        self.browsers = browsers
        self.server = server
        return



