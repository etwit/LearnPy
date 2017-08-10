#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月20日

@author: Ethan Wong
'''
#yield的使用 创建yield即生成器

'''
print range(10)

print xrange(10)

#range会创建一个数组，xrange只有在便利的时候创建，延迟创建
for item in xrange(3):
    print item
    
def foo():
    yield 11
    yield 22
    yield 33
re = foo()
#print re
for item in re:
    print item  
'''

def AlexReadlines():
    seek = 0
    while True:
        #with一旦出了f.seek()这一级在在执行下面会
        #自动关闭文件不用再f.close()
        #with file('ex9tt.txt','r') as f:
        f = file('ex9tt.txt','r')
            #根据字节跳到某一处
        f.seek(seek)
        data = f.readline()
        if data:
            seek = f.tell()
            yield data
        else:
            return

print AlexReadlines()
for line1 in AlexReadlines():
    print line1