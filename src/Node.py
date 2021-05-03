class Node:

    def __init__(self, name: str = '', neighbors: list = [], color: str = ''):
        self.name = name
        self.neighbors = neighbors
        self.edges = len(neighbors)
        self.color = color