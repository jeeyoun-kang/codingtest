s = "baabaa"
count=0
j=0
array = []
for i in s:
    array.append(i)
while(count!=len(s)):

    if array[j]==array[j+1]:
        array = array[:j-1]+array[:j+2]

    else:
        j+=1


