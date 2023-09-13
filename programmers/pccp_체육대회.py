def solution(ability):
    def DFS(L, s, ability, check):
        nonlocal answer # nonlocal : 중첩 함수 내에서 상위 함수의 변수를 사용할 떄 사용
        n = len(ability)
        m = len(ability[0])

        if L == m:
            answer = max(answer, s)
        else:
            for i in range(n):
                if check[i] == 0:
                    check[i] = 1
                    DFS(L + 1, s + ability[i][L], ability, check)
                    check[i] = 0

    answer = 0
    check = [0] * len(ability)
    DFS(0, 0, ability, check)

    return answer

solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]])



