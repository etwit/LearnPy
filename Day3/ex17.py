#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月26日

@author: Ethan Wong
'''
#Md5加密
#官方不推荐
import md5
hash2 = md5.new()
hash2.update('admin')
print hash2.hexdigest()

#推荐使用此方式
#把用户输入的 转MD5和数据库里的值比较
import hashlib
hash1 = hashlib.md5()
hash1.update('1234567')
print hash1.hexdigest()
print hash1.digest()