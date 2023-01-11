from sys import stdin

#input = lambda: sys.stdin.readline().strip()
n = int(stdin.readline()) #n개의 노드
tree = [[0]*3 for _ in range(n+1)]

for i in range(1,n+1):
    tree[i]=list(map(int,input().split()))

parent = [0]*(n+1) #부모노드 저장하기 위한 리스트

count=0 #이동 횟수
node=1 #이동기 및 루트노드 시작
r=0 #노드의 위치 확인

while (tree[1][1]!=-1 and tree[1][2]!=-1): #루트노드의 자식들
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
result=0
test=0
#마지막 노드가 순회 끝이 아니였을때
node=tree[n][0]
while (node!=1): #노드가 루트노드일때 멈춤
    if parent.count(parent[node])!=2: #전체노드에서 한 노드라도 형제 노드가 없을때
        result=1

    node = parent[node]
    test += 1
if result==1:
    count+=test



print(count)




