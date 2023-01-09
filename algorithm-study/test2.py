import sys
sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().strip()
n = int(input()) #n개의 노드
tree = [[0]*3 for _ in range(n+1)]

for i in range(1,n+1):
    tree[i]=list(map(int,input().split()))

parent = [0]*(n+1) #부모노드 저장하기 위한 리스트

count=0 #이동 횟수
node=1 #이동기 및 루트노드 시작
r=0 #노드의 위치 확인

while (node!=tree[n][0]): #마지막 노드 기준
    if tree[node][1] != -1 :
        parent[tree[node][1]] = tree[node][0]
        node = tree[node][1]
        count += 1

    elif tree[node][2]!=-1 :
        parent[tree[node][2]] = tree[node][0]
        node = tree[node][2]
        count += 1

    else: # 부모노드로 가기
        if tree[parent[node]][1] == node:
            r = 1
        elif tree[parent[node]][2] == node:
            r = 2
        node=parent[node]
        tree[node][r] = -1 #자식노드가 없거나 자식노드들 다 방문했을시
        count+=1

if parent.count(parent[tree[n][0]])!=2: #마지막 노드의 형제노드가 없을시
    count*=2

print(count)




