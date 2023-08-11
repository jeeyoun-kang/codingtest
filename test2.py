#deque나 stack을 이용해 풀어보기
def dfs(airport):
    air_test=[]
    airport_index=tickets.index(airport)
    visited[airport_index]=1 #방문표시
    for j in range(len(tickets)):
        if visited[j]==0 and tickets[j][0]==tickets[airport_index][1]:
            for k in range(len(tickets)):
                if tickets[k][0]==tickets[j][1]:
                    air_test.append(tickets[j])
    air_test.sort()
    test2 = air_test[0]
    result.append(test2[1])
    print(result)
    dfs(air_test[0])
tickets=[["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]
# for i in range(len(tickets)):
#     if tickets[i][0] == "AAD":
#         print(tickets[i])
result=[]
test = []
visited = [0] * len(tickets)  # 방문 표시 배열
for i in range(len(tickets)):
    if tickets[i][0] == "ICN":
        test.append(tickets[i])
test.sort() #정렬로 문자열비교
result.append(test[0][0])
result.append(test[0][1])
print(dfs(test[0]))