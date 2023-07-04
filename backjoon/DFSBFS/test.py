def solution(n, computers):
    def dfs(v):
        visited[v] = 1

        for j in range(n):  # 인접 노드
            if visited[j]==0 and computers[v][j]==1:  #인접한 노드중 방문하지 않은 노드가 있을때
                dfs(j)

    count = 0
    visited = [0] * (n)

    for i in range(n):
        if visited[i]==0:
            dfs(i)
            count += 1  # dfs 끝난 뒤 count

    return count
