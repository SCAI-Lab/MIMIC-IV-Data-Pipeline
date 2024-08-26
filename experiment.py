


import pickle


condVocabDict={}
procVocabDict={}
medVocabDict={}
outVocabDict={}
chartVocabDict={}
labVocabDict={}
ethVocabDict={}
ageVocabDict={}
genderVocabDict={}
insVocabDict={}


with open('./data/dict/'+'ethVocabDict', 'rb') as fp:
    ethVocabDict= pickle.load(fp)



with open('./data/dict/'+'ageVocabDict', 'rb') as fp:
    ageVocabDict= pickle.load(fp)



with open('./data/dict/'+'genderVocabDict', 'rb') as fp:
    genderVocabDict= pickle.load(fp)


    
with open('./data/dict/'+'insVocabDict', 'rb') as fp:
    insVocabDict= pickle.load(fp)

for key, value in insVocabDict.items():
    print(key, " : ", value)


file='condVocab'
with open ('./data/dict/'+file, 'rb') as fp:
    condVocabDict = pickle.load(fp)


print(len(condVocabDict))
print(condVocabDict)


file='procVocab'
with open ('./data/dict/'+file, 'rb') as fp:
    procVocabDict = pickle.load(fp)

print(len(procVocabDict))
print(procVocabDict)

file='medVocab'
with open ('./data/dict/'+file, 'rb') as fp:
    medVocabDict = pickle.load(fp)

print(len(medVocabDict))
print(medVocabDict)

file='outVocab'
with open ('./data/dict/'+file, 'rb') as fp:
    outVocabDict = pickle.load(fp)

print(len(outVocabDict))
print(outVocabDict)

file='chartVocab'
with open ('./data/dict/'+file, 'rb') as fp:
    chartVocabDict = pickle.load(fp)

print(len(chartVocabDict))
print(chartVocabDict)

file='labsVocab'
with open ('./data/dict/'+file, 'rb') as fp:
    labVocabDict = pickle.load(fp)

print(len(labVocabDict))
print(labVocabDict)




