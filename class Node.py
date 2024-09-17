import tkinter as tk

class Node:
    def __init__(self, color, value=None):
        self.color = color
        self.value = value
        self.left = None
        self.right = None

def create_tree(x, generations):
    root = Node(x)

    if generations == 0:
        return root

    root.left = create_tree("red", generations-1)
    root.right = create_tree("blue", generations-1)

    if root.color == "red":
        root.left.left = create_tree("blue", generations-1)
        root.left.right = create_tree("red", generations-1)
    else:
        root.right.left = create_tree("red", generations-1)

    return root

def draw_tree(root, x, y, canvas, x_offset=0):
    if not root:
        return

    if root.color == "red":
        color = "red"
    else:
        color = "blue"

    r = 5
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvas.create_oval(x0, y0, x1, y1, fill=color, outline=color)

    if root.left:
        canvas.create_line(x+x_offset, y, x-50+x_offset, y+50, fill="black")
        draw_tree(root.left, x-50, y+50, canvas, x_offset=x_offset)
    if root.right:
        canvas.create_line(x+x_offset, y, x+50+x_offset, y+50, fill="black")
        draw_tree(root.right, x+50, y+50, canvas, x_offset=x_offset)

def main():
    # Create the main window
    window = tk.Tk()
    window.title("Binary Tree")

    # Create the canvas
    canvas = tk.Canvas(window, width=800, height=600)
    canvas.pack()

    # Prompt the user for the number of generations
    generations = int(input("Enter the number of generations: "))

    # Create the binary tree
    root = create_tree("red", generations)

    # Determine the number of nodes at the deepest level of the tree
    deepest_level = 2 ** generations
    x_offset = (800 - (50 * (deepest_level - 1))) // 2

    # Draw the tree on the canvas
    draw_tree(root, 400, 50, canvas, x_offset=x_offset)

    # Start the main loop
    window.mainloop()

if __name__ == "__main__":
    main()
