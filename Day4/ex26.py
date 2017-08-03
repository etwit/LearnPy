#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月3日

@author: Ethan Wong
'''
#异常处理

#测试规范 xxx/xxx
data = raw_input('请输入地址：')
array = data.split('/')
try:
    userspance = __import__('function4.'+array[0])
    model = getattr(userspance, array[0])
    func = getattr(model,array[1])
    func()
#except (ImportError,AttributeError),e:
except ImportError,e:
    print 1,e
    print '跳转到自己定义的404'

except AttributeError,e:
    print 2,e
    print '跳转到自己定义的404'
    
#囊括所有错误
except Exception,e:
    print 3,e
    print '跳转到自己定义的404'
else:
    print '没有出错！'
    
finally:
    print '无论异常与否，都会执行！'
    


