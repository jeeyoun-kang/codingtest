# 모든 트럭이 다리를 건너려면 최소 몇 초
# 다리 길이, 다리가 견딜수있는 무게(완전히 오르지않은 무게 제외), 트럭리스트

from collections import deque
def solution(bridge_length, weight, truck_weights):

    answer = 0

    q = deque(truck_weights) #대기 트럭
    bridge_queue = deque([0]*bridge_length) #다리를 칸으로 표현
    bridge_sum = 0 # 다리 위 무게 합

    while q : 
        answer +=1 # 1초 카운팅

        bridge_sum -= bridge_queue.popleft() #맨 앞칸이 다리에서 내림

        if bridge_sum + q[0] <= weight : # 다음 트럭도 올려도 되면
            truck = q.popleft()
            bridge_queue.append(truck)
            bridge_sum+=truck
        else:
            bridge_queue.append(0) #무게 초과면 빈칸 투입

    return answer + bridge_length #마지막 트럭 빠져나가는 시간 더해줌

solution(2,10,[7,4,5,6])

# 내리는 시각을 저장하는 방식 풀이
# 다리에 빈칸(0) 채우지 않고, 트럭마다 몇초에 내릴지 같이 저장하는 방식

def solution_2(bridge_length, weight, truck_weights):
    time = 0
    q = deque(truck_weights)
    bridge = deque()          # (트럭 무게, 내리는 시각)
    total = 0

    while q or bridge:        # 대기 트럭이나 다리 위 트럭이 남아 있으면
        time += 1
        if bridge and bridge[0][1] == time:          # 내릴 시각이 된 트럭
            total -= bridge.popleft()[0]
        if q and total + q[0] <= weight:             # 올릴 수 있으면
            truck = q.popleft()
            total += truck
            bridge.append((truck, time + bridge_length))

    return time

solution_2(2,10,[7,4,5,6])
