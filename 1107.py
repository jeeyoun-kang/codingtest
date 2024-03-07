A = [2, 3, 1, 2, 4, 3]
S = 7


n = len(A)
min_length = n + 1
start = 0
current_sum = 0

for end in range(n):
    current_sum += A[end]
    while current_sum >= S:
        min_length = min(min_length, end - start + 1)
        current_sum -= A[start]
        start += 1

if min_length == n + 1:
    print(0)
else:
    print(min_length)

# def solution(A, S):
#     n = len(A)
#     min_length = n + 1
#     start = 0
#     current_sum = 0
#
#     for end in range(n):
#         current_sum += A[end]
#         while current_sum >= S:
#             min_length = min(min_length, end - start + 1)
#             current_sum -= A[start]
#             start += 1
#
#     if min_length == n + 1:
#         return 0
#     else:
#         return min_length