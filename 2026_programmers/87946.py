# 최소 피로도: 탐엄하기위한 가져야되는 피로도, 소모 피로도: 탐험후 소모되는 피로도

#유저의 현피로도 :k, [최소, 소모피로도] : dan~

# 유저가 탐험 가능한 최대 던전 수 리턴
# 탐험 던전 순서를 가장 최대로 돌수있는 순으로 값 리턴

# 최소 피로도와, 그다음 최소피로도중 멀 선택할건지 결정 후에,
# 뒤에 소모피로도를 비교해야될듯? 
# [60-a,40-a,70-a]

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)

    for order in permutations(dungeons):   # 모든 탐험 순서
        fatigue = k
        count = 0
        for need, cost in order:
            if fatigue >= need:            # 최소 피로도 만족하면 탐험
                fatigue -= cost            # 소모 피로도만큼 감소
                count += 1
        answer = max(answer, count)

    return answer

#DFS 백트래킹 버전
def solution(k, dungeons):
    n = len(dungeons)
    visited = [0] * n
    answer = 0

    def dfs(fatigue, count):
        nonlocal answer #안쪽에서 수정된 값을 바깥함수로 꺼내는 타입

        answer = max(answer, count)          # 지금까지 돈 개수 갱신

        for i in range(n):
            need, cost = dungeons[i]
            if not visited[i] and fatigue >= need:  # 안 간 던전 + 들어갈 수 있으면
                visited[i] = 1                    # 방문 표시
                dfs(fatigue - cost, count + 1)       # 들어가서 탐험 이어감
                visited[i] = 0                   # ★ 되돌리기(백트래킹)

    dfs(k, 0)
    return answer