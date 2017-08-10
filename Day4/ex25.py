#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月3日

@author: Ethan Wong
'''
#抽象类和抽象方法
#接口定义

#Python如何实现 类似Java interface 功能：就是利用抽象类和方法实现

#抽象类加抽象方法=接口 就是第二种接口 规范

from abc import ABCMeta,abstractmethod

class Alert:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def Send(self):pass

#一旦继承了抽象类 接口 就要符合一定的规范 就要按照规范来   
class Weixin(Alert):
    def __init__(self):
        print '__init__ foo'
    
    def Send(self):
        print 'send.weixin'
        
f = Weixin()
f.Send()