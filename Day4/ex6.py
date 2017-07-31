#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月31日

@author: Ethan Wong
'''
#装饰器
#加上装饰器的话 就会在所有方法中加验证功能
#
def outer(fun):
    def wrapper(arg):
        print '验证'        
        result = fun(arg)
        print '嗨嗨嗨'
        return result
    return wrapper
#函数要和装饰器建立某种关系 用@服务号和装饰器的函数名outer
@outer
def Func1(arg):
    print 'func1',arg
    return 'return'
'''
Func1 =
def wrapper(arg):
    print '验证' 
    fun(arg)   
    print '嗨嗨嗨'
'''
'''
@outer 
def Func2():
    print 'func2'
@outer    
def Func3():
    print 'func3'
'''
response = Func1('alex')
print response
#Func2()
#Func3()