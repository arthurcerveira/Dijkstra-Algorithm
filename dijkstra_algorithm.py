class Node(object):
    def __init__(self, index, linked_nodes_index):
        self.index = index

        self.linked_nodes_index = linked_nodes_index
        self.distance = float("inf")
        self.prev = -1

        self.open = True

    def relax_adj(self, nodes):
        for node_index, edge_value in self.linked_nodes_index:
            distance = self.distance + edge_value

            if distance < nodes[node_index].distance:
                nodes[node_index].distance = distance
                nodes[node_index].prev = self.index

    def close(self):
        self.open = False


class Graph(object):
    def __init__(self):
        self.nodes = []

    def add_node(self, index, linked_nodes_index):
        node = Node(index, linked_nodes_index)

        if index == 0:
            node.distance = 0

        self.nodes.append(node)

    def add_nodes_from_file(self, nodes):
        index = 0

        for line in nodes:
            data = line.split()

            linked_nodes_index = []
            i = 0

            while i < data.__len__() and data[i] != '-1':
                node = int(data[i])
                edge = int(data[i + 1])

                linked_nodes_index.append([node, edge])
                i += 2

            self.add_node(index, linked_nodes_index)
            index += 1

    def dijkstra(self):
        while self.open_nodes() is not None:
            min_node = self.find_min_node()
            min_node.close()

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

    def show_path(self, node_index):
        path = []
        node = self.nodes[node_index]

        while node.index != 0:
            path.append(node.index)
            node = self.nodes[node.prev]

        path.append(0)
        path.reverse()

        return path


def main():
    graph = Graph()

    with open("nodes.txt") as nodes:
        graph.add_nodes_from_file(nodes)

    graph.dijkstra()

    for n in graph.nodes:
        print("Best path to node " + n.index.__str__() + ": \n" + graph.show_path(n.index).__str__())


if __name__ == "__main__":
    main()
