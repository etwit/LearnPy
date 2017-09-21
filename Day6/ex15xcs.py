#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月18日

@author: Ethan Wong
'''
import threading
import time



num = 0

def run(n):
    time.sleep(1)
    global num
    samp.acquire()
    num +=1
    print '%s' %num
    samp.release()

samp = threading.BoundedSemaphore(4)

for i in range(200):
    t = threading.Thread(target=run,args=(i,))
    t.start()    