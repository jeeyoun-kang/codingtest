N = int(input())
M = list(input() for _ in range(N))

for i in range(len(M)):
    result = []
    final = ""
    test = ""
    test+= str(M[i])
    result = test.split(" ")
    result.reverse() #result[::-1]와 같다  #reverse는 리스트에만 쓴다.
    #문자열은 stack써서 pop()으로 써서 문자열 뒤집어서 뽑아야될듯
    final = ' '.join(result)
    print("Case #"+str(i+1)+": "+final)