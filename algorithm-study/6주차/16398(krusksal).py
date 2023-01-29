import sys
input = sys.stdin.readline
# find 연산
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# union 연산
def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [i for i in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
edges = []

for a in range(n):
    for b in range(a + 1, n):
        edges.append((graph[a][b], a, b))
# 간선 정보 비용 기준으로 오름차순 정렬
edges.sort()
total_cost = 0
# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
for k in range(len(edges)):
    cost, a, b = edges[k]
    # find 연산 후, 부모노드 다르면 사이클 발생 X으므로 union 연산 수행 -> 최소 신장 트리에 포함!
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total_cost += cost

print(total_cost)
