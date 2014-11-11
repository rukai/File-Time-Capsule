
# Copyright 2014 Lucas Kent
# Licenced under the GNU GPL V3

import tornado.ioloop
import tornado.web
from backend import DB

class CustomHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render("base.html", page="404")
        else:
            #super(tornado.web.RequestHandler, self).write_error(status_code, **kwargs)
            pass

#Displays the homepage
class RootHandler(CustomHandler):
    def get(self):
        if False: #logged in
            self.render("hub.html", page="Hub")
        else:
            self.render("landing.html", page="Landing")

#Displays the about page
class AboutHandler(CustomHandler):
    def get(self):
        self.render("about.html", page="About")

#Displays the login page
class LoginHandler(CustomHandler):
    def get(self):
        self.render("login.html", page="Login")

#Displays the signup page
class SignupHandler(CustomHandler):
    def get(self):
        self.render("signup.html", page="Signup")

#Displays a unique page for each file
class FilePageHandler(CustomHandler):
    def get(self, fileID):
        try:
            fileDetails = DB.getFile(fileID)
            self.render("file.html", page="File", **fileDetails)
        except TypeError:
            raise tornado.web.HTTPError(404, "Attempted to access user file that does not exist")

class Error404Handler(CustomHandler):
    def get(self, pathAttempt):
        raise tornado.web.HTTPError(404, "File not found")
