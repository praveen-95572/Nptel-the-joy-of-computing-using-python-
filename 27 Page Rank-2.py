import networkx as nx
import matplotlib.pyplot as plt
import random
import operator

G=nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(G,with_labels=True)
plt.show()

x=random.choice([i for i in range(G.number_of_nodes())])      #pick node randomly
dict_counter={}
for i in range(G.number_of_nodes()):
     dict_counter[i]=0

dict_counter[x]+=1
for i in range(1000000):
     list_n=list(G.neighbors(x))
     if(len(list_n)==0):
          x=random.choice([i for i in range(G.number_of_nodes())])
     else:
          x=random.choice(list_n)
     dict_counter[x]+=1

p=nx.pagerank(G)
sorted_p=sorted(p.items(),key=operator.itemgetter(1))       #by operator lib.(sorted based on values..... to sorted by key put 0)
sorted_rw=sorted(dict_counter.items(),key=operator.itemgetter(1))
print(p)
print(dict_counter)
