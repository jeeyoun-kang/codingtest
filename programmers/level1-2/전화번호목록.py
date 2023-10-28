
#pop()과 insert() -> 인덱스 조회 방식으로 시간 초과 해결

def solution(phone_book):
    phone_book.sort(reverse=True) #정렬시 근처 문자들이 비슷한 문자들로 구성될수밖에없음
    idx = len(phone_book) - 1  # phone_book의 마지막 요소부터 검사
    while idx > 0:
        key = phone_book[idx]  # 비교 대상
        if phone_book[idx - 1][:len(key)] == key:
            return False  # 바로 앞 숫자와 비교
        idx -= 1

    return True
solution(["123","456","789"])

