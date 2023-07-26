#n형 4열,각행의 4칸중 한칸만 밟으며 행을 내려와야한다
# 단 내려올때, 같은 열을 연속해서 밟을 수 없다
#밟은 값의 합의 최댓값 return
#각 행 중 가장 큰 수를 밟은 경우들을 구하고 최댓값 구하기

#dp
def solution(land):
    for j in range(1, len(land)):
        land[j][0] += max(land[j - 1][1], land[j - 1][2], land[j - 1][3])
        land[j][1] += max(land[j - 1][2], land[j - 1][3], land[j - 1][0])
        land[j][2] += max(land[j - 1][3], land[j - 1][0], land[j - 1][1])
        land[j][3] += max(land[j - 1][0], land[j - 1][1], land[j - 1][2])

    return max(land[-1])  # 마지막 줄의 max값

# 슬라이싱 이용
def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[len(land)-1])