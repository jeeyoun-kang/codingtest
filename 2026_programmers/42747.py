# h의 최댓값이 리턴값
# h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하

def solution(citations):
    answer = 0 #최소값으로 세팅

    cnt = 1
    while(cnt <= len(citations)):

        #h번 이상 인용된 논문 h편 이상 && 나머지 논문이 h번 이하
        # 나머지 논문 h 이하는 h를 최대값으로 잡으면 저절로 성립됌
        if(cnt<= sum(x >= cnt for x in citations)):
            # answer에 max값으로 넣기
            answer = max(answer,cnt)

        cnt+=1

    print(answer)
    return answer

solution([3,0,6,1,5])

#정렬 + enumerate 버전

def sol2(citations):
    citations.sort(reverse = True) # 내림차순 정렬
    h = 0
    for i,c in enumerate(citations):
        if c>=i+1: #i+1번째 논문이 i+1회 이상일때
            h = i+1
        else:
            break
    return h