#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月2日

@author: Ethan Wong
'''
#只读特性 和 可写特性

#第二步让类继承object
class Province(object):
    
    def __init__(self,name,capital,leader,falg):
        #动态字段 属于对象
        self.name = name
        self.capital = capital
        self.leader = leader
        #私有
        self.__Thailand = falg
    
    #特性 只读特性
    @property
    def siyou(self):
        return self.__Thailand
    
    
    #第一步setter可以用作只写
    #只写的特性
    @siyou.setter
    def siyou(self,value):
        self.__Thailand = value
    
japan = Province('日本','北海道','王胜辉',True)
print japan.siyou
japan.siyou = False
print japan.siyou
