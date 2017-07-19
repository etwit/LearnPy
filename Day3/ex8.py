#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月20日

@author: Ethan Wong
'''
#主讲参数可变性

#登录成功后 打印列表
#变态需求：函数只接收一个函数，却可传多个值
def show1(arg):
    for item in arg:
        #
        print item
def show2(arg1,arg2):
    print arg1,arg2

def show3(*arg):
    for item in arg:
        print item
    
show1(['lyang','alex'])

show2('liyang','zhangbing')

show3('liyanga','wangwuc','zhangtianb','liuliud')

#传参数时包装成字典
def show4(**kargs):
    for item in kargs.items():
        print item
show4(name='liyang',age='30',salary='5000')

def show5(**kargs):
    for item in kargs.items():
        print item
user_dict = {'age':'30','salary':'5000'}
#如果想把字典传入 要把星号带上列表也是一样的
show5(**user_dict)

