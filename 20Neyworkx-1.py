import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,3)
print(G.nodes())
print(G.edges())

nx.draw(G)
plt.show()


G=nx.Graph()
l=[1,2,3]
G.add_nodes_from(l)
nx.draw(G)
plt.show()


G=nx.Graph()

G=nx.complete_graph(10)
nx.draw(G)
plt.show()


G=nx.gnp_random_graph(20,0.2)
nx.draw(G)
plt.show()
