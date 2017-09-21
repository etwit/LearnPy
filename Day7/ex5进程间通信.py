#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月19日

@author: Ethan Wong
'''

from multiprocessing import Process
import threading

'''def run(info_list,n):
    
    info_list.append(n)
    print info_list
    
info = [] 
if __name__ =='__main__':
    print '--------Process--------'
    for num in range(10):
        p = Process(target=run,args=[info,num])
        p.start()
    print '--------threading------'
    for num in range(10):
        p = threading.Thread(target=run,args=[info,num])
        p.start()
    '''
#通过multiprocessing 中的Queue 共享
from multiprocessing import Process,Queue,Lock

#通过Lock进行线程同步
'''def f(q,n):
    q.put([n,'hello'])

if __name__ =='__main__':
    q = Queue()
    for num in range(7):
        p = Process(target=f,args=(q,num))
        p.start()
    while True:
        print q.get()'''
        
def f1(l,n):
    l.acquire()
    print 'nnnnnnn',n
    l.release()

if __name__ =='__main__':
    lock = Lock()
    for num in range(7):
        p = Process(target=f1,args=(lock,num))
        p.start()
