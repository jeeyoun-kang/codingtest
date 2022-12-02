cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
n = input()
count=0
i=0
while(i!=len(n)):
    if n[i:i+2] in cro:
        if "=" in n[i:i+2]:
            count+=1
        else:
            count+=2
        i+=2
    elif n[i:i+3] in cro:
        if "=" in n[i:i+3]:
            count+=2
        else:
            count+=3
        i+=3
    else:
        i+=1
print(count)