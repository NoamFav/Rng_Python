import networkx as nx
import matplotlib.pyplot as plt

def draw_collatz_tree(tree):
    # Create a new graph
    graph = nx.DiGraph()
    # Recursively add nodes and edges to the graph
    add_nodes_and_edges(tree, graph, 0, 0)
    return graph

def add_nodes_and_edges(tree, graph, x, y):
    # Add the current node to the graph
    node_id = str(tree[0])
    graph.add_node(node_id, pos=(x, y))
    # Compute the positions of the children
    children = tree[1]
    num_children = len(children)
    if num_children == 1:
        x_step = 0
        y_step = -1
    elif num_children == 2:
        x_step = -1
        y_step = -1
    else:
        x_step = -1
        y_step = 0
    # Add edges between the current node and its children
    for i, child in enumerate(children):
        child_id = str(child[0])
        graph.add_node(child_id, pos=(x + i * x_step, y + y_step))
        graph.add_edge(node_id, child_id)
        # Recurse on the children
        add_nodes_and_edges(child, graph, x + i * x_step, y + y_step)

def collatz_tree(n, depth=10):
    # Base case: if the depth is 0 or the number is 1, return a leaf node
    if depth == 0 or n == 1:
        return (n, [])
    # Recursive case: if the number is even, add two child nodes
    if n % 2 == 0:
        return (n, [collatz_tree(n / 2, depth - 1), collatz_tree(3 * n + 1, depth - 1)])
    # Recursive case: if the number is odd, add one child node
    return (n, [collatz_tree(3 * n + 1, depth - 1)])

# Generate the Collatz tree for the number 5 with a depth of 5
tree = collatz_tree(5, 20)

# Draw the tree
graph = draw_collatz_tree(tree)

# Show the graph
pos = nx.get_node_attributes(graph, 'pos')
nx.draw(graph, pos, with_labels=False, node_size=50)
plt.show()