#Plot network graph of authors who have done work together

import networkx as nx
import csv
from collections import defaultdict
import matplotlib.pyplot as plt
from collections import defaultdict



columns = defaultdict(list)
g=nx.Graph()
pos=nx.spring_layout(g)


with open("scopus.csv",'r') as f:
  reader=csv.DictReader(f)
  for row in reader:    
    for(k,v) in row.items():
      columns[k].append(v)

list_a=[]
list_b=[]
d=dict()
i=0
for a in columns['Authors']:
  a=a.replace(", ",",")
  list_a1=a.split(",")
  for a1 in list_a1:
    try:
      g.add_node(a1)
      i+=1
    except:
      pass
  list_a.append(list_a1)

edgeList = list_a

#for a in sorted(list_b):
 # print a
  

for i in range(0,len(edgeList)):
  try:  
    if len(edgeList[i])>1:
      #print len(edgeList[i])
      g.add_edges_from([edgeList[i]])
  except:
    pass


outdeg = g.degree()
to_remove = [n for n in outdeg if outdeg[n] < 2]
g.remove_nodes_from(to_remove)
g.remove_nodes_from(nx.isolates(g))  

#g.remove_small_components(min_size=4)  
#g.summary()
pos = nx.spring_layout(g)


nx.draw(g,pos,node_size=50,with_label=True)
#nx.draw_networkx_labels(g,d,font_size=16)
#pos = nx.spring_layout(g,scale=1) #default to scale=1
#nx.draw(g,pos, with_labels=True)
plt.show()


