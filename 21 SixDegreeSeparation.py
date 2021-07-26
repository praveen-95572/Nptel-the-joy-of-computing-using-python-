import networkx as nx
import numpy   #for mathematical fun.


G = nx.read_edgelist("facebook_combined.txt")
N=list(G.nodes())

spll=[]  #shortest path list

for u in N:
     for v in N:
          if u != v:
               l=nx.shotest_path_length(G,u,v)
               print("Shortest path between ",u," and ",v," is : ",l)
               spll.append(l)

min_spl=min(spll)
max_spl=max(spll)
avg_spl=numpy.average(spll)

print("Minimum shortest path length : ",min_spl)

print("Maximum shortest path length : ",max_spl)

print("Average shortest path length : ",avg_spl)
