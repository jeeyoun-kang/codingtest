from sys import stdin
n = int(stdin.readline())
date = []
sample = [0 for _ in range(365)]
for i in range(n):
    date.append(list(map(int,stdin.readline().split())))

print(sample)
#포함 안된 숫자 확인하기
