class Node(object):
    def __init__(self, index):
        self.index = index

        self.linked_nodes_index = []
        self.distance = float("inf")
        self.prev = -1

        self.open = True

    def relax_adj(self, nodes):
        for node_index, edge_value in self.linked_nodes_index:
            distance = self.distance + edge_value

            if distance < nodes[node_index].distance:
                nodes[node_index].distance = distance
                nodes[node_index].prev = self.index


class Graph(object):
    def __init__(self):
        self.nodes = []

        self.first_node = Node(0)
        self.first_node.distance = 0

        self.nodes.append(self.first_node)

    def dijkstra(self):
        while self.open_nodes() is not None:
            min_node = self.find_min_node()
            min_node.open = False

            min_node.relax_adj(self.nodes)

    def open_nodes(self):
        for node in self.nodes:
            if node.open is True:
                return node

        return None

    def find_min_node(self):
        min_distance = float("inf")
        min_node = None

        for node in self.nodes:
            if node.open and node.distance < min_distance:
                min_node = node
                min_distance = node.distance

        return min_node
