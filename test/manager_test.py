#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
from os.path import join, dirname, abspath

sys.path.insert(0, join(dirname(dirname(abspath(__file__)))))
from xdoc.manager import *

class TestModels(unittest.TestCase):
    
    def setUp(self):
        FileManager.INDEX_FILE = 'test.json'
        self.f = FileManager('../')

    def test_filemanager(self):
        self.f.update_info(path='test.md', title='Test', category='test')
        info = self.f.get_info('test.md')
        print info
        self.assertEqual(info['title'], 'Test')
        self.assertEqual(info['category'], 'test')

    def test_gitmanager(self):
        gm = GitManager('../')
        info = gm.get_all_info()
        print info

    def tearDown(self):
        os.remove(self.f.index)
 
if __name__ == '__main__':
    unittest.main()
