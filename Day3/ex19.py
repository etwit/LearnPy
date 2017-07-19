#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月26日

@author: Ethan Wong
'''
#正则表达式 和time
import re
#match只能从字符串起始的位置匹配
re1 = re.match('\d+', 'adljfaldjladjflajd')
if re1:
    print re1.group()
else:
    print re1
    
#search搜索整个字符串内容
re2 = re.search('\d+', 'adljfaldjladj123flajd')
if re2:
    print re2.group()
#findall会找到所有的
re3 = re.findall('\d+', 'adl11jf22aldjl333adj123fl44ajd')
print re3
#经过编译后返回的对象 为提升效率 编译一次 取100次
com = re.compile('\d+')
print type(com)
print com.findall('adl11jf22aldjl33adjfl44ajd')
#\d:匹配一个数字 +:匹配大于等于1 \w:匹配_字母数字- *:匹配多个字符
re4 = re.search('\d+\w*\d+', 'adl11jf22aldjl333adj123fl44ajd')
print re4.group()
print re4.groups()


