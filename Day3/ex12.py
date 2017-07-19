#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月24日

@author: Ethan Wong
'''
#商品列表加序号
li = ['手表','汽车','咖啡']

for item in li:
    print item

#第二个参数是起始值
for item in enumerate(li,11):
    print item[0],item[1]
    
#%s当占位符
#字符串格式化
s = 'i am {0} {1}'
print s.format('alex','sss')