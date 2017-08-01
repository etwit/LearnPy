#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月1日

@author: Ethan Wong
'''
#面向对象
#1.先跟世界上某一个局域内进行归类 ：人 与兽 创建两个类
#那我想造一个人 人在程序里就是一个对象 有血 有肉 四肢
#把创建对象的动作 叫实例化 实例化附上名字 变成 人和李阳 人和老狗
'''
class alex:
    xx = '没心没肺'

class person:
    xue = '血'
    
    def __init__(self,name,age):
        self.name = name
    
p1 = person('李阳',18)
print p1.name
p2 = person('老狗',30)
print p2.name
'''

class Province:
    #静态字段 只属于类
    memo = '中国的23个省之一'
    
    def __init__(self,name,capital,leader):
        #动态字段 属于对象
        self.name = name
        self.capital = capital
        self.leader = leader
    #动态方法 还有类方法
    def army_meet(self):
        print self.name+'正在阅兵'
     
    #把动态方法变成静态方法 1.方法前加上Python自带的@staticmethod
    #2.把self去掉 因为self是动态的
    #静态方法什么时候用：操作数据库 增删改查
    @staticmethod   
    def foo():
        print '所有省份沙场大点兵'
        
    #特性 加@property
    #作用 也可以添加返回值return
    @property
    def bar(self):
        #print self.name
        return 'somthing'
hb = Province('河北','石家庄','李阳')
sd = Province('山东','济南','盛辉')
print hb.name,hb.capital
print Province.memo

hb.army_meet()

Province.foo()

#变成字段的访问形式
hb.bar
print hb.bar