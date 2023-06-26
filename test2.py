S = "NAANAAXNABABYNNBZ"*10000
S = list(S)
cntA = 0
cntN = 0
cntB = 0
result = 0
for i in range(len(S)):
    if S[i] == "A" or S[i] == "N" or S[i] == "B":
        if S[i]=="A":
            cntA+=1
        elif S[i]=="N":
            cntN+=1
        else:
            cntB+=1

while(cntA>=3 and cntB>=1 and cntN>=2):
    result+=1
    cntA-=3
    cntN-=2
    cntB-=1

print(result)

