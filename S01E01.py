#L1 = [1,2,3,4,5,6,7]
#L1_1=L1[0::2]
#print(L1)
#L1_1[0]="A"
#print(L1)
#print(L1_1)
#L1[0]="B"
#print(L1)
#print(L1_1)
#print(L1[3:-1])
#print(L1[3:-2])
#print(L1[3:-3])
#print(L1)
#print(L1[2:3])
#L2 = [1, 'spam', [2,3,4], "abc"]
#print(L2[2:-1])
#print(L2)
#print(L2[0:1])
#print(L2[1:2])
#print(L2[1:2][0][0:1])
#print(L2[2:3])
#print(L2[2:3][0][2:3])
#print(L2[3:4])
L3 = []
L3.append('ABC')
L3.insert(1, [1,2,3,4])
L3.extend([11,22,33])
print(L3)
L3[1:2][0].append('A1')
print(L3)
del L3[2:3]
print(L3)
print(L3[1:2][0])
L3[1:2][0].remove("A1");
print(L3)
print(L3[1:2].pop())
print(L3)
L3[1:2] = ["bb", "aa"]
print(L3)
L4=L3[0:3]
L4.sort()
print(L4)
L4.reverse()
print(L4)