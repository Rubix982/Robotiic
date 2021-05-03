# Package imports
import matplotlib.pyplot as plt
import networkx as nx

# Local imports

## Controllers
from controllers.MCVDriver import GenerateMCVGraph
from controllers.MRVDriver import GenerateMRVGraph

def GraphDriver():

    '''
    Generates a standard Pakistan represent of the graph, starting
    from here all the way to plt.savefig()
    '''
    G=nx.Graph()

    network_edges = [('Sindh', 'Baluchistan'), ('Sindh', 'Punjab'), ('Punjab', 'Baluchistan'), ('Punjab', 'NWFP'), ('Punjab', 'Kashmir'), ('Baluchistan', 'NWFP'), ('NWFP', 'Kashmir')]

    G.add_node('Sindh')
    G.add_node('Baluchistan')
    G.add_node('Punjab')
    G.add_node('NWFP')
    G.add_node('Kashmir')
    G.add_edges_from(network_edges)

    pos = nx.kamada_kawai_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                        node_size = 250)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=network_edges, edge_color='black', arrows=True)
    plt.savefig("./assets/img/Pakistan.png") # save as png

    colors = [ 'red', 'green', 'blue' ]

    GenerateMCVGraph(G, colors, network_edges)

    GenerateMRVGraph(G, colors, network_edges)

