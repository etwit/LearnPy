#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月18日

@author: Ethan Wong
'''
#默认参数和可变参数
#如果有默认值得参数都放在后面
def foo(name,action='砍柴',where='北京'):
    print name,'去',where,action
    
foo('liyang','砍柴')
foo('alex','bb')
foo('zhangbing',where='上海')

