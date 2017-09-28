#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月27日

@author: Ethan Wong
'''

#redis基本使用
'''
1.配置 redis.conf 守护进程后台常驻
daemonize yes

2.启动redis
/usr/local/reids/bin/redis-server /usr/local/redis/redis.conf

3.连接进入redis
/usr/local/redis/redis-cli -h 127.0.0.1 -p 6379

4.设置key value 键值对
set name 'alexli'
set name 'rain wang' EX 10

5.获取可以 value值
get name

6.列表
lpush mylist redis
lpush mylist mongodb
lpush mylist rabitmq

查看列表10个值内
lrange mylist 0 10

'''


