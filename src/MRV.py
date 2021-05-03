# Package imports
import networkx as nx
import random

# Local imports
from src.Node import Node

class MRV:
    '''
    Minimum Remaining Values heuristic
    '''

    def __init__(self, Graph: nx.classes.graph.Graph, colors: list = []):
        self.Graph = Graph
        self.Nodes = []
        self.colors = colors
        self.totalColors = len(colors)

    def Preprocess(self):
        nodes = self.Graph.nodes

        for node in nodes:
            edges = self.Graph.edges(node)
            neighbors = []
            for edge in edges:
                neighbors.append(edge[1])
            
            self.Nodes.append(Node(name=node, neighbors=neighbors))

    def StartIteration(self):

        self.Preprocess()

        node_path = []

        while True:

            '''
            This loop wil be terminated by two conditions
            in the below algorithm
            '''

            minn = len(self.Nodes) + 1
            min_node_index = -1

            # The first part of the algorithm is the selection
            # phase where we select the node
            for i in range(0, len(self.Nodes)):

                # Checking for a potential node
                if minn > self.Nodes[i].edges and self.Nodes[i].color == '':

                    # If a potential node is found, then
                    # select it
                    minn = self.Nodes[i].edges
                    min_node_index = i

            # We check if a potential node was found
            if min_node_index == -1:
                
                # No potential node can be found anymore
                break 

            node_path.append(self.Nodes[min_node_index].name)

            '''
            If we come here, that means there indeed
            is a potential node present. We need to
            step through the process with the following
            algorithm,

            1. Maintain some variables,
                1.1. A local copy list of the colors that can be assigned
                1.2. A local copy of the selected node's neighbors
            2.1. Traverse the neighboring adjacent nodes
            2.2 if they contain a color, remove that color from our list of possible colors
            3. Out of the colors that remain, randomly select one
            and assign it to the current selected node
            4. Update the edge count in the neighboring adjacent nodes
            '''

            # Step 1.1, A local copy list of the colors that can be assigned
            __local_color_store = self.colors.copy()

            # Step 1.2, A local copy of the selected node's neighbors
            __local_neighbor_store = self.Nodes[min_node_index].neighbors

            # Step 2.1, traversing the neigboring adjacent nodes
            for i in range(0, len(self.Nodes)):

                if i != min_node_index and self.Nodes[i].name in __local_neighbor_store and self.Nodes[i].color in __local_color_store:

                    # 2.2 if they contain a color, remove that color from our list of possible colors
                    __local_color_store.remove(self.Nodes[i].color)

            # If the __local_color_store has at least 1
            # color remaining
            if len(__local_color_store) == 0:
                break
            
            # 3. Out of the colors that remain, randomly select one
            # and assign it to the current selected node
            self.Nodes[min_node_index].color = random.choice(__local_color_store)

            # 4. Update the edge count in the neighboring adjacent nodes
            for i in range(0, len(self.Nodes)):

                if i != min_node_index and self.Nodes[i].name in __local_neighbor_store:
                    self.Nodes[i].edges -= 1

        final_node_list = []

        for i in range(0, len(self.Nodes)):

            # Appending to list the dict version 
            # of the nodes
            final_node_list.append(self.Nodes[i].__dict__)

        # Checking if all the nodes were 
        # colored successfully
        for i in range(0, len(self.Nodes)):
            
            # A node couldn't be colored for some reason
            if self.Nodes[i].color == '':
                return { 'succesful': False, 'nodes': final_node_list, 'path': node_path }

        return { 'successful': True, 'nodes': final_node_list, 'path': node_path }
