#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月1日

@author: Ethan Wong
'''
#面向对象和函数式编程选择
#面向对象多态 狗芽菜上山打狼 你上山打狼 避免重复代码 灵活 代码扩展更加容易


#公有 和私有
#私有字段一般用在 不让别人改 只能看到只读

class Province:
        #静态字段 只属于类
    memo = '中国的23个省之一'
    
    def __init__(self,name,capital,leader,falg):
        #动态字段 属于对象
        self.name = name
        self.capital = capital
        self.leader = leader
        #私有
        self.__Thailand = falg
    #间接的访问   
    def show(self):
        print self.__Thailand
        
    #私有方法
    def __sha(self):
        print '我是alex'
    
    def public(self):
        self.__sha()
    
    @property    
    def siyou(self):
        return self.__Thailand

japan = Province('日本','北海道','王胜辉',True)
#间接访问
japan.show()
#print japan.__Thailand


japan.public()
#japan.__sha()
#不建议使用此种方法调用
japan._Province__sha()

#属性 以字段的形式访问
print japan.siyou

