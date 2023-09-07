#딕셔너리로 보석 종류 확인 후, 끝 지점을 정한 다음, 시작 지점을 정한다.
def solution(gems):
    N = len(gems)
    answer = [0, N- 1]
    kind = len(set(gems))  # 보석종류
    dic = {gems[0]: 1}  # 종류 체크할 딕셔너리
    s, e = 0, 0  # 투포인터
    while s < N and e < N:
        if len(dic) < kind:  # 종류 부족하면 end point 증가 & dic 개수 증가
            e += 1
            if e == N:
                break
            dic[gems[e]] = dic.get(gems[e], 0) + 1

        else:  # 종류 같으면 ans 비교 후 답 갱신하고, start point 증가 & dic 개수 다운
            if (e - s + 1) < (answer[1] - answer[0] + 1):
                answer = [s, e]
            if dic[gems[s]] == 1:
                del dic[gems[s]]
            else:
                dic[gems[s]] -= 1
            s += 1

    answer[0] += 1
    answer[1] += 1
    return answer

# 리스트 슬라이싱은 객체를 n개 조회하기 때문에 O(n)
# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
#
# gems_cnt= set(gems)
# start,end = 0,len(gems)-1
#
# while True:
#     if len(set(gems[start:end]))==len(gems_cnt):
#         end-=1
#     else:
#         break
#
# while True:
#     if len(set(gems[start+1:end+1]))==len(gems_cnt):
#         start+=1
#     else:
#         break
# print(start+1,end+1)
