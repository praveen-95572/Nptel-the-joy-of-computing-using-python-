import networkx as nx
import matplotlib.pyplot as plt
U=nx.Graph()        #undirected graph

G=nx.DiGraph()      #Directed graph

print(G.nodes())

G.add_nodes_from([i for i in range(10)])
print(G.edges())              #by default show outgoing edges


G.add_edge(1,2)
G.add_edge(0,2)
G.add_edge(1,3)
G.add_edge(3,1)
G.add_edge(3,5)

print(G.out_edges())
print(G.in_edges())

nx.draw(G,with_labels=True)
plt.show()
