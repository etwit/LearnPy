#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月18日

@author: Ethan Wong
'''
#防止别人调用我

#函数式编程
#函数有参数，有返回值

#默认参数 和可变参数


def login(username):
    if username == 123:
        return '登录成功！'
    else:
        return '登录失败！'

def detail(user):
    print user,'你的详细信息！'

if __name__ == '__main__':
    user = raw_input('请输入名字:')
    res = login(user)
    if res == '登录成功':
        detail(user)
    else:
        print '奖金发放完了，你来晚了！'

from function import test