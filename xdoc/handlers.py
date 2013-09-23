#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import json
import tornado.web

from parser import Parser
from model import *
from bson.objectid import ObjectId

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        self.parser = Parser()
        db_init()

    def get_error_html(self, code, **kwargs):
        self.write(str(code))

#static file handler
class StaticHandler(tornado.web.StaticFileHandler):
    def initialize(self, path, filename):
        super(StaticHandler, self).initialize(path)
        self.filename = filename

    def get(self):
        super(StaticHandler, self).get(self.filename)

#REST
class DraftHandler(BaseHandler):
    def get(self, obj_id=None):
        try:
            if not obj_id:
                result = list(Doc.objects)
            else:
                result = Doc.objects.get(id=ObjectId(obj_id))
        except:
            raise tornado.web.HTTPError(404)

        if not result:
            raise tornado.web.HTTPError(404)

        self.write(json.dumps(result, cls=DocJSONEncoder))

    def put(self, obj_id=None):
        pass

    def post(self, obj_id=None):
        arguments = json.loads(self.request.body)
        path = arguments['path']

    def delete(self):
        pass
