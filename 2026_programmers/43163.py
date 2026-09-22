#bfs
from collections import deque

def solution(begin, target, words):

    #타킷이 목록에 없음 리턴 0
    if target not in words:
        return 0
    

    q = deque()

    q.append((begin,0)) #현 단어, 변환 횟수

    visit = set()
    visit.add(begin) #begin넣어서 방문하지않게 함

    while q:
        word, cnt = q.popleft()

        #타깃될때 리턴
        if word == target:
            return cnt

        for w in words:
            # zip : 같은 인덱스 문자끼리 짝지음
            # sum은 true 갯수 더하기에 다른거 하나니깐 1로 조건 확인
            #if w not in visit and sum(x!= y for x,y, in zip(word, w)) == 1:
            
            # 슬라이싱 : 하나만 같은게 있음(다른거 하나) 되는 조건
            if w not in visit and any(word[:j] == w[:j] and word[j+1:] == w[j+1:] for j in range(len(word))):

                visit.add(w)
                q.append((w,cnt+1))
                   
    return 0