#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月24日

@author: Ethan Wong
'''
def function(arg):
    print arg

function('alxe')
#也可以通过 apply执行函数
#print apply(function('aaa'))

def foo(arg):
    return arg + 100
li = [11,22,33]
temp = []
for item in li:
    temp.append(foo(item))
print temp

#map可以替换以上函数
#map对所有的元素进行统一的操作
temp = map(lambda arg:arg+100, li)
print temp

#用作过滤的 想过滤加一个过滤条件
#如果返回的是true 放在新列表 否则返回false
def foo1(arg):
    if arg<22:
        return True
    else:
        return False
print filter(foo1,li)
#用作过滤的 判断通过了才放到新的序列
print filter(lambda x:x<22,li)

#累加 累乘 只能有两个参数
print reduce(lambda x,y:x*y,li)

