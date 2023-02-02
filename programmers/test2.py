from collections import deque
test = [1,2,3]
test2 = [2,3,4]
test=deque(test)
test2=deque(test2)
print(test2.append(test.popleft()))
print(test2)
print(test)