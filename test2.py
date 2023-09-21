numbers=[6, 10, 2]
numbers = list(map(str, numbers))
print(numbers)
#문자열 비교는 첫번째 문자를 아스키코드로 비교, 같을때는 두번째 문자값 비교
numbers.sort(key=lambda x : x*3,reverse=True)
print(numbers)