#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月3日

@author: Ethan Wong
'''
#自定义异常和手动触发异常
'''
class MyException(Exception):
    
    def __init__(self,msg):
        self.error = msg
    
    def __str__(self, *args, **kwargs):
        #return self.error
        return '该对象是MyException类实例化的一个对象'
    
obj = MyException('错误')
print obj
'''
class MyException(Exception):
    
    def __init__(self,msg):
        self.error = msg
    
    def __str__(self, *args, **kwargs):
        return self.error
        #return '该对象是MyException类实例化的一个对象'
    
#obj = MyException('自定义错误信息')
#print obj
try:
    raise MyException('自定义错误')
except Exception,e:
    print e