#Create csv file with topic information
import gensim
from gensim import *
import collections
from collections import defaultdict
import pyLDAvis.gensim
import csv
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

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

i=0
for t in ldamodel.show_topics(num_topics=15):
  print "Topic #"+str(i),"\n", t, "\n"
  i+=1
"""
print sorted(ldamodel[corpus[5009]],key=itemgetter(1),reverse=True),columns['Year'][5009],columns['Title'][5009]
"""

with open("BUS_new_top.csv",'w') as f:
  fieldnames = []
  for i in range(0,15):
    fieldnames.append("Topic "+str(i))
  writer = csv.DictWriter(f,fieldnames=fieldnames)
  writer.writeheader()
  for i in range(len(corpus)):
    dict1={}
    
    for term in sorted(ldamodel[corpus[i]],key=itemgetter(0)):
      dict1["Topic "+ str(term[0])]=term[1]
    for i in range(0,15):
      if ("Topic " + str(i)) not in dict1:
        dict1["Topic "+str(i)]=0
    writer.writerow(dict1)
  
for i in range(len(corpus)):
  print i,(sorted(ldamodel[corpus[i]],key=itemgetter(1)))


  #print i,(sorted(ldamodel[corpus[i]],key=itemgetter(1),reverse=True))[0],columns['Year'][i]


