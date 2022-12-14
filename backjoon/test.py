a = [1,2,3,4,5]
while (len(a)!=1):
    a.pop(a.index(min(a)))
    print(a)
print(a)