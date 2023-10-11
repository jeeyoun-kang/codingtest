import sys
input = sys.stdin.readline
#일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.
#일관성 있는 목록인 경우에는 YES, 아닌 경우에는 NO
t = int(input())
for i in range(t):
    n=int(input())#전화번호수
    phone=[input().rstrip() for _ in range(n)]
    phone.sort()
    answer=0
    for j in range(n-1):
        #원소가 문자인 경우, 앞에서부터 아스키코드 순으로 정렬하기에 아래와 같이 비교해도 된다
        if phone[j]==phone[j+1][0:len(phone[j])]:
            answer=1
    if answer==1:
        print("NO")
    else:
        print("YES")