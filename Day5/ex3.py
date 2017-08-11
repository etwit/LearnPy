#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月4日

@author: Ethan Wong
'''
#特性解释
#经典类和新式类中的特性的区别

#经典类中的特性全部是可读可写(没有只读的功能)
class Person:
    def __init__(self):
        self.__name = 'alex'
    @property
    def Name(self):
        return self.__name
p1 = Person()
#通过特性Nanme，读取self.__name的值
print p1.Name
#通过特性Name，设置self.__name的值
p1.Name = 'xxxx'
print p1.Name


#新式类中特性默认都是只读，如果想设置，那么就需要再创建
#一个被装饰@xxx.setter修饰的特性

class Person1(object):
    
    def __init__(self):
        self.__name = 'alex'
    @property
    def Name(self):
        return self.__name
    #必须在创建一个@Name.setter的修饰特性
    @Name.setter
    def Name(self,value):
        self.__name = value
p1 = Person1()
#通过特性Nanme，读取self.__name的值
print p1.Name
#通过特性Name，设置self.__name的值时，会出错
p1.Name = 'xyzxyz'
print p1.Name

