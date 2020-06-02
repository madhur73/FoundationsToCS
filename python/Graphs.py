from collections import deque


class Node:
    def __init__(self, value):
        self.id = value
        self.neighbours = []
        self.is_visited = False


class Graph:
    def __init__(self):
        self.graph_nodes = dict()

    def set_graph_nodes(self, adj_list_input):
        # Assuming Adjaceny list dictionary
        for key in adj_list_input.keys():
            if key not in self.graph_nodes:
                node = Node(key)

                self.graph_nodes[key] = node
                node.neighbours = self.init_nodes(adj_list_input[key])

    def init_nodes(self, neighbours):
        neighbour_nodes = []
        for id_node in neighbours:
            if id_node not in self.graph_nodes:
                neighbour_nodes.append(Node(id_node))
            else:
                neighbour_nodes.append(self.graph_nodes[id_node])
        return neighbour_nodes

    def search(self, node_id):
        source_node = self.graph_nodes[node_id]
        self.traverse_dfs(source_node)

    def traverse_dfs(self, root):
        if root is None:
            return
        '''
         When Path is to found between nodes
         if root.id == destination:
            print("found the destination")
            return
        
        '''
        root.is_visited = True
        print(root.neighbours)
        print("Visiting Node with value:{}".format(root.id))
        for nodes in root.neighbours:
            if nodes:
                if not nodes.is_visited:
                    self.traverse_dfs(nodes)


visited_nodes = set()
graph_nodes = dict()


def simple_dfs(root, graph_list):
    if root is None:
        return

    visited_nodes.add(root)
    print("Visiting Node with value:{}".format(root))
    for neighbours in graph_list[root]:
        if neighbours not in visited_nodes:
            simple_dfs(neighbours, graph_list)


def simple_bfs(root, graph_list):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    visited_nodes.add(root)
    while queue:
        parent_node = queue.popleft()
        child_node_list = adj_list[parent_node]
        print("Parent with value:{}", parent_node)
        for child_node in child_node_list:
            if child_node not in visited_nodes:
                queue.append(child_node)
                visited_nodes.add(child_node)


graph_obj = Graph()

adj_list = {
    0: [1, 4, 5],
    5: [],
    1: [4, 3],
    4: [],
    2: [1],
    3: [2, 4],
}
# simple_dfs(0, adj_list)
simple_bfs(0, adj_list)
'''
graph_obj.set_graph_nodes(adj_list)
print(graph_obj.graph_nodes)
graph_obj.search(0)
'''
