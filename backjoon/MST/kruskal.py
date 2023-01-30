
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# find 연산
# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# union 연산
# 두 원소가 속한 집합을 합치기
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    #기존 노드의 부모노드의 값을 노드 번호가 작은 부모노드의 값으로 치환
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 간선 정보 담을 리스트와 최소 신장 트리 계산 변수 정의
edges = []
total_cost = 0

# 간선 정보 주어지고 비용을 기준으로 정렬
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선 정보 비용 기준으로 오름차순 정렬
edges.sort()

# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
for i in range(e):
    cost, a, b = edges[i]
    # find 연산 후, 부모노드 다르면 사이클 발생 X으므로 union 연산 수행 -> 최소 신장 트리에 포함!
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total_cost += cost

print(total_cost)