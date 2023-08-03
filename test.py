from collections import deque
def bfs(graph, start_v):
    visited = [start_v]

    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    print(visited)
    return visited

graph = {
"A": ["B"],
"B": ["A", "C", "E"],
"C": ["B", "D"],
"D": ["C", "E", "F"],
"E": ["B", "D", "F"],
"F": ["D", "E"],
}
print(bfs(graph,'A'))