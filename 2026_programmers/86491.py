#명함 수납할수 있는 가장 작은 지갑

# 가로를 길게, 세로를 짧게 

def solution(sizes):
    x = -float("inf")
    y = -float("inf")
    for a,b in sizes:
        if(a<b):
            a,b = b,a
        x = max(x,a)
        y = max(y,b)

    return x*y