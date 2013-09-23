#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tornado.ioloop
import tornado.httpserver
import tornado.web
from tornado.options import define, options
import git

from handlers import *

define('port', default=8000, help='run on the given port', type=int)
define('db', default='xdoc', help='database name', type=str)

class XdocApp(tornado.web.Application):
    def __init__(self, db_name):
        self.db_name = db_name

        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'login_url': '/login',
        }

        html_path = os.path.join(settings['static_path'], 'html')
        handlers = [
            (r'/draft/(.*)', DraftHandler),
            (r'/draft', DraftHandler),
            (r'/editor', StaticHandler, {'path': html_path, 'filename': 'edit.html'}),
        ]

        super(XdocApp,self).__init__(handlers, **settings)

if __name__ == '__main__':
    options.parse_command_line()
    XdocApp(options.db).listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
