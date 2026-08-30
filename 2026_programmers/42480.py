def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    one_score = 0
    two_score = 0
    three_score =0

    for i in range(len(answers)) : 
            if(answers[i] == one[i%len(one)]):
                one_score+=1
            if(answers[i] == two[i%len(two)]):
                two_score+=1

            if(answers[i] == three[i%len(three)]):
                three_score+=1
    scores = [one_score, two_score, three_score]
    highest = max(scores)

    answer = []
    for i in range(len(scores)):
        if scores[i] == highest:      # 최고점과 같은 사람 다 담기(인덱스 순이라 자동 오름차순)
            answer.append(i + 1)      

    return answer

solution([1,2,3,4,5])