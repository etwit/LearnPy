#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月3日

@author: Ethan Wong
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(6)
while True:
    try:
        x = next(g)
        print ('g:',x)
    except StopIteration as e:
        print ('Generator return value:',e.value)
        break