
ingredient=[2,1,1,2,3,1,2,3,1]
s = []
cnt = 0
for i in ingredient:
    s.append(i)
    if s[-4:] == [1, 2, 3, 1]:
        cnt += 1
        for i in range(4):
            s.pop()
print(cnt)