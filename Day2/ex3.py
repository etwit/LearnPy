#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月7日

@author: Ethan Wong
'''
#Python文件处理
#文件处理模式
#r已只读模式打开文件
#w已只写模式打开文件
#a已追加模式打开文件

#r+b以读写模式打开
#w+b以写读模式打开
#a+b以追加及读模式打开
f = file('ex3tt.txt','r')
for line in f.readlines():
    line = line.strip('\n').split(':')
    print line
f.close()    

#列表、元组、字典的使用

#集合的妙用

#函数基础
