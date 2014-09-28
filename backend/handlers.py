# Copyright 2014 Lucas Kent
# Licenced under the GNU GPL V3

import tornado.ioloop
import tornado.web

class RootHandler(tornado.web.RequestHandler):
    def get(self):
        if False: #logged in
            self.render("hub.html", page="Hub")
        else:
            self.render("landing.html", page="Landing")

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("about.html", page="About")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html", page="Login")

class SignupHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("signup.html", page="Signup")

class FilePageHandler(tornado.web.RequestHandler):
    def get(self, requestedFile):
        self.render("file.html", page="File", filename=requestedFile)
