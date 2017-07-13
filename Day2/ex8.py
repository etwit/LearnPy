#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月11日

@author: Ethan Wong
'''
#列表index用法
a = [1,2,3,4,5,6,7,8,1,2,3,4,1,2,3,4,5]
pos = 0
for i in range(a.count(2)):
    if pos == 0:
        pos = a.index(2)
    else:
        pos = a.index(2,pos+1)
    print 'Find:',pos