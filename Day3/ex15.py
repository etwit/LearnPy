#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月25日

@author: Ethan Wong
'''

#反射 通过字符串的形式导入模块 并以字符串的形式执行函数
#主要应用于大型程序随时切换数据库时 设计模式 工厂模式 降低程序的耦合
temp = 'sys'

model = __import__(temp)
print model.path

func = 'getrefcount'
Function = getattr(model,func)
print Function

#判断某一个模块 有没有那个函数
#hasattr()
#删除这个模块里的那个函数
#delattr()

#import sys
#help(sys)

print chr(90)
