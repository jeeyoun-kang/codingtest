# 지도 크기 N, M 및 주사위 위치 x, y 입력
N, M, x, y, K = map(int, input().split())

# 지도 생성 및 초기화
map_data = []
for _ in range(N):
    map_data.append(list(map(int, input().split())))

# 주사위 초기화
dice = [0, 0, 0, 0, 0, 0]

# 주사위 이동 방향 (동, 서, 북, 남)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 굴리기
commands = list(map(int, input().split()))

for command in commands:
    nx, ny = x + dx[command - 1], y + dy[command - 1]

    if 0 <= nx < N and 0 <= ny < M:
        if command == 1:  # 동쪽
            dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
        elif command == 2:  # 서쪽
            dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
        elif command == 3:  # 북쪽
            dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        else:  # 남쪽
            dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

        if map_data[nx][ny] == 0:
            map_data[nx][ny] = dice[3]
        else:
            dice[3] = map_data[nx][ny]
            map_data[nx][ny] = 0

        x, y = nx, ny
        print(dice[0])