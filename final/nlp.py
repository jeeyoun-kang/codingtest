# import spacy
#
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(u'jeeyoun is looking at buying U.K. startup for $1 billion')
# for token in doc:
#     print(token.lemma_)
import spacy
extest = ""
result = ""
repllast = "x"
nlp = spacy.load('en_core_web_sm')
sentences = 'jee youn is ate an apple'


doc = nlp(sentences)
for i in doc:

    if i.tag_ == 'NNP':
        result = str(i.text)
        test = len(i)*'x'
        sentences = sentences.replace(result,test)

sentences = list(sentences)
for j in range(len(sentences)):
    if sentences[j] == 'x' and sentences[j+1] == ' ' and sentences[j+2] == 'x':
                repllast,sentences[j+1] = sentences[j+1],repllast
                # sentences = ','.join(sentences)
                # sentences = sentences.replace(repllast,'x')

#         # result = 0
# # for j in extest:
# #     if sentences in j:
# #         print("hi")

print(''.join(sentences))

