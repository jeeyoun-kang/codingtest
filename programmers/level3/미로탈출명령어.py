import sys

sys.setrecursionlimit(10**5)

dirs = [["d", 1, 0], ["l", 0, -1], ["r", 0, 1], ["u", -1, 0]]


def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c) # 남은 이동 거리수
    # 가장 빠르게 도착한 경로로 return
    if dist > k:
        return "impossible"
    if dist % 2 != k % 2: # 남은 이동 거리수와 k가 서로 홀수거나 짝수여야 이동가능
        return "impossible"

    def dfs(y, x, path, cnt):
        if cnt == k and y==r and x==c:
            return path
        else:
            for prc in dirs:
                ny = y + prc[1]
                nx = x + prc[2]
                if 1 <= ny <= n and 1 <= nx <= m:
                    dist = abs(ny - r) + abs(nx - c)
                    if dist > k - (cnt + 1): #남은 이동수로 남은 거리를 갈수 있는지
                        continue
                    rtn = dfs(ny, nx, path + prc[0], cnt + 1)
                    if rtn is not None:
                        return rtn

    answer = dfs(x, y, "", 0)
    if answer is None:
        return "impossible"
    return answer

def solution(n, m, x, y, r, c, k):
    stack = [(x, y, [])]
    result = 'impossible'
    while stack:
        x_pos, y_pos, path = stack.pop()
        if len(path) == k and (x_pos, y_pos) == (r, c):
            result = ''.join(path)
            break
        remain, shortest_path = k - len(path), abs(x_pos - r) + abs(y_pos - c)
        if remain < shortest_path or remain % 2 != shortest_path % 2: # 남은 이동수가 이동할수 있는 수보다 작거나 / 남은 이동 거리수와 k가 모두 홀수거나 짝수가 아닐때
            continue
        if x_pos > 1:
            stack.append((x_pos - 1, y_pos, path + ['u']))
        if y_pos < m:
            stack.append((x_pos, y_pos + 1, path + ['r']))
        if y_pos > 1:
            stack.append((x_pos, y_pos - 1, path + ['l']))
        if x_pos < n:
            stack.append((x_pos + 1, y_pos, path + ['d']))
    return result