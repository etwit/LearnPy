#!/usr/bin/env python
#encoding: utf-8
'''
Created on 2017年7月5日

@author: Ethan Wong
'''
print_num = input('Which loop do you want it to be printed out?')
count = 0

while count <1000000:
    if count == print_num:
        print 'There you got the number:', count
        choice = raw_input('Do you want to continue the loop?(y/n)')
        if choice == 'n':
            break
        else:
            while print_num <= count:
                print_num = input('Which loop do you want it to be printed out?')
                print "已经过了,sx!"
    else:
        print 'Loop:',count
    count +=1
else:
    print 'loop:',count