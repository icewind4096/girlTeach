str = 'abcdefg'
print(str[0])
print(str[0:-1])
print(str[-2])
print(str[0::2])
print(str[-1:1:-1])
print(len(str))

str = 'abc'
str = 'cde'+str
print(str)

str1 = ['abcdefg']
str2 = str1[:]
str3 = str1
print(str2)
print(str1 is str2)
print(str1 is str3)

for s in str3:
    print(s)
