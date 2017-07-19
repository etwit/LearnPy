#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月21日

@author: Ethan Wong
'''
#三元运算和lambda表达式
temp = None
if 1>3:
    temp = 'gt'
else:
    temp = 'lt'
print temp

result = 'gt' if 1>3 else 'lt'
print result


#lambda表达式
def foo(x,y):
    return x+y
print foo(4,10)
#智能调用一次 函数简单不会经常被调用
temp = lambda x,y,z:x+y*z
print temp(4,4,5)

#内置函数
a = []
#help(a)
#传的是key
print dir()
#传的是key和value
print vars()
#查看变量类型
print type(a)
#reload()会重新载入一次函数

t1 = 123
t2 = 124
print id(t1)
print id(t2)

print abs(-9)
print bool(-1)
#分页显示 取余数取商
#除数除以被除数等于商
print divmod(9, 3)
#指数
print pow(2, 11)

#所有都是真才是真0是假
print all([1,2,3,0])
#如果有一个是真即是真
print any([1,0,0,0])

print bool('')

print bool(None)
#字母数字转换
print chr(69)
print ord('A')

#十进制 十六进制 二进制
print hex(2000)
print bin(2000)
print oct(2)

