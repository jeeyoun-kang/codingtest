def solution(total_sp, skills):
    graph = {}
    for s, t in skills:
        if s not in graph:
            graph[s] = []
        graph[s].append(t)

    def dfs(skill):
        if skill not in graph:
            return 1

        points = 0
        for next_skill in graph[skill]:
            points += dfs(next_skill)

        return points

    skill_points = {}
    for i in range(1, len(skills) + 2):
        skill_points[i] = dfs(i)

    total_points = sum(skill_points.values())
    factor = total_sp / total_points

    result = [int(skill_points[i] * factor) for i in range(1, len(skills) + 2)]
    return result


# 예시 호출
total_sp = 121
skills = [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]
print(solution(total_sp, skills))  # [44, 11, 33, 11, 11, 11]
