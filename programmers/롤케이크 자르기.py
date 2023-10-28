from collections import Counter


topping=[1, 2, 1, 3, 1, 4, 1, 2]
dic = Counter(topping)

print(sorted(dic.items(), key=lambda x:-x[1]))
set_dic = set()
res = 0
for i in topping:
    dic[i] -= 1
    set_dic.add(i)
    if dic[i] == 0:
        dic.pop(i) #그부분을 제거한다. ex) 3:0 -> 아예 제거
    if len(dic) == len(set_dic):
        res += 1
print(res)

from itertools import product
a = [1,2,3,4]
b = [4,5,5,6]
print(list(product(a,b,repeat=3)))