def solution(happy, angry, sad, joy, song):
    emotions = [happy, angry, sad, joy]
    emo_dict = {"happy": 0, "angry": 1, "sad": 2, "joy": 3}
    result = []

    for line in song:
        count = [0, 0, 0, 0]
        words = line.split()
        for word in words:
            for idx, emo_words in enumerate(emotions):
                if word in emo_words:
                    count[idx] += 1
        max_emotion = count.index(max(count))
        result.append(list(emo_dict.keys())[max_emotion])

    return result


# Test case
happy1 = ["charmed", "cheerful", "satisfied"]
angry1 = ["upset", "mad", "raging"]
sad1 = ["dry", "ugly"]
joy1 = ["cool", "delighted"]
song1 = ["charmed dry cool cheerful", "cool mad cheerful cool", "dry dry cool"]
print(solution(happy1, angry1, sad1, joy1, song1))  # Output: ['happy', 'joy', 'sad']

happy2 = ["good", "thrilled"]
angry2 = ["annoyed"]
sad2 = ["mournful", "melancholy"]
joy2 = ["gladness"]
song2 = ["mournful gladness mournful", "annoyed gladness good thrilled", "mournful melancholy melancholy"]
print(solution(happy2, angry2, sad2, joy2, song2))  # Output: ['sad', 'happy', 'sad']
