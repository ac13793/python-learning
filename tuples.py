d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print("d.items():", d.items())
print(t)

print("************Traversing a dictionary************")
print("***********Method #1****************")
for key in list(d.keys()):
    print(key, d[key])

print("***********Method #2****************")
for key, val in list(d.items()):
    print(key, val)