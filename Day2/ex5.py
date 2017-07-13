#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月11日

@author: Ethan Wong
'''
#open和file没有区别
f = open('size_test.txt','r')

f.read()
#open获取文件的开头和结尾的句柄，如果实时的刷新文件，打开一次会自动刷新结尾
#和tail -f 功能类似