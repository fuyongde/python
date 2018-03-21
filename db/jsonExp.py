# -*- coding: utf-8 -*-
import json

#obj = {'userId':1368, 'userType':2, 'title':'自定义标题' ,'content':'自定义内容', 'customerId':1027, 'customerName':'王中财', 'investId':1111}

title = '这是自定义标题'
content = '这是内容'
userIds = [1368, 792]

# 用户类型，2=员工|3=便利店
userType = 2

investId = 1111

customerId = 1027
customerName = '王中财'

obj = {'userIds':userIds, 'userType': userType, 'title':title ,'content':content, 'customerId':customerId, 'customerName':customerName, 'investId':investId}

json_str = json.dumps(obj)

print (json_str)