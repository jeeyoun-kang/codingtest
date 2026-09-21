# 순열로 중복없이 담아서 소수판별
from itertools import permutations

def solution(numbers):
    numbers = list(numbers)

    #소수 판별 람다함수
    is_prime = lambda n: n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

    primes = set()   # answer 대신 set
    for j in range(len(numbers)):
        for i in permutations(numbers, j+1):
            s = int(''.join(i))
            if is_prime(s):
                primes.add(s)   # 중복은 자동으로 하나만

    return len(primes)

solution("17")