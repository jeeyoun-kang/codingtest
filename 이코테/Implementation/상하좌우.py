

# nx = x + dx[i]
# ny = y + dyp[i]
# 처음시작(1,1)


nx = 1
ny= 1
N = int(input()) #공간 크기
data = list(map(str,input().split()))

for i in data:
    if i == "R":
        if ny != N:
            ny = ny + 1

        else:
            continue
    elif i == "L":

        if ny != 1:

            ny = ny - 1

        else:

            continue
    elif i == "U":
        if nx != 1:
            nx = nx - 1
        else:
            continue
    elif i == "D":
        if nx != N:
            nx = nx + 1
        else:
            continue

print(nx,ny)

# x,y라 해서 헷갈리지 말것 (1,1) (x,y)이다 오른쪽이 늘어나면 y가 늘어남
