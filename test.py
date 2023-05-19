T = int(input())

for t in range(1, T+1) :
    N = int(input())
    result = [[0] * N for i in range(N)]

    i, j, index = 0, -1, 0
    dir = ["R", "D", "L", "U"]
    value = 1

    for k in range(N * N) :
        if dir[index] == "R" :
            j += 1
            if j >= N or result[i][j] != 0 :
                i += 1
                j -= 1
                index = 1
        elif dir[index] == "D" :
            i += 1
            if i >= N or result[i][j] != 0 :
                i -= 1
                j -= 1
                index = 2
        elif dir[index] == "L" :
            j -= 1
            if j < 0 or result[i][j] != 0 :
                i -= 1
                j += 1
                index = 3
        elif dir[index] == "U" :
            i -= 1
            if i < 0 or result[i][j] != 0 :
                i += 1
                j += 1
                index = 0
        result[i][j] = value
        value += 1

    print("#{}".format(t))
    for i in range(N) :
        print(*result[i])