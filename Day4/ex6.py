#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月31日

@author: Ethan Wong
'''
#装饰器
#加上装饰器的话 就会在所有方法中加验证功能
#装饰器：在源代码不修改的情况下 在他的之前或之后添加一些功能
#修改密码流程 第一 第二 第三 过了第二才能 到达第三步
#可以做成一个类
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