#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月11日

@author: Ethan Wong
'''
#元组tuple 不可修改

a =(1,2,3,4,5)
#转换list
list(a)
#转换tuple
tuple(a)

import sys,os

if len(sys.argv) <=4:
    print "usage:./ex9.py old_text new_text filename"
old_text,new_text = sys.argv[1],sys.argv[2]

file_name = sys.argv[3]

f = file(file_name,'rb')
new_file = file('.%s.bak' % file_name,'wb')
for line in f.xreadlines():
    new_file.write(line.replace(old_text,new_text))
f.close()
new_file.close()

if '--bak' in sys.argv:
    #unchanged
    os.rename(file_name, '%s.bak'%file_name)
    #changed
    os.rename('.%s.bak'%file_name,file_name)
else:
    #replace old file
    os.rename('.%s.bak'%file_name,file_name)

#python ex9.py : | passwd