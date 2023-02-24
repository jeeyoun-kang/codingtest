import sys
input = sys.stdin.readline
n,r,c = map(int,input().split())
cnt=0
if r%2==0:
    if c%2==0: # (0,0)
        cnt+=((r - 0) * 4*r) + ((c - 0) * 4*c) + 0
    else: #(0,1)
        cnt+=((r - 0) * 4) + ((c - 1) * 4) + 1
else:
    if c % 2 == 0:  # (1,0)
        cnt+=((r - 1) * 4) + ((c - 0) * 4) + 2
    else:  # (1,1)
        cnt+=((r-1)*4) + ((c-1)*4) +3
print(cnt)