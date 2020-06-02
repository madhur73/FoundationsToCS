IMBALANCE_THRESHOLD = 2


class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert_from_array(self, array_input):
        for val in array_input:
            if not self.root:
                self.root = Node(val)
            else:
                self._insert_node(self.root, val)

    def _insert_node(self, root, value_to_ins):

        if value_to_ins > root.value:
            if root.right is None:
                root.right = Node(value_to_ins)
            else:
                self._insert_node(root.right, value_to_ins)
        else:
            if root.left is None:
                root.left = Node(value_to_ins)
            else:
                self._insert_node(root.left, value_to_ins)

    def is_node_imbalanced(self,node):
        if node is None:
            return
        self.is_node_imbalanced(node.left)
        height = self.calculate_height_of_node(node)
        if height >= IMBALANCE_THRESHOLD:
            print("Node with value:{0} is imbalance{0}".format(node.value, height))
        self.is_node_imbalanced(node.right)

    def calculate_height_of_node(self, root):
        if root is None:
            return 0
        return abs(self.calculate_height_of_node(root.left) - self.calculate_height_of_node(root.right)) + 1

    def print_all_nodes(self):
        self.inorder_traversal(self.root)

    def inorder_traversal(self, node):

        if node is None:
            return

        self.inorder_traversal(node.left)
        print(node.value, "->")
        self.inorder_traversal(node.right)


tree_obj = Tree()
tree_obj.insert_from_array([1,2,3])
tree_obj.print_all_nodes()
print(tree_obj.calculate_height_of_node(tree_obj.root))
# print(tree_obj.is_node_imbalanced(tree_obj.root))
