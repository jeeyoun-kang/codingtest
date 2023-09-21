def solution(phone_book):
    cnt=0
    while cnt<len(phone_book):
        v = phone_book.pop(cnt)
        for i in range(len(phone_book)):
            if v == phone_book[i][:len(v)]:
                return False
        phone_book.insert(cnt,v)
        cnt+=1
    return True

#pop()과 insert() -> 인덱스 조회 방식으로 시간 초과 해결

def solution(phone_book):
    phone_book.sort(reverse=True)
    idx = len(phone_book) - 1  # phone_book의 마지막 요소부터 검사
    while idx > 0:
        key = phone_book[idx]  # 비교 대상
        if phone_book[idx - 1][:len(key)] == key: return False  # 바로 앞 숫자와 비교
        idx -= 1

    return True


