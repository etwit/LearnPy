#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月14日

@author: Ethan Wong
'''

'''
三层架构之公共层
model模型层
utility公共层
'''
import MySQLdb

class MySqlHelper(object):
    
    def __init__(self):
        pass
    
    def Get_Dict(self,sql,params):
        conn = MySQLdb.connect(host='localhost',user='welltime',passwd='123456',db='welltime')
        #获取数据的时候以字典类型拿到
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        #获取数据以元组类似拿到
        #cur = conn.cursor()
        
        reCount = cur.execute(sql,params)
        data = cur.fetchall()
        
        cur.close()
        conn.close()
        return data
    
    def Get_One(self,sql,params):
        conn = MySQLdb.connect(host='localhost',user='welltime',passwd='123456',db='welltime')
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        
        reCount = cur.execute(sql,params)
        data = cur.fetchone()
        
        cur.close()
        conn.close()
        return data

  
helper = MySqlHelper()
sql = "select * from admin where id>%s"
params = (1,)

simple_data = helper.Get_One(sql, params)
dict_data = helper.Get_Dict(sql, params)

print simple_data
print dict_data
