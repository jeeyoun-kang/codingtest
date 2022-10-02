def solution(s):
    first = 0
    count = 0
    answer = []
    while(s!="1"):
        for i in s:
            if i == "0":
                count +=1
        s = s.split("0")
        s = "".join(s)
        s = len(s)
        s = ((bin(s))[2:])
        first +=1

    return [first,count]