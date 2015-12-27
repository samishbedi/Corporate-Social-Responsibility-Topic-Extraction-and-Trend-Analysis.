#for visualization in pyLDAvis and time plot

import gensim
from gensim import *
import collections
from collections import defaultdict
import pyLDAvis.gensim
import csv
import matplotlib.pyplot as plt
import numpy as np

columns = defaultdict(list)

with open("BUS_new.csv",'r') as f:
  reader=csv.DictReader(f)
  for row in reader:    
    for(k,v) in row.items():
      columns[k].append(v)
corpus=corpora.MmCorpus('corpus_bus_new.mm')
dictionary=corpora.Dictionary.load('dictionary_bus_new.dict')
print len(corpus)

ldamodel =  models.LdaModel.load('lda_csr_bus_15.model')
print ldamodel.show_topics(num_topics=15)

#print ldamodel[]


corp_70=[]
corp_80=[]
corp_90=[]
corp_00=[]
corp_10=[]

i=0
for a in columns['Year']:
  i+=1
  try:
    if int(a)<1980:
      corp_70+=corpus[i-1]
    if int(a)>=1980 and int(a)<1990:
      corp_80+=corpus[i-1]
    if int(a)>=1990 and int(a)<2000:      
      corp_90+=corpus[i-1]
    if int(a)>=2000 and int(a)<2010:
      corp_00+=corpus[i-1]
    if int(a)>=2010 and int(a)<2020:
      #print i-1,a
      corp_10+=corpus[i-1]
      #print a
      #print i-1
  except:
    continue
  #if a>=1970 and a<1980:
   # print a
    #print i,corpus[i]
    #corp_70+=corpus[i]
  #i+=1


#print ldamodel.show_topics()
doc_topic=[ldamodel[corp_70],ldamodel[corp_80],ldamodel[corp_90],ldamodel[corp_00],ldamodel[corp_10]]

i=0
for t in ldamodel.show_topics(num_topics=15):
  print "Topic #"+str(i),"\n", t, "\n"
  i+=1
  """
  if i==0:
    print "Topic #"+str(7),"\n", t, "\n"
  if i==1:
    print "Topic #"+str(3),"\n", t, "\n"
  if i==2:
    print "Topic #"+str(2),"\n", t, "\n"
  if i==3:
    print "Topic #"+str(6),"\n", t, "\n"
  if i==4:
    print "Topic #"+str(8),"\n", t, "\n"
  if i==5:
    print "Topic #"+str(5),"\n", t, "\n"
  if i==6:
    print "Topic #"+str(4),"\n", t, "\n"
  if i==7:
    print "Topic #"+str(1),"\n", t, "\n"
  i+=1

  if i==0:
    print "Topic #"+str(3),"\n", t, "\n"
  if i==1:
    print "Topic #"+str(2),"\n", t, "\n"
  if i==2:
    print "Topic #"+str(1),"\n", t, "\n"
  if i==3:
    print "Topic #"+str(4),"\n", t, "\n"
  if i==4:
    print "Topic #"+str(9),"\n", t, "\n"
  if i==5:
    print "Topic #"+str(5),"\n", t, "\n"
  if i==6:
    print "Topic #"+str(10),"\n", t, "\n"
  if i==7:
    print "Topic #"+str(7),"\n", t, "\n"
  if i==8:
    print "Topic #"+str(8),"\n", t, "\n"
  if i==9:
    print "Topic #"+str(6),"\n", t, "\n"
"""
  

#print ldamodel[corp_80]
#print ldamodel[corp_90]
#print ldamodel[corp_00]
#print ldamodel[corp_10]

doctopic=[]

for a in doc_topic:
  li=[]
  for b in a:
    li.append(b[1])
  doctopic.append(li)

#doctopic1=[doctopic[2],doctopic[1],doctopic[0],doctopic[3],doctopic[5],doctopic[9],doctopic[7],doctopic[8],doctopic[4],topic[6]]
#doctopic=doctopic1

doctopic=np.array(doctopic)
#print doctopic[1][4]
#print doctopic
    


N=5 #No. of time stamps
K=8 #No. of topics

ind = np.arange(N)
width =0.5
plots=[]
height_cumulative = np.zeros(N)
#print height_cumulative
"""
for k in range(K):
  color = plt.cm.coolwarm((k*1.0)/K, 1)
  #print color
  if k == 0:
    p = plt.bar(ind, doctopic[:, k], width, color=color)
  else:
    p = plt.bar(ind, doctopic[:, k], width, bottom=height_cumulative, color=color)
  height_cumulative += doctopic[:, k]
 #print doctopic[:, k]
 #print height_cumulative
  plots.append(p) 
"""
x1=[]
for d in  doctopic:
  x1.append(d[0])

arr=np.array(x1)
  
docnames=['1970s','1980s','1990s','2000s','2010s']
#plt.ylim((0, 1))
plt.ylabel('Topics')
plt.title('Topics in CSR')
plt.xticks(ind+width/2, docnames)
plt.bar(ind, x1, width=width)
#plt.yticks(np.arange(0, 1, 10))
#topic_labels = ['Topic #{}'.format(k) for k in range(K)]
#topic_labels=[1,2,3,4,5,6,7,8]
#topic_labels = ['Topic #3','Topic #2','Topic #1','Topic #4','Topic #9','Topic #5','Topic #10','Topic #7','Topic #8','Topic #6']
#topic_labels = ['Topic #7','Topic #3','Topic #2','Topic #6','Topic #8','Topic #5','Topic #4','Topic #1']


#plt.legend([p[0] for p in plots], topic_labels,loc=1,bbox_to_anchor=(1.07, 1),borderaxespad=0.)


#vis=pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary)
#pyLDAvis.save_html(vis,'LDA_vis_bus_10.html')
plt.show()
#pyLDAvis.show(vis)


