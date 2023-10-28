def solution(office, r, c, move):
    # 방향 북, 동, 남, 서
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    n = len(office)
    cleaned = 0
    location = 0  #북

    # 현재 위치의 먼지 청소
    cleaned += office[r][c]
    office[r][c] = 0

    for action in move:
        if action == "go":
            nr, nc = r + dr[location], c + dc[location]
            if 0 <= nr < n and 0 <= nc < n and office[nr][nc] != -1:
                r, c = nr, nc
                cleaned += office[r][c]
                office[r][c] = 0
        elif actㄴion == "right":
            location = (location + 1) % 4
        elif action == "left":
            location = (location - 1) % 4

    return cleaned