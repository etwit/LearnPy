#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月12日

@author: Ethan Wong
'''
#购物车程序
#字典如果有100万个数值，可以快速查询到数值
#字典无默认排序
name_info = {'name':'Jacky',
             'age':29,
             'job':'Engineer',
             'salary':30000,
             'address':'BJ',
             'gender':'Male'
             }
#print name_info['name']

#效率较高
#for i in name_info:
#    print i,name_info[i]

#items 是每一次循环都是两个值  效率较低 要先转成列表
for k,v in name_info.items():
    print k,v
    


info3 = name_info.copy()

name_info['age'] = 39
name_info['addr'] = 'Beijing'
#浅copy
#字典里套列表，列表里也可以套字典
info3['exlist'] = ['Coral','Erion']

info3['exlist'].append('Wutenglan')

print name_info
print info3

#深copy import copy
import copy
info5 = copy.deepcopy(info3)

info3['exlist'][2] = 'LongZeluola'
print info5
print info3

