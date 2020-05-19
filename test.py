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






#print(utter,speaker,startTime)




f.close()
x=utter

############this is the first utter #########
#print(x[1])
###########








#print(" ############################ pos /neg / neutral ######################")
from textblob import TextBlob
#print(" +/-/neutral   program startin .....")

"""
y=0
for i in x:
    print(x[y])
    testimonial = TextBlob(x[y])
    if testimonial.sentiment.polarity >0.1:
       print("Positive utterence")
    elif testimonial.sentiment.polarity < 0.1 and testimonial.sentiment.polarity >-0.1:
         print("neutral sentiment")
    else:
        print("Negative sentiment")

    print(testimonial.sentiment.polarity)
   # print("-------------------------------------------------------------------------------------------------------------------------")  
    y=y+1

"""
"""
for (a,b,c) in itertools.zip_longest(x,speaker,startTime):
    print (a, b, c)
"""
p=0
q=0
r=0
s=0
data={}
data['utterence'] = []
data['overallSentiment']=[]
pnumbers=[]
nnumbers=[]
for (a,b,c) in itertools.zip_longest(x,speaker,startTime):

    """    data['utterence'].append({
    "utterance":x[p],
    "speaker":speaker[q],
    "startTime":startTime[r]  })
    """

#    print (x[p])

 #   print (speaker[q])
 #   q=q+1
  #  print (startTime[r])
  #  r=r+1
    testimonial = TextBlob(x[p])
   # numbers.append(testimonial.sentiment.polarity)
    if testimonial.sentiment.polarity >0.1:
       pnumbers.append(testimonial.sentiment.polarity)      
       m="Positive"
    elif testimonial.sentiment.polarity < 0.1 and testimonial.sentiment.polarity >-0.1:
         m="neutral"
    else:
        nnumbers.append(testimonial.sentiment.polarity)
        m="Negative"
   # data["sentiment"]=m
    data['utterence'].append({"utterance":x[p],"speaker":speaker[q],"startTime":startTime[r],"sentiment":m,"sentimentScore":testimonial.sentiment.polarity})
    #data['utterence'].append({"sentiment":m})
    s= s + testimonial.sentiment.polarity
    #data['utterence'].append({"sentimentScore":testimonial.sentiment.polarity})
#    data["sentimentScore"]=testimonial.sentiment.polarity
    p=p+1
    q=q+1
    r=r+1

"""
print(pnumbers)
print(statistics.mean(pnumbers))
print(nnumbers)
print(statistics.mean(nnumbers))
"""
#print("______")
if s>0:
   o="positve"
elif s==0:
   o="neutral"
else:
   o="negative"
data['overallSentiment'].append({"positivity":statistics.mean(pnumbers),"negativity":statistics.mean(nnumbers), "overallSentiment":o,"sentimentScore":(s/len(x))})
#print(s/len(x))
#data['overallSentiment'].append({"sentimentScore":s/len(x)})
##############

























########################################################################output file name ###################
with open('ut.json', 'w') as outfile:
    json.dump(data, outfile,indent=4)
print("___done___")
