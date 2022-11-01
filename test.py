import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

if __name__ == '__main__':

    # load the karate club graph
    G = nx.Graph()
    G.add_edge("a", "b", weight=0.6)
    G.add_edge("a", "c", weight=0.2)
    G.add_edge("c", "d", weight=0.1)
    G.add_edge("c", "e", weight=0.7)
    G.add_edge("c", "f", weight=0.9)
    G.add_edge("a", "d", weight=0.3)
    #G = nx.karate_club_graph()

    # first compute the best partition
    partition = community_louvain.best_partition(G)
    print(partition)
    # draw the graph
    pos = nx.spring_layout(G)
    # color the nodes according to their partition
    cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
    nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                           cmap=cmap, node_color=list(partition.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show()