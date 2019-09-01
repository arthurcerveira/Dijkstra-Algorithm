class Node(object):
    def __init__(self):
        self.linked_nodes = []
        self.distance = float("inf")
        self.prev = -1

        self.closed = False


class Graph(object):
    def __init__(self):
        self.nodes = []

        self.first_node = Node()
        self.first_node.distance = 0
        self.first_node.closed = True

        self.nodes.append(self.first_node)

    # def dijkstra_algorithm():
