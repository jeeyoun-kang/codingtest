
#회전에 의해 위치가 바뀐 숫자들 중
#가장 작은 숫자들을 순서대로 배열에 담아 return

def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for i in range(columns)] for j in range(rows)] #행렬
    num = 1
    for row in range(rows):
        for column in range(columns):
            matrix[row][column]=num
            num+=1

    for x1,y1,x2,y2 in queries:
        tmp = matrix[x1-1][y1-1]
        mini = tmp

        for k in range(x1-1,x2-1): #왼쪽 세로
            test = matrix[k+1][y1-1]
            matrix[k][y1-1] = test
            mini = min(mini,test)

        for k in range(y1 - 1, y2 - 1):  # 하단 가로
            test = matrix[x2 - 1][k + 1]
            matrix[x2 - 1][k] = test
            mini = min(mini, test)

        for k in range(x2 - 1, x1 - 1, -1):  # 왼쪽 세로
            test = matrix[k - 1][y2 - 1]
            matrix[k][y2 - 1] = test
            mini = min(mini, test)

        for k in range(y2 - 1, y1 - 1, -1):  # 상단 가로
            test = matrix[x1 - 1][k - 1]
            matrix[x1 - 1][k] = test
            mini = min(mini, test)

        matrix[x1 - 1][y1] = tmp  #matrix[x1-1][y1-1]값에는 값이 바뀌기전 값이 입력되어야함
        answer.append(mini)
    return answer




