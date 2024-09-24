import plotly.graph_objects as go


# Create the first two branches
fig = go.Figure(go.Scatter(x=[0, 1], y=[0, 0], mode='lines', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=[0, -1], y=[0, 0], mode='lines', line=dict(color='red')))

# Define the recursive function to generate the tree
def create_tree(fig, x, y, depth, is_red):
    if depth == 0:
        return fig
    
    if is_red:
        # Create a blue branch
        fig.add_trace(go.Scatter(x=[x, x+1], y=[y, y-1], mode='lines', line=dict(color='blue')))
        fig = create_tree(fig, x+1, y-1, depth-1, False)
    else:
        # Create a blue branch
        fig.add_trace(go.Scatter(x=[x, x+1], y=[y, y-1], mode='lines', line=dict(color='blue')))
        fig = create_tree(fig, x+1, y-1, depth-1, False)
        # Create a red branch
        fig.add_trace(go.Scatter(x=[x, x-1], y=[y, y-1], mode='lines', line=dict(color='red')))
        fig = create_tree(fig, x-1, y-1, depth-1, True)
        
    return fig

# Call the recursive function to generate the tree
fig = create_tree(fig, 1, 0, 15, False)

# Set layout options and show the figure
fig.update_layout(title='Tree Example', showlegend=False)
fig.show()
