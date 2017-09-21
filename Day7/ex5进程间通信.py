#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月19日

@author: Ethan Wong
'''
#python进程间通信 
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
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Lock


'''def f(q,n):
    q.put([n,'hello'])

if __name__ =='__main__':
    q = Queue()
    for num in range(7):
        p = Process(target=f,args=(q,num))
        p.start()
    while True:
        print q.get()'''


#通过Lock进行进程同步       
def f1(l,n):
    l.acquire()
    print 'nnnnnnn',n
    l.release()

if __name__ =='__main__':
    lock = Lock()
    for num in range(10):
        p = Process(target=f1,args=(lock,num))
        p.start()
        #达到穿行效果
        p.join()


#共享进程之间状态

from multiprocessing import Process, Value, Array

'''def f2(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(15))
    print num
    print arr

    p = Process(target=f2, args=(num, arr))
    p.start()
    p.join()

    print num.value
    print arr[:]'''

#进程间的数据共享，是通过第三方通道
from multiprocessing import Process, Manager

'''def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    manager = Manager()

    d = manager.dict()
    l = manager.list(range(10))

    p = Process(target=f, args=(d, l))
    p.start()
    #为了达到穿行效果
    #p.join()

    print d
    print l'''