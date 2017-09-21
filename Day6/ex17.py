#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月18日

@author: Ethan Wong
'''
import paramiko

private_key_path = '/home/auto/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(private_key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('182.92.219.96 ', 22, 'wupeiqi', 'xxxx', key)

stdin, stdout, stderr = ssh.exec_command('df')
print stdout.read()
ssh.close();

