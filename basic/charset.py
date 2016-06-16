#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("包含中文的str");

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'));
print(ord('中'));

print(chr(66));
print(chr(25991));

#如果知道字符的整数编码，还可以用十六进制这么写str：
print('\u4e2d\u6587');

#Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x=b'ABC';
print(x);

print("ABC".encode('ascii'));
print("中文".encode("UTF-8"));
#python不支持中文进行ascii编码

print(b'ABC'.decode('ascii'));
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'));

#要计算str包含多少个字符，可以用len()函数：
print(len("ABC"));
print(len("中文"));

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len(b'ABC'));
print(len(b'\xe4\xb8\xad\xe6\x96\x87'));
print(len('中文'.encode("UTF-8")));

#格式化
#常见的占位符(%d整数、%f浮点数、%s字符串、%x十六进制整数)
print('Hi, %s, you have $%d.' % ('Jason', 1000000));

#格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print("%2d-%02d" % (3, 1));
print("%.2f" % 3.141592653879);

#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print("Age:%s.Gender:%s" % (25, True));

#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print("growth rate : %d %%" % 7);