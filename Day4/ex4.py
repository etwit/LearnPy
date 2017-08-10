#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月27日

@author: Ethan Wong
'''
#反射应用
#反射就是根据字符串的形式导入模块
'''
from function4 import account


data = raw_input('请输入地址：')
#array = data.split('/')
if data == 'account/login':
    account.login()
elif data == 'account/logout':
    account.logout()
'''

#反射就是根据字符串的形式导入模块，再根据字符串形式去执行模块下的函数
#测试规范 xxx/xxx
#account/login  account/logout admin/index web/hello
data = raw_input('请输入地址：')
array = data.split('/')
userspance = __import__('function4.'+array[0])
model = getattr(userspance, array[0])
func = getattr(model,array[1])
func()



