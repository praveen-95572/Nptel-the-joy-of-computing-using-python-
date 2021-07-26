import networkx as nx
import matplotlib.pyplot as plt

'''G=nx.barbell_graph(4,3)
G=nx.complete_graph(5)
G=nx.cycle_graph(5)
G=nx.ladder_graph(5)
G=nx.path_graph(5)
G=nx.star_graph(1)
G=nx.wheel_graph(4)'''
G=nx.gnp_random_graph(5,0.5)
nx.draw(G)
plt.show()
