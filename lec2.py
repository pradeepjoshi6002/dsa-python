# document distance d(D1,D2)

#document=sequence of words
#word=string sequnce of alphanumeric chars.

#finding @=arccos((D1.D2)/(|D1|.|D2|))
import math

doc1="apples are red"
doc2="apples are green too"

def getVector(sentence):
    arr=sentence.split(" ")
    hash={}
    for word in arr:
        if word in hash:
            hash[word]+=1
        else:
            hash[word]=1
    return hash

def getVectorMagnitude(vector):
    res=0
    for values in vector.values():
        res+=values*values
    res=math.sqrt(res)
    return res
    
vector1=getVector(doc1)
vector2=getVector(doc2)

sum=0

for word in vector1.keys():
    if word in vector2:
        sum+=vector2[word]*vector1[word]

magnitude1=getVectorMagnitude(vector1)
magnitude2=getVectorMagnitude(vector2)

cosine=sum/(magnitude1*magnitude2)
distance = math.acos(cosine)

print(distance)