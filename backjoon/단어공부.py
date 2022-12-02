import collections
n = input()
b = n.upper()
n=list(b)
a = collections.Counter(b)
if len(n)==1:
    print(b)

elif a.most_common(1)[0][1] == a.most_common(2)[1][1]:
    print("?")
else:
    test = dict(a.most_common(1))
    print(a.most_common(1)[0][0])
