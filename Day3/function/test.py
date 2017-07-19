#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月17日

@author: Ethan Wong
'''

print 'test',__name__
def Foo():
    '''
    命令老荀
    '''
    Bar()
    print '老荀去砍柴！'

def Bar():
    '''
    命令狗熊
    '''
    print '狗熊掰棒子！'

if __name__ == '__main__':
    Foo()
else:
    print '滚之'