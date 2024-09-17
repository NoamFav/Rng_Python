import matplotlib.pyplot as plt
import networkx as nx
import random as r

class TreeNode:
    def __init__(self, key, depth=0, position=0):
        self.left = None
        self.right = None
        self.val = key
        self.depth = depth
        self.position = position

class BinaryTree:
    def __init__(self, max_depth):
        self.root = None
        self.max_depth = max_depth
        self.nodes = []
        self.edges = []

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
            self.nodes.append((self.root.depth, self.root.position, self.root.val))
        else:
            self._insert_recursive(self.root, key, 1, 0)

    def _insert_recursive(self, node, key, depth, position):
        if depth > self.max_depth:
            return  # Do not insert if the depth exceeds max depth

        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key, depth, position - 1)
                self.nodes.append((node.left.depth, node.left.position, node.left.val))
                self.edges.append(((node.depth, node.position), (node.left.depth, node.left.position)))
            else:
                self._insert_recursive(node.left, key, depth + 1, position - 1)
        else:
            if node.right is None:
                node.right = TreeNode(key, depth, position + 1)
                self.nodes.append((node.right.depth, node.right.position, node.right.val))
                self.edges.append(((node.depth, node.position), (node.right.depth, node.right.position)))
            else:
                self._insert_recursive(node.right, key, depth + 1, position + 1)

    def plot_tree(self):
        G = nx.DiGraph()
        G.add_nodes_from([(x[:2], {"label": x[2]}) for x in self.nodes])
        G.add_edges_from(self.edges)

        pos = {(depth, position): (-position, -depth) for depth, position, _ in self.nodes}
        labels = {node: G.nodes[node]["label"] for node in G.nodes()}

        nx.draw(G, pos, labels=labels, with_labels=True, node_size=2000, node_color="skyblue")
        plt.title("Binary Tree Visualization")
        plt.show()

# Example usage
max_depth = 20
tree = BinaryTree(max_depth)
for i in range(100):
    tree.insert(r.randint(1,1000))

# Plotting the tree
tree.plot_tree()