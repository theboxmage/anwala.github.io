import networkx
from matplotlib import pylab

G = networkx.karate_club_graph()
pos = networkx.spring_layout(G)
c = networkx.connected_component_subgraphs(G)
iterCount=0
print("Iteration: ", iterCount)
output = "graph" + format(iterCount, '02d') + ".png"
pylab.figure()
networkx.draw_networkx(G, pos)
pylab.savefig(output)
pylab.close()
while (len(list(c)) == 1):
    #G.remove_edge(*edge_to_remove(G))
    hold = networkx.edge_betweenness_centrality(G)
    curr = hold.items()
    currSorted = sorted(curr,key=lambda x:x[1], reverse = True)
    G.remove_edge(*currSorted[0][0])
    c = networkx.connected_component_subgraphs(G)
    pos = networkx.spring_layout(G)
    iterCount += 1
    output = "graph" + format(iterCount, '02d') + ".png"
    print("Iteration: ", iterCount)
    pylab.figure()
    networkx.draw_networkx(G, pos)
    pylab.savefig(output)
    pylab.close()
pylab.figure()
c = networkx.connected_component_subgraphs(G)
pos = networkx.spring_layout(G)
networkx.draw_networkx(G, pos)
networkx.draw_networkx_nodes(G, pos, nodelist=[0, 1, 3, 4, 5, 6, 7, 10, 11, 12, 13, 16, 17, 19, 21], node_color='b')
pylab.savefig("final.png")
pylab.close()


