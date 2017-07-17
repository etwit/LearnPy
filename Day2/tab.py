#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月13日

@author: Ethan Wong
'''
try:
    import readline
except ImportError:
    print("Module readline not available.")
else:
    #import rlcompleter
    readline.parse_and_bind("tab: complete")