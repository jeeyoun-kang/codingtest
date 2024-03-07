# n = int(input()) #testcase
# for i in range(n):
#     test,cnt = list(map(int,input().split()))
#     test=list(str(test))
#     for k in range(cnt):
#         for j in range(len(test)-1,0,-1):
#             if test[j] == max(test):
#                 test[j], test[0] = test[0], test[j]
#                 break
#
#
test = [1,2,3,4,5]
for i in range(4,0,-1):
    print(i)
