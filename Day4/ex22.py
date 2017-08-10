#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月2日

@author: Ethan Wong
'''
#析构函数 和 __call__方法 

#构造函数是init

import time
class foo:
    
    def __init__(self):
        pass
    
    #析构函数
    #通过类创建对象的时候经过init函数 然后内存就被Python解释器来管理
    #他会有一套算法 去计算 计算这个对象是不是还在应用
    #当不再有指针调用的时候，就会调用析构函数 特殊函数 来销毁对象占用空间
    def __del__(self):
        print '解释器要销毁我了，我要做最后一次的呐喊！'
    
    def go(self):
        print 'go'
        
    def __call__(self):
        print 'call'

#创建对象f1    
f1 = foo()
f1.go()
time.sleep(10)
#如果对 对象后面加() 就是调用call方法
f1()



