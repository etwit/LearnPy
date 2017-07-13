#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月5日

@author: Ethan Wong
'''
import sys
retry_count = 0
retry_limit = 3
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'

#只要重试不超过3次就不断循环
while retry_count < retry_limit: 
    
    username = raw_input('Username:')
    #当用户输入用户名后，打开lock文件以检查是否此用户已经lock了
    lock_check = file(lock_file) 
    
    #循环lock文件
    for line in lock_check.readlines(): 
        line = line.split()
        if username == line[0]:
            #如果LOCK了就直接退出
            sys.exit('User %s is locked!' % username)
    
    passwd = raw_input('Password:')
    
    #打开账号文件
    f = file(account_file,'r+b')
    #默认为Flase，如果用户match上了，就设置为True
    match_flag = False 
    for line in f.readlines():
        #去掉每行多余的\n并把这一行按空格分成两列；分别赋值为user,passwd两个变量
        user,password = line.strip('\n').split()
        #判断用户名和密码是否都相等
        if username == user and password == passwd:
            print 'Match!',username
            #相等就把循环外的match_flag变量改为了True
            match_flag = True
            break
    f.close()
    
    #如果match_flag还为False，代表上面的循环中根本就没有match上用户名和密码，所以需要继续循环
    if match_flag == False:
        #如果match_flag还为False,代表上面的循环中跟本就没有match上用户名和密码，所以需要继续循环
        print 'User Or Password unmatched!'
        retry_count +=1
    else:
        print "Welcome login OldBoy Learning system!"
else:
    print 'Your account is locked!'
    f = file(lock_file,'a+b')
    f.write(username)
    f.close()