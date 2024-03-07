# def solution(user_times, T):
#     max_remaining_time = 0
#
#     for time in user_times:
#         remaining_time = T - (time % T)
#         max_remaining_time = max(max_remaining_time, remaining_time)
#
#     return max_remaining_time

# def solution(user_times, T):
#     max_remaining_time = 0
#
#     for time in user_times:
#         remaining_time = T - (time % T)
#         if remaining_time == T:
#             return 0
#         max_remaining_time = max(max_remaining_time, remaining_time)
#
#     return max_remaining_time

# def solution(user_times, T):
#     max_remaining_time = 0
#
#     for time in user_times:
#         remaining_time = T - (time % T)
#         if remaining_time == T:
#             max_remaining_time = 0
#             continue
#         max_remaining_time = max(max_remaining_time, remaining_time)
#
#     return max_remaining_time

# def solution(user_times, T):
#     max_remaining_time = 0
#
#     for time in user_times:
#         remaining_time = T - (time % T)
#         if remaining_time == T:
#             max_remaining_time = 0
#         else:
#             max_remaining_time = max(max_remaining_time, remaining_time)
#
#     return max_remaining_time

def solution(user_times, T):
    max_remaining_time = -1  # max_remaining_time을 -1로 설정하여 아직 값을 갱신하지 않았음을 나타냄

    for time in user_times:
        remaining_time = T - (time % T)
        if remaining_time == T:  # 주어진 주기의 배수인 경우
            max_remaining_time = max(max_remaining_time, 0)  # 기존의 최대 남은 시간과 0 중 더 큰 값을 선택하여 갱신
        else:
            max_remaining_time = max(max_remaining_time, remaining_time)  # 최대 남은 시간을 갱신

    return max_remaining_time
# Test cases
user_times1 = [20, 40, 65, 110]
T1 = 30
print(solution(user_times1, T1))  # Output: 25

user_times2 = [20, 40, 65, 110]
T2 = 1
print(solution(user_times2, T2))  # Output: 0

