#round() - 두번째 인자 없을시, 소수점 첫째자리에서 반올림, 인자 존재시, 인자자리에서 반올림
print(round(1223.556,2))

a=7
b=3
print(a/b) #나누기
print(a%b) #나머지
print(a//b) #몫

print(a**b) #거듭제곱

#인덱싱과 슬라이싱

a=[1,2,3,4,5,6,7,8,9]
print(a[-1]) #뒤에서 첫번째 원소
print(a[-3]) #뒤에서 세번째 원소
print(a[1:4]) # a[1]원소부터 a[3] 원소까지

#리스트 컴프리헨션 - 리스트안에 조건문+반복문을 넣어 리스트 초기화하는 방식
array=[i for i in range(20) if i%2==1]
print(array)

array=[i*i for i in range(1,10)]
print(array)

array=[[0]*4 for _ in range(3)]
print(array)

#리스트 관련 기타 메서드

a=[1,4,3]

a.append(2) # 삽입, O(1)
a.sort() #오름차순 정렬, O(NlogN)
a.sort(reverse=True) #내림차순 정렬
a.reverse() #원소 순서 뒤집기, O(n)
a.count(3) #특정 값을 가지는 데이터 개수, O(n)
a.remove(1) #특정 값을 가지는 원소 삭제, O(n)

#특정 값만 제거

a= [1,2,3,4,5,5,5]
remove_set = [3,5]

#remove_set에 포함되지 않은 값만을 저장
result= [i for i in a if i not in remove_set]
print(result)

#튜플 자료형 - 소괄호 이용
#튜플에서 한번 선언된 값은 변경 불가

a=(1,2,3,4)
# a[2]=7

#사전 자료형- {key:value} , 내부적으로 해시테이블로 구성 -> 데이터 검색/수정 - O(1)
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)

#사전 자료형 관련 함수
key_list = data.keys()
value_list = data.values()
print(key_list,value_list)

#집합 자료형 - 중복허용x, 순서x
#set(), {} , O(1)
data = set([1,1,2,3,4,5])
print(data)

#집합 관련 연산
a=set([1,2,3,4,5])
b=set([1,3,5,7,9])
print(a|b) #합집합
print(a&b) #교집합
print(a-b) #차집합

a.add(6) #원소 추가
a.update([7,8]) #여러 원소 추가
a.remove(3) #특정 값의 원소 삭제
print(a)

if a == {1,4,2,5,6,7,8}:
    print(True)

#여러 타입을 같이 출력
answer = 7
print("정답은",answer,"입니다")
print("정답은"+str(answer)+"입니다")
print(f"정답은{answer}입니다")