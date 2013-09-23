#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
from os.path import join, dirname, abspath
from bson.objectid import ObjectId
import uuid
from datetime import datetime
import json

sys.path.insert(0, join(dirname(dirname(abspath(__file__)))))
from xdoc.model import *

class TestModels(unittest.TestCase):
    
    def setUp(self):
        db_init('xdoc')

    def test_Doc(self):
        with open('../example.md', 'r') as f:
            content = f.read().decode('utf-8')

        '''
        d = Doc(uuid=str(uuid.uuid4()),
                title='Example',
                content=content);
        d.save()
        '''
        d = Doc.objects
        print json.dumps(d, cls=DocJSONEncoder)

if __name__ == '__main__':
    unittest.main()
