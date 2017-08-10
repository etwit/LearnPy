#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月2日

@author: Ethan Wong
'''
#旧式类 特性 即可读也可写
class test1:
    
    def __init__(self):
        self.__pravite = 'alex 1'
        
    @property
    def Show(self):
        return self.__pravite

#新式类    特性只读 可写需加@方法名.setter
class test2(object):
    
    def __init__(self):
        self.__pravite = 'alex 2'
        
    @property
    def Show(self):
        return self.__pravite
    
    @Show.setter
    def Show(self,value):
        self.__pravite = value
    
t1 = test1()
print t1.Show
t1.Show = 'chang 1'
print t1.Show

t2 = test2()
print t2.Show
t2.Show = 'chang 2'
print t2.Show
    