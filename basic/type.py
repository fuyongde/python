'''
整数

Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。
计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。
'''
print(0xff00);

'''
浮点数

浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。
整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。
'''

#字符串
print("I'm OK");
#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，可以在Python的交互式命令行用print()打印字符串看看：
print("I\'m \"OK\"!");
print("\\");
print("I'm learning\nPython");

print('\\\n\\');
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：
print(r'\\\t\\');

#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容，可以自己试试：
print('''line1
line2
line3''');

#布尔值True、False
print(3>5);
print(3<5);

#and运算
print("True and True is", True and True);
print("True and False is", True and False);
print("False and False is", False and False);

#or运算
print("True or True is", True or True);
print("True or False is", True or False);
print("False or False is", False or False);

#not运算
print("not True is",  not True);
print("not False is", not False);

age = 18;
if age >= 18:
    print('成年人');
else: 
    print('未成年人');

'''
空值

空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，我们后面会继续讲到。
'''

a = 123;
print(a);
a = "abc"
print(a);

PI = 3.14159265359;
print(PI);

print(10 / 3);
print(10 // 3);
print(10 % 3);