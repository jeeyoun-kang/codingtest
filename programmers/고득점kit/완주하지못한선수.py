import collections


participant = ["mislav", "stanko", "mislav", "ana"] #참여
completion = ["stanko", "ana", "mislav"] #완주
hi =collections.Counter(participant)
test = collections.Counter(participant)-collections.Counter(completion)
print(list(hi.values()))