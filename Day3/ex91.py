#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月21日

@author: Ethan Wong
'''
'''
默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
一是必选参数在前，默认参数在后，否则Python的解释器会报错
（思考一下为什么默认参数不能放在必选参数前面）;
二是如何设置默认参数。
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
变化小的参数就可以作为默认参数。
使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
'''
def power(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s

print power(5,3)

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print add_end()
print add_end()

'''
可变参数
定义可变参数和定义一个list或tuple参数相比，
仅仅在参数前面加了一个*号。
'''
def calc(*numbers):
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n * n
    return sum1

print calc(1,2)
print calc()
#Python允许你在list或tuple前面加一个*号，
#把list或tuple的元素变成可变参数传进去
nums = [1,2,3]
print calc(*nums)

'''
关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时
自动组装为一个tuple。而关键字参数允许你传入0个或任意个含
参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
'''
def person(name,age,**kw):
    print(name,age,kw)
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack',24,**extra)

