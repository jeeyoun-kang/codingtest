def solution(s, skip, index):
    alpha = list(range(1,27)) #소문자 알파멧 아스키코드를 1부터 시작으로 전환
    s = list(s)
    
    q = []
    for i in s:
        q.append(ord(i)-96)

    skip = list(skip)
    skip.sort()

    answer = []
    for i in q:
        cnt = 0
        while cnt < index : 
            i = i%26+1
            if chr(i+96) not in skip: 
                cnt +=1
        answer.append(chr(i+ 96))
    print(''.join(map(str,answer)))

    return ''.join(map(str,answer))

solution("mississippi","q",4)