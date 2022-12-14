survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
answer=''
scores = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
add_score = {1: 3, 2: 2, 3: 1, 4: 0, 5: -1, 6: -2, 7: -3}

for i in range(len(survey)):
    scores[survey[i][0]] += add_score[choices[i]]

answer += "R" if scores["R"] >= scores["T"] else "T"
answer += "C" if scores["C"] >= scores["F"] else "F"
answer += "J" if scores["J"] >= scores["M"] else "M"
answer += "A" if scores["A"] >= scores["N"] else "N"
print(answer)