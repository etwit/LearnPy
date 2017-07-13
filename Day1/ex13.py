'''
Created on 2017-07-04

@author: Ethon Wong
'''
name = raw_input('Please input your name:')
#age = input('age:')
job = raw_input('Job:')
salary = raw_input('salary:')

real_age = 30

for i in range(10):
    age = input('age:')
    if age >30:
        print 'think smaller'
    elif age == 30:
        print '\033[32;1m--------good!\033[0m'
        break
    else:
        print 'think bigger'
    print 'you still got %s shots!' % (9 - i)

print '''
Personal information of %s:
        Name:%s
        Age :%d
        Job :%s
        Salary:%s
------------------------------
''' % (name,name,age,job,salary)