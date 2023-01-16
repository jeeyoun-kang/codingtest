test=[]
# DFS 함수 정의
def dfs(graph, v, visited,count):

    # 현재 노드를 방문 처리
    visited[v] = True
    count+=1
    test.append(1)
    print(v, end=' ')
    print(count, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:

            # 만약 방문하지 않은 노드가 있다면
        if not visited[i]:
            test.append(1)
            # 탐색 시작
            dfs(graph, i, visited,count)
        #test.append(1)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],        # 0을 기준으로 연결되어 있는 노드
  [2,3], # 1을 기준으로 연결되어 있는 노드
  [4,5],
  [6,7],
  [],
    [],
    [],
[]

]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 탐색 시작 노드 1을 넣어주며 dfs() 실행
dfs(graph, 1, visited,0)
print(test)