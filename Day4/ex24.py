#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月2日

@author: Ethan Wong
'''
#经典类和新式类 的区别
#区别：继承了 找同一方法同一函数 查找方式不一样 深度优先 广度优先
#新式类修复了经典类的一个bug 经典类在面临多重继承时的问题
#类是可以多继承的加，号
#你的类如果 继承自object 为新式类
#没有object 为经典类
class Father(object):
    
    def __init__(self):
        self.Fname = 'ffff'
        print 'father.__init__'
        
    def Func(self):
        print 'father.Func'
    
    def Bad(self):
        print 'father.抽烟喝酒泡妞'
       
class Son(Father):
    def __init__(self):
        self.Sname = 'ssss'
        print 'son.__init__'
        #显式调用父类构造函数
        #Father.__init__(self)
        
        super(Son,self).__init__()
        
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

