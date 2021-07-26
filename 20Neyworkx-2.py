import matplotlib.pyplot as plt
import networkx as nx

G=nx.gnp_random_graph(50,0.3)

print("Degree of 0th node = ",G.degree(0))
nx.draw(G)
plt.show()


G=nx.barabasi_albert_graph(50,2)
nx.draw(G)
plt.show()

nx.write_gexf(G,"networkx_analysis.gexf")
print("Stored graph in gexf/xml format")
