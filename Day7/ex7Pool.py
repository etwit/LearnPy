#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月21日

@author: Ethan Wong
'''
#进程池Pool

from multiprocessing import Pool
import time

def f1(x):
    print x*x
    time.sleep(1)
    return x*x
if __name__=='__main__':
    res_list = []
    pool = Pool(processes=4)
    
    for num1 in range(10):
        res = pool.apply_async(f1,[num1,])
        #res = Process(target=f,args=[i,])
        print '----:',num1
        res_list.append(res)
    
    for m in res_list:
        print m.get(timeout=10)
    
    #print pool.map(f1,range(10))
