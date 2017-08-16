#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月16日

@author: Ethan Wong
'''

class Foo(object):
    
    def __init__(self):
        print 'init'
        
    def __call__(self):
        return 'call'
    
foo = Foo()
foo()