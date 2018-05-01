D = {
        'name':{'first':'Bob', 'last':'Smith'},
        'job' : ['dev','mgr'],
        'age' : 0.5,
        'addr': 'BeiJing'
}
print(D)
print(D['job'][1:2])


D = {}
print(D)
D['name']="wangj"
D['sex']='male'
print(D)

keyList=["运动", "读书", "电影"]
valueList=["骑车","搜寻红十月", "饮食男女"]
D['favourite'] = dict(zip(keyList, valueList))
print(D)

D['favourite'].update(dict([("烹饪", "宫保鸡丁")]))
print(D)

if "烹饪" in D['favourite']:
        print(D['favourite']['烹饪'])

print(D.get('favourite').get('电影'))

print('爱好Key:', list(D['favourite'].keys()))
print('爱好Value:', list(D['favourite'].values()))
print('爱好Key-Value:', list(D['favourite'].items()))