import gensim
from gensim import *
import collections
from collections import defaultdict
import pyLDAvis.gensim
import csv
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

columns = defaultdict(list)

with open("BUS_new _withtops.csv",'r') as f:
  reader=csv.DictReader(f)
  for row in reader:    
    for(k,v) in row.items():
      columns[k].append(v)
corpus=corpora.MmCorpus('corpus_bus_new.mm')
dictionary=corpora.Dictionary.load('dictionary_bus_new.dict')
#print len(corpus)

ldamodel =  models.LdaModel.load('lda_csr_bus_15.model')
#print ldamodel.show_topics(num_topics=15)

i=0
for t in ldamodel.show_topics(num_topics=15):
  print "Topic #"+str(i),"\n", t, "\n"
  i+=1

dic_lis=[]

for i in range(0,15):
  dic_lis.append({})

for j in range(0,15):
  for i in sorted(set(columns['Year'])):
    dic_lis[j][i]=0
 

#dict_0['2016']+=1

#Set cutoff by changing 0.1
for i in range(len(columns['Year'])):
    #print columns['Year'][i],columns['Topic 0'][i]
  for k in range(0,15):
    if float(columns['Topic '+str(k)][i]) > 0.1:
      dic_lis[k][columns['Year'][i]]+=1

print dic_lis[0]
 

for i in range(0,15):
  dic_lis[i]=OrderedDict(sorted((dic_lis[i]).items(), key=lambda t: t[0]))
  dic_lis[i].pop('')
#print dic_lis[0]
#print dict_0.values()

#y_1=np.array(float(dict_0.values()))
#x_1=np.array(int(dict_0.keys())

y=[]
x=[]
for i in range(0,15):
  y1=[]
  for j in dic_lis[i].values():
    y1.append(int(j))
  y1 = np.array(y1)
  y.append(y1)

for i in dic_lis[0].keys():
  x.append(int(i))

f=open('topics.csv','w')
f.write("Year,")
for i in range(0,15):
  f.write(str("Topic "+str(i)))
  f.write(",")
f.write("\n")
for i in dic_lis[0].keys():
  f.write(i)
  f.write(",")
  for k in range(0,15):
    f.write(str(dic_lis[k][i]))
    f.write(",")
  f.write("\n")
  
#print y_0

y = np.array(y)
x = np.array(x)
#print y,x
#y1, y2, y3 = fnx(), fnx(), fnx()


fig, ax = plt.subplots()
#ax.set_xlim(1962,2016)
minor_ticks = np.arange(1962,2017, 1)                                               
ax.set_xticks(minor_ticks)                                           
ax.stackplot(x, y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8],y[9],y[10],y[11],y[12],y[13],y[14])
plt.show()


#fig, ax = plt.subplots()
#ax.stackplot(x, y1, y2, y3)
#plt.show()

