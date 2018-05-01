T = (6, 1,2,3,4)
M = ("SPAM", 1.0, [11,22,33], {('name', "王健")})
print(T)
print(T[1])

print(M)
print(M[1:3])

temp = list(T)
temp.sort()
T = tuple(temp)
print(T)