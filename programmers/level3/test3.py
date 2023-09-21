from collections import Counter

a = [1, 2, 4, 5, 6, 1, 1, 3, 4]
b = Counter(a)

# 값(value)을 기준으로 내림차순 정렬
sorted_b = sorted(b.items(), key=lambda item:(-item[1]))
print(sorted_b)