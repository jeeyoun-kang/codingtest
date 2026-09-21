from collections import defaultdict
def solution(clothes):
    b = defaultdict(list)
    for i in range(len(clothes)):
        b[clothes[i][1]].append(clothes[i][0])

    #b = {'상의': ['흰티','검티'], '하의': ['청바지']}

    answer = 1

    for kind in b: #종류별씩 돌기
        answer *= len(b[kind])+1 # 그 종류의 갯수
    answer -=1 # 모두 안입는 경우 제외

    return answer

#라이브러리 쓰지않은 해시 버전

def sol2(clothes):
    clothes_type = {}

    for c,t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2 # 안입는거까지 추가해서 2로 세팅
        else :
            clothes_type[t] +=1

    # clothes_type = {'상의': 3, '하의': 2}

    cnt = 1
    for num in clothes_type.values():
        cnt *= num
    
    return cnt -1 # 모두 안입는 경우 제외

#Counter 버전

from collections import Counter

def sol3(clothes):
    # 종류별 개수(리스트기에 이런식으로 써야지 분류가능) - kind 뽑을것, name 쪼개는 규칙

    cnt = Counter(kind for name, kind in clothes)  
    # cnt = Counter({'상의': 2, '하의': 1})

    answer = 1
    for num in cnt.values():
        answer *= num + 1
    answer -= 1

    return answer