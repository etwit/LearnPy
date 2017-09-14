#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月13日

@author: Ethan Wong
'''
import threading
import time

gl_num = 0

lock = threading.RLock()

def Func():
    lock.acquire()
    global gl_num
    gl_num +=1
    time.sleep(1)
    print gl_num
    lock.release()
    
for i in range(10):
    t = threading.Thread(target=Func)
    t.start()

