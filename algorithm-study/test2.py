from sys import stdin
n = int(stdin.readline()) #n개의 노드
tree = [[0]*3 for _ in range(n)]
#visit = [[0]*3 for _ in range(n)] #자식노드 방문 여부 확인 리스트
for i in range(n):
    tree[i]=list(map(int,stdin.readline().split()))
parent = 0  # 부모노드 저장
count=0 #이동 횟수
node=0 #이동기
if tree[0][1]!=-1: #자식노드 여부 확인
    node=tree[0][1]

    count+=1
    parent=1

else:
    if tree[0][2]!=-1:
        node=tree[0][2]

        count+=1
        parent = 1
if count!=0:
    while True:


        if tree[node-1][1] != -1 :

            parent = node
            node = tree[node-1][1]
            count += 1

        elif tree[node-1][2]!=-1 :

            parent = node
            node = tree[node - 1][2]
            tree[node - 1][2] = -1
            count += 1


        else: # 부모노드로 가기
            node=parent
            count+=1


else: #루트노드만 있는경우 확인
    print(0)





