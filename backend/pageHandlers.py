
# Copyright 2014 Lucas Kent
# Licenced under the GNU GPL V3

import tornado.ioloop
import tornado.web
from backend import DB

#Displays the homepage
class RootHandler(tornado.web.RequestHandler):
    def get(self):
        if False: #logged in
            self.render("hub.html", page="Hub")
        else:
            self.render("landing.html", page="Landing")

#Displays the about page
class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("about.html", page="About")

#Displays the login page
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html", page="Login")

#Displays the signup page
class SignupHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("signup.html", page="Signup")

#Displays a unique page for each file
class FilePageHandler(tornado.web.RequestHandler):
    def get(self, requestedFile):
        self.render("file.html", page="File", filename=requestedFile)
