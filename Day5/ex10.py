#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月14日

@author: Ethan Wong
'''

#fetchone() 是第一次拿到第一行的数据,第二次拿到是第二行的数据，以此类推。
#fetchall() 是一次把所有的数据都拿回来
#fetchmany() 


'''
import MySQLdb

#创建连接
conn = MySQLdb.connect(host='localhost',user='welltime',passwd='123456',db='welltime')

#获取数据的时候以字典类型拿到
cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
#获取数据以元组类似拿到
#cur = conn.cursor()


reCount = cur.execute('select * from admin')
nRet = cur.fetchone()
print nRet

nRet = cur.fetchone()
print nRet
cur.scroll(0,mode='absolute')
nRet = cur.fetchone()
print nRet

#相对定位
#cur.scroll(-1,mode='relative')
#绝对定位
#cur.scroll(0,mode='absolute')


cur.close()
conn.close()

#print reCount
#print nRet
'''
import MySQLdb

#创建连接
conn = MySQLdb.connect(host='localhost',user='welltime',passwd='123456',db='welltime')
#cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
cur = conn.cursor()

sql = "insert into media(address) values(%s)"

params = ('/usr/bin/a.txt',)

reCount = cur.execute(sql,params)
conn.commit()
#获取自增id
print cur.lastrowid

cur.close()
conn.close()

#print reCount
