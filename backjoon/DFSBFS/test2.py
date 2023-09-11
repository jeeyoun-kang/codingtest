def solution(ability):
    def DFS(L, s, ability, check):
        nonlocal answer
        n = len(ability)        # 학생 수
        m = len(ability[0])     # 종목 개수

        if L == m:
            answer = max(answer, s)   # 능력치 합의 최댓값을 구함
        else:
            for i in range(n):
                if check[i] == 0:
                    check[i] = 1
                    print(L,ability[i][L])

                    DFS(L+1, s + ability[i][L], ability, check)
                    check[i] = 0
    answer = 0        
    check = [0]*len(ability)
    DFS(0, 0, ability, check)      
    # Level, sum, ability, check
    # L : level (고를 수 있는 학생 수 중 몇 명째 선택한 것인지), sum : 능력치의 합
    
    return answer

solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]])