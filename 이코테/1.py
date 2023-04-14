import sys

input = sys.stdin.readline

t = int(input())
P = []
num_list = []
for i in range(t):
    P.append(input().strip())
    n = int(input())
    num_list.append(list(input()))
print(num_list)
# for j in range(t):
#     test = "".join(P[j])
#     print(test)
#     test=test.pop()
#     if test == 'R':
#         test2 = num_list[j]
#         test2 = test2[::-1]
#         num_list[j] = test2
#     else:
#         test3 = num_list[j]
#         test3 = test3.pop()
#         num_list[j] = test3
