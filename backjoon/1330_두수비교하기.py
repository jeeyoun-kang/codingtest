A,B = map(int,input().split()) #공백을 기준으로 분리

if(A>B):
    print('>')
elif(A<B):
    print('<')
else:
    print('==')
