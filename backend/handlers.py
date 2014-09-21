import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("landing.html", page="Root")

class HubHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("hub.html", page="Hub")

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("about.html", page="About")
