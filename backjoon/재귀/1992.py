import sys
input = sys.stdin.readline


n = int(input())
tree=[list(map(int,input().strip())) for _ in range(n)]

def dfs(x,y,n):
    check = tree[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=tree[i][j]: #다른경우
                check=-1
                break
    if check == -1:   # 범위안에 한개라도 다른경우는 4분할으로 나눠서 다시 검색
        print("(",end="")
        n = n//2
        dfs(x,y,n) #1사분면
        dfs(x,y+n,n)#2사분면
        dfs(x+n,y,n)#3사분면
        dfs(x+n,y+n,n)#4사분면
        print(")",end="")

    elif check==1:
        print(1,end="")
    else:
        print(0,end="")


dfs(0,0,n) # tree[0][0]