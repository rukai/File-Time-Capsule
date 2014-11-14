# Copyright 2014 Lucas Kent
# Licenced under the GNU GPL V3

import tornado.ioloop
import tornado.web
from backend import DB

#creates a new file based on data POST'd by client
class NewFileHandler(tornado.web.RequestHandler):
    def post(self):
        #organise data
        uploadedFile = self.request.files["file"][0]
        date = self.get_argument("datetimeSubmit")
        notes = self.get_argument("notes")
        
        #store data
        ID = DB.newFile(uploadedFile, date, notes)

        #redirect to the new files page
        self.redirect("/filepage/" + ID)
