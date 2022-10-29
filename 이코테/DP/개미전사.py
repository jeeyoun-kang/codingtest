# 정수 N을 입력 받기
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(DP) 진행 (보텀업)
d[0] = array[0]  #첫번째에서 최댓값은 첫번째 값
d[1] = max(array[0], array[1])  #두번재에서 최댓값은 첫째,둘째 중 맥스값
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])


#피보나치 수열과 같은 점화식을 이용해 풀어야한다.