import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white,blue=0,0

def cnt(x, y, n) :
  global white,blue
  color = paper[x][y]
  for i in range(x, x+n) :
    for j in range(y, y+n) :
      if color != paper[i][j] :
        cnt(x, y, n//2)
        cnt(x, y+n//2,n//2)
        cnt(x+n//2, y, n//2)
        cnt(x+n//2, y+n//2, n//2)
        return
  if color == 0:
    white+=1
  else :
    blue+=1


cnt(0,0,n)
print(white)
print(blue)