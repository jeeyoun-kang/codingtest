n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
answer = [0,0]
stack = [words[0]]
for i in range(1, len(words)):
    if stack[-1][-1] == words[i][0] and words[i] not in stack:
        print(stack[-1][-1])
        stack.append(words[i])
    else:
        answer[0] = (i % n) + 1
        answer[1] = i // n + 1
        print(answer)
        break
print(answer)
