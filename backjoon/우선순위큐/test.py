#두 개의 파일을 계속 합하여 최종적으로 하나의 파일을 완성하는데 필요한 비용의 최소 총합
import sys
import heapq
input = sys.stdin.readline
t =int(input())

for _ in range(t):
    k = int(input())
    file = list(map(int, input().split()))
    heapq.heapify(file)
    result = 0
    while len(file) >= 2:
        f = heapq.heappop(file)
        s = heapq.heappop(file)
        result += f + s
        heapq.heappush(file, f + s)
    print(result)
