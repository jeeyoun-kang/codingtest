

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