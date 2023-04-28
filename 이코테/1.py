def solution(dirs):
    test = [[0, 0]]  #
    dx = 0
    dy = 0  # 현재위치
    for i in range(len(dirs)):
        if dirs[i] == "U":
            dy = dy + 1
            if -5 <= dy <= 5:
                test.append([dx, dy])

            else:
                dy = dy - 1
        elif dirs[i] == "D":
            dy = dy - 1
            if -5 <= dy <= 5:
                test.append([dx, dy])
            else:
                dy = dy + 1
        elif dirs[i] == "L":
            dx = dx - 1
            if -5 <= dx <= 5:
                test.append([dx, dy])
            else:
                dx = dx + 1
        else:
            dx = dx + 1
            if -5 <= dx <= 5:
                test.append([dx, dy])
            else:
                dx = dx - 1
        if test.count([dx, dy]) >= 2 and test.count(test[-2]) >= 2 and test[-1] != test[-2]:
            test.pop()
            test.pop()

    print(test)

    return len(test) - 1
