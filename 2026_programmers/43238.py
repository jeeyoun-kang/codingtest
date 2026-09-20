#모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.

def solution(n, times):

    result = float('inf')

    lo = times[0]        # 첫 사람 진입 시간 (네 tictok 초기값)
    hi = times[-1] * n   # 젤 느린 시간* 총 인원 수로 맥스로 세팅

    while lo <= hi:       # 모든 사람이 다 통과하는 시간 찾기

        tictok = (lo + hi) // 2   # 범위의 중간값을 기준

        # tictok까지 각 심사관이 처리한 인원 합
        cnt = 0
        for i in range(len(times)):
            cnt += tictok // times[i]

        if cnt >= n:              # 다 통과함 → 더 짧은 시간 후보 저장
            result = min(result, tictok) # 정답후보로 저장
            hi = tictok - 1             # 충분 -> 시간 줄임
        else:                     # 부족 → 시간 늘림
            lo = tictok + 1

    print(result)
    return result

solution(6, [7, 10])
