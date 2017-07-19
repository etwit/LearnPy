#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月26日

@author: Ethan Wong
'''
#序列化 把一个对象(序列、字典等)以特殊二进制的方式加密
#并对一个类一个对象还可以进行反序列化
import pickle

li = ['alex',11,22,'ok','sb']
dumpsed = pickle.dumps(li)
print dumpsed
print type(dumpsed)

#反序列化
loadsed = pickle.loads(dumpsed)
print loadsed
print type(loadsed)
#可以把序列化到文件里
#主要应用在Python与Python之间共享数据
#用这种形式实现了两个程序之间在内存之间的数据交互
with file('ex18tt.txt','r+') as f:
    pickle.dump(li, f)
#读取文件数据
with file('ex18tt.txt','r+') as f1:
    result = pickle.load(f1)
print result
#pickle还可以序列化对象 类 Python中的所有数据类型都可以被序列化
#json是所有语言都支持的接口形式，只能序列化常规数据格式类型 
#json和xml 同样的数据量json比xml小很多
import json
name_dic = {'name':'wupeiqi','age':30}
serialized = json.dumps(name_dic)
print serialized
fser = json.loads(serialized)
print fser
#写入json文件
with file('ex18.json','r+') as fj1:
    serj = json.dump(name_dic, fj1)
#读取ex8.json文件数据
with file('ex18.json','r+') as fj2:
    result2 = json.load(fj2)
print result2





