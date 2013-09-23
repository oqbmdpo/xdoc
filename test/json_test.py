#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
from os.path import join, dirname, abspath
from bson.objectid import ObjectId
import uuid
from datetime import datetime
from json import JSONEncoder

sys.path.insert(0, join(dirname(dirname(abspath(__file__)))))
from xdoc.model import *

class Test(object):
    title = 'Test'
    content = 'This is the content'

class TestJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Test):
            return {'title': obj.title, 'content': obj.content}
        else:
            return super(TestJSONEncoder, self).default(obj)

t = [Test(), Test(), Test()]
print json.dumps(t, cls=TestJSONEncoder)
