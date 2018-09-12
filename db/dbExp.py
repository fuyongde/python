# -*- coding: utf-8 -*-
import pymysql, json
 
# 打开数据库连接
db = pymysql.connect(host="192.168.1.66", user="fuyongde", passwd="fuyongde", db="quickstart", charset="utf8")
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

try:
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT * FROM `website`")
    
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()

    list = []

    for row in data:
        id = row[0]
        name = row[1]
        url = row[2]
        alexa = row[3]
        country = row[4]
        dict = {'id' : id, 'name' : name, 'url' : url, 'alexa' : alexa, 'country' : country}
        list.append(dict)

    print(json.dumps(list))

except:
   print ("Error: unable to fetch data")

# 关闭数据库连接
db.close()