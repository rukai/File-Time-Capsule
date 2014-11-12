
# Copyright 2014 Lucas Kent
# Licenced under the GNU GPL V3

import datetime
import tornado.ioloop
import tornado.web
from backend import DB

class CustomHandler(tornado.web.RequestHandler):
    #Displays a 404 page for when a handler cannot find a suitable page to display.
    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            message = kwargs["exc_info"][1].reason
            print(message)
            self.render("404.html", page="404handler", message=message)
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
            self.render("file.html", page="File", ID=fileID, **fileDetails)
        except TypeError:
            raise tornado.web.HTTPError(404, reason="The requested page for a user file '/{}' does not exist.".format(fileID))

class FileHandler(CustomHandler):
    def get(self, fileID):
        try:
            fileDetails = DB.getFile(fileID)
            self.set_header("Content-Type", "application/octet-stream")
            self.set_header("Content-Disposition", "attachment; filename={}".format(fileDetails["name"]))
            if fileDetails["date_accessible"] > int(datetime.datetime.now().strftime("%s")):
                raise tornado.web.HTTPError(403, reason="This file cannot be accessed yet.")
            with open("fileDB/" + str(fileID), "br") as fileRead:
                self.write(fileRead.read())
        except TypeError:
            raise tornado.web.HTTPError(404, reason="The requested file '/{}' does not exist".format(fileID))


#Displays a 404 page for any undefined url
class Error404Handler(CustomHandler):
    def get(self, path):
        raise tornado.web.HTTPError(404, reason="The requested page '/{}' does not exist.".format(path))

