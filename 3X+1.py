import networkx as nx
import matplotlib.pyplot as plt


def generate_tree(n):
    G = nx.DiGraph()
    root = "x"
    queue = [(root, "root", 0)]  # Added a position value
    node_count = 1
    y_pos = 0

    while queue and y_pos < n:
        next_queue = []
        width = len(queue)
        x_pos = -width / 2.0  # starting position for this level
        
        for node, branch_color, _ in queue:
            if branch_color == "root":
                left_child = f"node{node_count}"
                G.add_node(left_child, pos=(x_pos, y_pos - 1))
                G.add_edge(node, left_child, color="red")
                next_queue.append((left_child, "red", x_pos))
                node_count += 1
                x_pos += 1

                right_child = f"node{node_count}"
                G.add_node(right_child, pos=(x_pos, y_pos - 1))
                G.add_edge(node, right_child, color="blue")
                next_queue.append((right_child, "blue", x_pos))
                node_count += 1
                x_pos += 1
            elif branch_color == "red":
                child = f"node{node_count}"
                G.add_node(child, pos=(x_pos, y_pos - 1))
                G.add_edge(node, child, color="red")
                next_queue.append((child, "red", x_pos))
                node_count += 1
                x_pos += 1
            elif branch_color == "blue":
                left_child = f"node{node_count}"
                G.add_node(left_child, pos=(x_pos, y_pos - 1))
                G.add_edge(node, left_child, color="red")
                next_queue.append((left_child, "red", x_pos))
                node_count += 1
                x_pos += 1

                right_child = f"node{node_count}"
                G.add_node(right_child, pos=(x_pos, y_pos - 1))
                G.add_edge(node, right_child, color="blue")
                next_queue.append((right_child, "blue", x_pos))
                node_count += 1
                x_pos += 1

        y_pos -= 1
        queue = next_queue

    return G

def draw_tree(G):
    pos = nx.get_node_attributes(G, 'pos')
    edge_colors = [G[u][v]['color'] for u, v in G.edges()]
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="black", edge_color=edge_colors, width=2.0)
    plt.show()

if __name__ == "__main__":
    generations = int(input("Enter the number of generations: "))
    G = generate_tree(generations)
    draw_tree(G)
