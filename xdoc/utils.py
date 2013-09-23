#!/usr/bin/env python
# -*- coding: utf-8 -*-

def title2file(title):
    return title.replace(' ', '-')

def file2title(filename):
    return filename.replace('-', ' ')
