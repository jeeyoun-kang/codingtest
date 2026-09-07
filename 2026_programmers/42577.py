#특정 번호가 다른 번호의 접두어일때 false

#hash - O(n)
#set()으로 만들고 in으로 찾으면 O(1)로 찾기가능
def solution(phone_book):
    phone_set = set(phone_book) #o(n)

    for number in phone_book: #o(n)
        for i in range(1, len(number)):
            if number[:i] in phone_set : #O(1)(O(L)-L은 문자열길이)
                return False
    return True

#sort - o(nlogn) - sort()
def sort_solution(phone_book):
    phone_book.sort() #O(nlogn)
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

solution(["119", "97674223", "1195524421"])