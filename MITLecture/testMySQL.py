__author__ = 'joe'
# -*- coding: utf-8 -*-
import mysql.connector

conn = mysql.connector.connect(user='root', password='111', database='test')
cursor = conn.cursor()
# 创建user表
cursor.execute('create table user(id VARCHAR(20) primary key, name VARCHAR(20))')
# 插入一行记录，mysql占位符是%s
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'joe'])

# 提交事务
conn.commit()
cursor.close()
# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ['1'])
values = cursor.fetchall()
print(values)
conn.commit()
cursor.close()
