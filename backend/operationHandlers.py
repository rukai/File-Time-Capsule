# Copyright 2014 Lucas Kent
# Licenced under the GNU GPL V3

import tornado.ioloop
import tornado.web
from backend import DB

#creates a new file based on data POST'd by client
class NewFileHandler(tornado.web.RequestHandler):
    def post(self):
        uploadedFile = self.request.files["file"][0]
        date = self.get_argument("datetime")
        notes = self.get_argument("notes")
        
        DB.newFile(uploadedFile, date, notes)
