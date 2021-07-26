import networkx as nx
import random
import matplotlib.pyplot as plt
def add_edges():
     nodes =list(G.nodes())

     for s in nodes:
          for t in nodes:
               if s!=t:
                    r=random.random()
                    if r<=0.5:
                         G.add_edge(s,t)

     return G

def assign_points(G):
     nodes=list(G.nodes())
     p=[]
     for each in nodes:
          p.append(100)
     return p

def distribute_points(G,points):
     nodes=list(G.nodes())
     new_points=[]
     for i in range(len(nodes)):
          new_points.append(0)
     for n in nodes:
          out=list(G.out_edges(n))
          if len(out)==0:
               new_points[n]+=points[n]
          else:
               share=points[n]/len(out)
               for(src,tgt) in out:
                    new_points[tgt]+=share
     return new_points
          

def Keep_distributing(points,G):
     while(1):
          new_points=distribute_points(G,points)
          print(new_points)
          points=new_points
          stop=input("Press # to stop or any other key to continue : ")
          if stop=='#':
               break
     return new_points

def rank_by_points(final_points):
     dict={}
     for i in range(len(final_points)):
          dict[i]=final_points[i]
     print(sorted(dict.items(),key=lambda f:f[1]))
     
G=nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G=add_edges()

nx.draw(G,with_labels=True)
plt.show()

#assign initial point
ppoints=assign_points(G)   

#Keep distributing the points
final_points=Keep_distributing(ppoints,G)

#Rank by points
rank_by_points(final_points)

#default networkx fun.
result=nx.pagerank(G)
print(sorted(result.items(),key=lambda f:f[1]))
