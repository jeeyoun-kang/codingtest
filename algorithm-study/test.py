# from sys import stdin
# v = int(stdin.readline()) #트리의 정점 개수
# tree=[]
# loc = [[0] for _ in range(v)]
# for i in range(v):
#     tree.append(list(map(int,stdin.readline().split())))
#
# for j in range(len(tree)):
#     k = 0
#     while(tree[j][k]==-1):
#         if k%2==1:
#             loc[j][k]+=tree[j][k]
#         k+=1

tree={1:[1,0]}
print(tree.get(0))