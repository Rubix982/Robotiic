# Package imports
import matplotlib.pyplot as plt
import networkx as nx

# Local imports
from src.MCV import MCV

def GenerateMCVGraph(Graph: nx.classes.graph.Graph, colors: list, network_edges: list):

    mcv = MCV(Graph, colors)
    mcv = mcv.StartIteration()

    color_map = []

    for node in mcv['nodes']:
        color_map.append(node['color'])

    pos = nx.kamada_kawai_layout(Graph)
    nx.draw_networkx_nodes(Graph, pos, cmap=plt.get_cmap('jet'), 
                        node_size = 250, node_color=color_map)
    nx.draw_networkx_labels(Graph, pos)
    nx.draw_networkx_edges(Graph, pos, edgelist=network_edges, edge_color='black', arrows=True)
    plt.savefig("./assets/img/MCV.png") # save as png    

