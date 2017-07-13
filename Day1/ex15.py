#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年7月5日

@author: Ethon Wong
'''
import sys
print_num = 0
count = 0

while count <1000000:
    if count == print_num:
        print 'There you got the number:', count
        while print_num <= count:
            print_num = input('Which loop do you want it to be printed out?[input 0 to exit]')
            
            if print_num == 0:
                sys.exit('Exit the Program!')    
            if print_num <= count:
                print u"已经过了,sx!"
    else:
        print 'Loop:',count
    count +=1
else:
    print 'loop:',count