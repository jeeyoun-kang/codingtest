#첫째줄에서 뽑은 집합과 밑에 집합과 일치할때 , 최대로 많이 뽑는 방법

import sys
input = sys.stdin.readline

n = int(input())
result=[0] #순서를 맞추기위한 맨 앞에 0 대입
compare_list=[] #dfs함수안에서 두 집합을 비교하기 위한 배열
cnt=0
final=0
def dfs(index,x): #첫째줄(인덱스) , 둘째줄(해당 값)
    global cnt
    if cnt==answer: #뽑을 수만큼 다 뽑은 경우
        if len(set(compare_list))*2 ==len(compare_list): # 두 집합이 일치하는 경우
            return True
    cnt+=1
    if x in result:
        return dfs(x,result[x]) #해당 인덱스 값으로 이동 후 재귀
    else:
        return


for i in range(n):
    a=int(input().rstrip())
    result.append(a)

result_set=set(result)
for j in range(len(result_set)-1,0,-1):
    answer=j
    compare_list.append(j)
    compare_list.append(result[j])
    for k in range(j):
        if dfs(j,result[j]) is True: #일치하는 경우
            final=j
            break
    if final!=0: #일치하는 경우
        break

print(final)
compare_list = compare_list.sort()  #오름차순 정렬
for k in range(final):
    print(compare_list[k])
