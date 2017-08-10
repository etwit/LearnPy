#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月26日

@author: Ethan Wong
'''
#time模块 时间的三种表达方式
#1、时间戳    1970年1月1日之后的秒
#3、元组 包含了：年、日、星期等... time.struct_time
#4、格式化的字符串    2014-11-11 11:11
import time
#print time.time()

#print time.gmtime()    #可加时间戳参数
#print time.localtime() #可加时间戳参数

#print time.strftime('%Y-%m-%d %H:%M:%S')


#格式化转换
#转化结构化格式
#print time.strptime('2016-11-11', '%Y-%m-%d')

#时间戳
print time.time()
print time.mktime(time.localtime())
#结构化格式
print time.gmtime()    #可加时间戳参数
print time.localtime() #可加时间戳参数
print time.strptime('2014-11-11', '%Y-%m-%d')
#字符串格式
print time.strftime('%Y-%m-%d %H:%M:%S') #默认当前时间
print time.strftime('%Y-%m-%d',time.localtime()) #默认当前时间
print time.asctime()
print time.asctime(time.localtime())
print time.ctime(time.time())
