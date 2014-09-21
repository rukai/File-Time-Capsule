import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        with open("landing.html") as htmlFile:
            page = htmlFile.read()
        self.write(page)

class HubHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("The hub page!")

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("The about page!")

class CssHandler(tornado.web.RequestHandler):
    def get(self, filename):
        print(filename)
        with open("css/{}".format(filename)) as cssFile:
            css = cssFile.read()
        self.write(css)
