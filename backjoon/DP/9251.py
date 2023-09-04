import sys
input = sys.stdin.readline

char1 = input().strip()
char2 = input().strip()
cache = [[0] * (len(char2)+1) for _ in range(len(char1)+1)]

for i in range(1, len(char1)+1):
    for j in range(1, len(char2)+1):
        if char1[i-1] == char2[j-1]:
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i][j-1], cache[i-1][j])
print(cache[-1][-1])


# char1= input().strip()
# char2 = input().strip()
# cache = [0] * len(char2)
#
# for i in range(len(char1)):
#     cnt = 0
#     for j in range(len(char2)):
#         if cnt < cache[j]:
#             cnt = cache[j]
#         elif char1[i] == char2[j]:
#             cache[j] = cnt + 1
# print(max(cache))