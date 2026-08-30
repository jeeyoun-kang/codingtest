#조건 : numbers의 길이는 1 이상 100,000 이하
#조건을 기준으로 1초(10억)연산이 가능하게 만들어야됌

#단순 이중 for문이나 순열으로 구할시에 시간초과남
#이중 for문 O(n^2) = 10만*10만 = 100억
#순열 : O(n!) 

def solution(numbers):
    numbers = list(map(str, numbers))
    #조건이 각 자릿수가 1000이하여서 3번정도 곱한값
    #문자열이라 3 > 333, 30 > 303030 , 문자열아라 2번째에서 3이 이김
    answer = numbers.sort(key=lambda x: x * 3, reverse=True)
    return answer if answer[0] != '0' else '0'
    
solution([6,10,2])
