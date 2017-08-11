#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月4日

@author: Ethan Wong
'''

'''
Linux

安装mysql： apt-get install mysql-server
安装python-mysql模块：apt-get install python-mysqldb
Windows

下载安装mysql
python操作mysql模块：MySQL-python-1.2.3.win32-py2.7.exe 
或 MySQL-python-1.2.3.win-amd64-py2.7.exe
mysql图形界面：Navicat_for_MySQL
安装完成后，导入MySQLdb测试是否安装成功

数据库：
show databases;
use [databasename];
create database  [name];

数据表：
show tables;

create table students
    (
        id int  not null auto_increment primary key,
        name char(8) not null,
        sex char(4) not null,
        age tinyint unsigned not null,
        tel char(13) null default "-"
    );
    

增删改查:
insert into students(name,sex,age,tel) values('alex','man',18,'151515151')

delete from students where id =2;

update students set name = 'sb' where id =1;

select * from students

'''