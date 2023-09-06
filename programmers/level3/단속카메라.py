# 고속도로를 이동하는 차량의 경로 routes가 매개변수
# 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치
def solution(routes):
    # routes를 나간 지점 기준 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    print(routes)
    answer = 1

    camera = routes[0][1]

    # 현재 카메라가 설치된 위치보다 진입 지점이 뒤일때 -> 현재 차량의 나간 지점 = camera , answer 1 증가
    for i in range(1, len(routes)):
        if camera < routes[i][0]:
            camera = routes[i][1]
            answer += 1

    return answer



