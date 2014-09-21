#!/usr/bin/env python3
import tornado.ioloop
import tornado.web

from fileaway.handlers import *

def run():
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/hub", HubHandler),
        (r"/about", AboutHandler),
        (r"/css/(.+)", tornado.web.StaticFileHandler, {"path": "./css"}), # check the file access this gives
        (r"/js/(.+)", tornado.web.StaticFileHandler, {"path": "./js"}),
        ])
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run()
