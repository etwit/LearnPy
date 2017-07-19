#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月25日

@author: Ethan Wong
'''
#random 用于生成随机数
import random
#生成随机数0~1之间
print random.random()
#生成1~5之间整数
print random.randint(1,5)
#生成1~10之间的数
print random.randrange(1,10)

#生成随机验证码
checkcode = ''
for i in range(6):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print checkcode
'''
for i in range(6):
    if i == random.randint(1,5):
        print random.randint(1,5)
    else:
        temp = random.randint(65,91)
        print chr(temp)
'''
code = []
for i in range(6):
    if i == random.randint(1,5):
        code.append(str(random.randint(1,5)))
    else:
        temp = random.randint(65,90)
        code.append(chr(temp))
#join效率最高
print ''.join(code)