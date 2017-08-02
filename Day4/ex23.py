#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月2日

@author: Ethan Wong
'''
#继承

class Father:
    
    def __init__(self):
        self.Fname = 'ffff'
        
    def Func(self):
        print 'father.Func'
    
    def Bad(self):
        print 'father.抽烟喝酒泡妞'
       
class Son(Father):
    def __init__(self):
        self.Sname = 'ssss'
        
    def Bar(self):
        print 'son.Bar'
        
    def Bad(self):
        Father.Bad(self)
        print 'father.戒烟了不喝酒了妞还是改不了'
#父类和子类
#基类和派生类        
        
s1 = Son()
s1.Bar()
s1.Func()
s1.Bad()