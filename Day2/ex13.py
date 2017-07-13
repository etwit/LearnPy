#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月12日

@author: Ethan Wong
'''
#set集合 特点：无序 元素不重复 功能：关系测试 去重

name_set = {'a','c',3,'d',5}

print name_set

x = {1,'a',2,'f',5}
y = {2,'a',5,6}
a = {1,2,3,4,5}
b = {2,3,4}
#交 并 差集 对称差集
print x & y
print x | y
print x - y
print x ^ y
print a.issubset(b)
print a.issuperset(b)