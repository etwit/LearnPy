#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月17日

@author: Ethan Wong
'''
#模块，对于Python来说如果想导入某一个文件夹下的.py文件函数，
#要在该文件夹下创建_init_.py变成包即可导入

#至关重要的__init__.py
#是否为主文件：__name__
#    if __name__ == '__main__':
#        pass
#当前文件路径：__file__
#当前文件描述：__doc__

from function import test
test.Foo()

print 'ex3',__name__

if __name__ == '__main__':
    pass

print __file__
print __doc__
