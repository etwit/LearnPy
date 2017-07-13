#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月7日

@author: Ethan Wong
'''
#file的方法
f = file('ex4tt.txt','r+')
for line in f.xreadlines():
    print line
f.close()