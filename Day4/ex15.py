#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月1日

@author: Ethan Wong
'''
#开始 为了对大千世界进行分类 我们创建了类
#属于这一类的某一个对象 东西 是通过实例化进行创建的
#类里面有各种各样的 字段 方法 特性 有什么作用 
#字段 方法 特性的目的就是为你提供统一方法或数据 来处理这一类的请求
#创建类的目的是对某一类东西 做一个抽象 这一类都有同样的动作
#

class MsSqlHelper:
    @staticmethod
    def add(self,sql):
        pass
    @staticmethod
    def delete(self,sql):
        pass
    @staticmethod
    def update(self,sql):
        pass
    @staticmethod
    def select(self,sql):
        pass    

#对应一万个业务 的话 就要创建 n多个对象 站用内存空间
#而静态方法的话
ms = MsSqlHelper()
ms.update()
ms = MsSqlHelper()
ms.update()
ms = MsSqlHelper()
ms.update()

#静态方法 作用是通过不实例化类就可以调用 下面的方法
MsSqlHelper.add()
MsSqlHelper.update()

#面向对象编程 每次都要new一个方法
#里面有 堆 栈 code segment: 静态方法 在内存code segment里