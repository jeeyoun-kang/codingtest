from collections import Counter
x = [1,1,1,1,2,2,2,3,3,4]
x = Counter(x)
print(x)
print(x.most_common(2))
