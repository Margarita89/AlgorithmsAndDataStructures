# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

from collections import deque

class Node():
    def __init__(self, node):
        self.node = node
        self.adjacent = []
        self.visited = False

    def addAdjacent(self, x):
        self.adjacent.append(x)

    #def getAdjacent(self):
    #    return self.adjacent

    #def getNode(self):
    #    return self.node

class directedGraph():
    def __init__(self):
        self.nodes = []

    def addNode(self, x):
        self.nodes.append(x)


# find out whether there is a route between two nodes (bfs)
def breadthFirstSearch(graph, node1, node2):
    if node1 == node2:
        return True

    queue = deque()
    queue.append(node1)
    node1.visited = True

    while queue:
        node_from_queue = queue.popleft()
        for i in range(len(node_from_queue.adjacent)):
            print('node_from_queue.adjacent[i] : ', node_from_queue.adjacent[i].node)
            if not node_from_queue.adjacent[i].visited:
                if node_from_queue.adjacent[i] == node2:
                    print('Path was found')
                    return
                queue.append(node_from_queue.adjacent[i])
                node_from_queue.adjacent[i].visited = True
    print('Path was not found')
    return


# without cycles
def createAcycleGraph():
    graph_a = directedGraph()
    arr_nodes = []
    num_nodes_graph = 6

    for i in range(num_nodes_graph):
        arr_nodes.append(Node(i))

    arr_nodes[0].addAdjacent(arr_nodes[1])
    arr_nodes[0].addAdjacent(arr_nodes[2])
    arr_nodes[0].addAdjacent(arr_nodes[3])
    arr_nodes[2].addAdjacent(arr_nodes[4])
    arr_nodes[4].addAdjacent(arr_nodes[5])

    for i in range(num_nodes_graph):
        graph_a.addNode(arr_nodes[i])

    return graph_a


def createCycleGraph():
    graph_c = directedGraph()
    arr_nodes =  []
    num_nodes_graph = 6

    for i in range(num_nodes_graph):
        arr_nodes.append(Node(i))

    arr_nodes[0].addAdjacent(arr_nodes[1])
    arr_nodes[0].addAdjacent(arr_nodes[2])
    arr_nodes[0].addAdjacent(arr_nodes[3])
    arr_nodes[2].addAdjacent(arr_nodes[4])
    arr_nodes[4].addAdjacent(arr_nodes[5])
    arr_nodes[1].addAdjacent(arr_nodes[3])
    arr_nodes[4].addAdjacent(arr_nodes[0])

    for i in range(num_nodes_graph):
        graph_c.addNode(arr_nodes[i])

    return graph_c

if __name__ == "__main__":
    graph = createAcycleGraph()
    nodes = graph.nodes
    node1 = nodes[0]
    node2 = nodes[-1]
    breadthFirstSearch(graph, node1, node2)

    graph2 = createCycleGraph()
    nodes = graph2.nodes
    node1 = nodes[0]
    node2 = nodes[-1]
    breadthFirstSearch(graph2, node1, node2)


    #node1 = Node("a")
    #node2 = Node("b")
    #node3 = Node("c")
    #node4 = Node("d")
    #node5 = Node("e")
    #node6 = Node("f")

    #node1.addAdjacent(node2)
    #node1.addAdjacent(node3)
    #node1.addAdjacent(node4)
    #node2.addAdjacent(node5)
    #node5.addAdjacent(node6)


    #graph_a.addNode(node1)
    #graph_a.addNode(node2)
    #graph_a.addNode(node3)
    #graph_a.addNode(node4)
    #graph_a.addNode(node5)
    #graph_a.addNode(node6)
