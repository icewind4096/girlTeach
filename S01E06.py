#字符串的find方法实现子字符串查找的操作
str1 = 'abcdefg'
print('a' in str1)
print(str1.find('cd'))
print(str1.find('zg'))


#替换操作运用的是replace方法
str1 = str1.replace('c', 'zz')
str1 = str1.replace('e', 'zz')
print(str1.replace('zz', '|', 1))
print(str1.replace('zz', '|'))

#字符串的提取功能，用split方法
str1 = 'Tom,21,USA,UCLA'
list=str1.split(',')
print(list)

#将列表中的元素连接成一个字符串,用join方法
list=['tom','cat','fish']
print(''.join(list))
print(','.join(list))

#去前后空格用strip方法
str1 = ' tom 21 usa ucla\r\n'
print(str1)
print(str1.strip())

#字符串的格式化输出
name = 'wangj'
age = 28
schools=['南京师范大学', '南京工业大学']
print('name:{},age:{},and school from {}'.format(name, age, schools))
print('name:{2},age:{1},and school from {0}'.format(schools, age, name))

print('float number = {:.2f}'.format(12.3456))
print('bin number = {:b}'.format(256))

#原始字符串 用r''表示
print('c:\new\s01e06.py')
print(r'c:\new\s01e06.py')

num1 = '19'
num2 = 3
print(int(num1) + 3)

print(float('1.5'))

print(str(123.12))
print(bin(12))
#十进制
print(int('111'))
#二进制
print(int('111',2))