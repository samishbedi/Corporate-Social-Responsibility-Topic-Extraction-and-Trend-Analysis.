#LDA model for topic modeling

#import pyLDAvis.gensim
import gensim
from gensim import *
import collections
from collections import defaultdict
import pyLDAvis.gensim


corpus=corpora.MmCorpus('corpus_bus_new.mm')
dictionary=corpora.Dictionary.load('dictionary_bus_new.dict')

#for i in dictionary:
#  print dictionary[i]

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=15, id2word = dictionary, passes=30)
print ldamodel.show_topics()
ldamodel.save('lda_csr_bus_finalruns_15_2.model')

#ldamodel =  models.LdaModel.load('lda_csr_bus_8_lem.model')
vis=pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary)
pyLDAvis.save_html(vis,'LDA_vis_bus_finalsruns_15_2.html')
pyLDAvis.show(vis)

