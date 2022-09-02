import time

start_time = time.time()
count = 0
n, k = map(int, input().split())
while (n !=1):
    if n%k == 0:
        n //= k
        count +=1
    else:
        if(n ==2):
            count +=1
            break
        result = n%k
        n -= result
        count +=result
print(count)
# n, k = map(int, input().split())
#
# result = 0
#
# while True:
#     target = (n // k) * k
#     result += (n - target)
#     n = target
#
#     if n < k:
#         break
#     result += 1
#     n = n // k
#
# result += (n - 1)
# print(result)
end_time = time.time()
print("time=",end_time - start_time)
