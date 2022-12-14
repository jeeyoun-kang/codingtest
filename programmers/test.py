# # pop1번 , insert1번을 합해 1번이라한다.
# queue1= [3,2,7,2] #14
# queue2 = [4,6,5,1] #16
#
# number = (sum(queue1)+sum(queue2))//2
# test = queue1 - number
from collections import deque

test = deque([1,2,3,4])
print(test.popleft())
