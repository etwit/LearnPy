#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月4日

@author: Ethan Wong
'''
#Python操作MySQL之查询

'''
import MySQLdb

#创建连接
conn = MySQLdb.connect(host='localhost',user='welltime',passwd='123456',db='welltime')
#cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
cur = conn.cursor()


reCount = cur.execute('select * from admin')
nRet = cur.fetchall()


cur.close()
conn.close()

print reCount
print nRet
'''

'''
import MySQLdb

#创建连接
conn = MySQLdb.connect(host='localhost',user='welltime',passwd='123456',db='welltime')
#cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
cur = conn.cursor()

sql = "insert into admin(id,name,address) values(%s,%s,%s)"

params = ('3','alex','usa')

reCount = cur.execute(sql,params)
conn.commit()

cur.close()
conn.close()

print reCount
'''

'''
import MySQLdb

#创建连接
conn = MySQLdb.connect(host='localhost',user='welltime',passwd='123456',db='welltime')
#cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
cur = conn.cursor()

sql = "delete from admin where id=%s"

params = ('3',)

reCount = cur.execute(sql,params)
conn.commit()

cur.close()
conn.close()

print reCount
'''

'''
import MySQLdb

#创建连接
conn = MySQLdb.connect(host='localhost',user='welltime',passwd='123456',db='welltime')
#获取数据的时候以字典类型拿到
#cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
#获取数据以元组类似拿到
cur = conn.cursor()

sql = "update admin set name = %s where id = 1"

params = ('sb',)

reCount = cur.execute(sql,params)
conn.commit()

#conn.rollback()

cur.close()
conn.close()

print reCount
'''

'''
import MySQLdb

#创建连接
conn = MySQLdb.connect(host='localhost',user='welltime',passwd='123456',db='welltime')
#获取数据的时候以字典类型拿到
cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
#获取数据以元组类似拿到
#cur = conn.cursor()


sql = "insert into admin(id,name,address) values(%s,%s,%s)"

params = [
    ('4','alex','usa'),
    ('5','sb','usa'),
]

reCount = cur.executemany(sql,params)
conn.commit()

#conn.rollback()

cur.close()
conn.close()

print reCount
'''

import MySQLdb

#创建连接
conn = MySQLdb.connect(host='localhost',user='welltime',passwd='123456',db='welltime')

#获取数据的时候以字典类型拿到
cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
#获取数据以元组类似拿到
#cur = conn.cursor()


reCount = cur.execute('select * from admin')
nRet = cur.fetchall()


cur.close()
conn.close()

print reCount
print nRet
