for x in [1,2,3]:
        print (x)

D = {}
D['姓名']='wangj'
D['性别']='男'
for item in D:
    print('{}----{}'.format(item, D[item]))

for name,sex in D.items():
    print('{}----{}'.format(name, sex))

#作用于输入序列的运算表达式；
a = [1,2,3,4,5,6,7,8,9]
b = [x**2 for x in a]
print(b)

#用列表a中所有能被3整除的元素来构造列表b
a = [1,2,3,4,5,6,7,8,9]
b = [x**2 for x in a if x % 3 == 0]
print(b)

#可以用字典以及列表等这些可以迭代的数据类型，来构造一个新的字典
D1 = {name:'_'+sex for (name,sex) in D.items()}
print(D1)