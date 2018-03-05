#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql, json
 
# 打开数据库连接
db = pymysql.connect("192.168.1.66","fuyongde","fuyongde","quickstart" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT * FROM website")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()

json_str = json.dumps(data)

print (json_str)
 
# 关闭数据库连接
db.close()