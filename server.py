#!/usr/bin/env python3
# Copyright 2014 Lucas Kent
# Licenced under the GNU GPL V3

import tornado.ioloop
import tornado.web

from backend.handlers import *

def run():
    application = tornado.web.Application(
        [
            (r"/", RootHandler),
            (r"/about", AboutHandler),
            (r"/login", LoginHandler),
            (r"/signup", SignupHandler),
            (r"/css/(.+)", tornado.web.StaticFileHandler, {"path": "./css"}), # check the file access this gives
            (r"/js/(.+)", tornado.web.StaticFileHandler, {"path": "./js"}),
            (r"/graphics/(.+)", tornado.web.StaticFileHandler, {"path": "./graphics"}),
            (r"/fonts/(.+)", tornado.web.StaticFileHandler, {"path": "./fonts"}),
            ],
        template_path="templates/",
        )
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run()
