#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月27日

@author: Ethan Wong
'''
#反射应用
'''
from function4 import account


data = raw_input('请输入地址：')
#array = data.split('/')
if data == 'account/login':
    account.login()
elif data == 'account/logout':
    account.logout()
'''
#测试规范 xxx/xxx
#account/login  account/logout admin/index
data = raw_input('请输入地址：')
array = data.split('/')
userspance = __import__('function4.'+array[0])
model = getattr(userspance, array[0])
func = getattr(model,array[1])
func()



