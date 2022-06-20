def solution(s):
    if len(s) in (4,6) and s.isdigit(): #isdigit()함수는 문자열이 숫자로 구성되어있는지 판별하는함수
        answer = True
    else:
        answer = False
    return answer