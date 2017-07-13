#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月11日

@author: Ethan Wong
'''
#列表
name = ['!','@','#',1,2,3,4,5,6,1,2,3,4,5,6,7,8,1,2]

first_pos = 0
for i in range(name.count(2)):
    new_list = name[first_pos:]
    next_pos = new_list.index(2) +1
    print 'Find:',first_pos + next_pos
    first_pos += next_pos

a = range(100)

print a[::2]
print a[1::2]