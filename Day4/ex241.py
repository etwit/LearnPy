#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月3日

@author: Ethan Wong
'''
#经典类多重继承问题
#多重继承时经典类深度优先，先搜B-搜A-不在搜C
#多重继承时新式方法广度优先，先搜B-搜C-在搜A
class A(object):
    def __init__(self):
        print 'This is A'
    def save(self):
        print 'save methmod from A'
        
class B(A):
    def __init__(self):
        print 'This is B'

class C(A):
    def __init__(self):
        print 'This is C'
    def save(self):
        A.save(self)
        print 'save methmod from --C--'

class D(B,C):
    def __init__(self):
        print 'This is D'

C = D()
C.save()
