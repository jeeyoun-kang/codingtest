from collections import deque
n=int(input()) # 컴퓨터 개수
v=int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] # 그래프 초기화
visited=[0]*(n+1) # 방문한 컴퓨터인지 표시
for i in range(v): # 그래프 생성
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향
count=0
def dfs(v):
    global count
    visited[v]=1
    for nx in graph[v]: #인접한 노드 탐색
        if visited[nx]==0:
            dfs(nx)
            count+=1
def bfs(v):
    global count
    visited[v]=1
    Q=deque([v])
    while Q:
        v =Q.popleft()
        for i in graph[v]:
            if (visited[i]==0):
                visited[i]=1
                Q.append(i)
                count+=1
#bfs(1)
bfs(1)
#print(sum(visited)-1)
print(count)