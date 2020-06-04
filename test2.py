import itertools  
import statistics
import pandas as pd
import json
# Opening JSON file
f = open('1.json',"r")




####################################################################################################
data = json.loads(f.read())


df = pd.DataFrame(data["transcript"])
#transcript
#print(df)
data=df["utterance"]
utter=[]
for i in data:
    utter.append(i)
###############
bata=df["speaker"]
chata=df["startTime"]
speaker =[]
for i in bata:
    speaker.append(i)
startTime=[]
for i in chata:
    startTime.append(i)



f.close()
x=utter

import textblob
from textblob import TextBlob


p=0
q=0
r=0
s=0
data={}
data['utterence'] = []
data['overallSentiment']=[]
data['wordbag']=[]
pnumbers=[]
nnumbers=[]
onebhords=[]
twobhords=[]
threebhords=[]
##########sentiment per word
onebhordss=[]
twobhordss=[]
threebhordss=[]

for (a,b,c) in itertools.zip_longest(x,speaker,startTime):


    testimonial = TextBlob(x[p])
   # numbers.append(testimonial.sentiment.polarity)
    if testimonial.sentiment.polarity >0.1:
       pnumbers.append(testimonial.sentiment.polarity)
       
       zen = TextBlob(x[p])
       for word in zen.words:
           if TextBlob(word).sentiment.polarity>0:
             # print("positive :")
             # print(word)
              #onebhords.clear()
              onebhords.append(word)
              onebhordss.append(TextBlob(word).sentiment.polarity)

       m="Positive"
    elif testimonial.sentiment.polarity < 0.1 and testimonial.sentiment.polarity >-0.1:
         zen = TextBlob(x[p])
         for word in zen.words:
             if TextBlob(word).sentiment.polarity<0.1 and TextBlob(word).sentiment.polarity>-0.1:
              #  print("neutral :")
               #  print(word)
                #twobhords.clear()
                twobhords.append(word)
                twobhordss.append(TextBlob(word).sentiment.polarity)
         m="neutral"
    else:
        nnumbers.append(testimonial.sentiment.polarity)
        zen = TextBlob(x[p])
        for word in zen.words:
            if TextBlob(word).sentiment.polarity<-0.1:
               #print("negative :")
               #print(word)
               #threebhords.clear()
               threebhords.append(word)
               threebhordss.append(TextBlob(word).sentiment.polarity)
        m="Negative"
   # data["sentiment"]=m
    #print(onebhords)
    #print(twobhords)
    #print(threebhords)
    data['utterence'].append({"utterance":x[p],"speaker":speaker[q],"startTime":startTime[r],"sentiment":m,"sentimentScore":testimonial.sentiment.polarity })
    #data['utterence'].append({"sentiment":m})
    s= s + testimonial.sentiment.polarity
    #data['utterence'].append({"sentimentScore":testimonial.sentiment.polarity})
#    data["sentimentScore"]=testimonial.sentiment.polarity
    p=p+1
    q=q+1
    r=r+1







"""
print("+")
print(onebhords)
print(onebhordss)
print("neutral")
print(twobhords)
print(twobhordss)
print("-")
print(len(onebhords));
print(len(onebhordss));
print(onebhords);
print(onebhordss);
"""

#print("______")
if s>0:
   o="positve"
elif s==0:
   o="neutral"
else:
   o="negative"
data['overallSentiment'].append({"positivity":statistics.mean(pnumbers),"negativity":statistics.mean(nnumbers), "overallSentiment":o,"sentimentScore":(s/len(x))})
#data['overallSentiment1'].append({"positivity":statistics.mean(pnumbers),"negativity":statistics.mean(nnumbers), "overallSentiment":o,"sentimentScore":(s/len(x))})
bakri1 = 0;
for  aa in onebhords:
     data['wordbag'].append({"positiveword":onebhords[bakri1],"wordscore":onebhordss[bakri1]})
     bakri1=bakri1+1;


bakri2 = 0;
for  bb in threebhords:
     data['wordbag'].append({"negativeword":threebhords[bakri2],"wordscore":threebhordss[bakri2]})
     bakri2=bakri2+1;
#data['wordbag'].append({"positivewords":onebhords,"neutralwords":twobhords,"negativewords":threebhords })
#print(s/len(x))
#data['overallSentiment'].append({"sentimentScore":s/len(x)})
##############



########################################################################output file name ###################
with open('bakri.json', 'w') as outfile:
    json.dump(data, outfile,indent=4)
print("___done___")

