# Package imports
import matplotlib.pyplot as plt
import networkx as nx

# Local imports
from src.MRV import MRV

def GenerateMRVGraph(Graph: nx.classes.graph.Graph, colors: list, network_edges: list):

    mrv = MRV(Graph, colors)
    mrv = mrv.StartIteration()

    color_map = []

    for node in mrv['nodes']:
        color_map.append(node['color'])

    pos = nx.kamada_kawai_layout(Graph)
    nx.draw_networkx_nodes(Graph, pos, cmap=plt.get_cmap('jet'), 
                        node_size = 250, node_color=color_map)
    nx.draw_networkx_labels(Graph, pos)
    nx.draw_networkx_edges(Graph, pos, edgelist=network_edges, edge_color='black', arrows=True)
    plt.savefig("./assets/img/MRV.png") # save as png    

    return mrv['path']