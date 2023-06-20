import networkx as nx
import matplotlib.pyplot as plt

# Create an empty undirected graph
G = nx.Graph()

# Define the vertices
vertices = ['A', 'B', 'C', 'D', 'E', 'F']

# Add the vertices to the graph
G.add_nodes_from(vertices)

# Define the edges
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('F', 'D'), ('E', 'F'), ('C', 'F')]

# Add the edges to the graph
G.add_edges_from(edges)

# Define the positions of the vertices
pos = {'A': (0, 1), 'B': (0.95, 0.31), 'C': (0.59, -0.81),
       'D': (-0.59, -0.81), 'E': (-0.95, 0.31), 'F': (0, 0)}

# Draw the graph with specified positions and node labels
nx.draw(G, pos=pos, with_labels=False, node_color='lightblue', node_size=1000, font_size=12, font_weight='bold')

# Add custom labels to nodes
custom_labels = {'A': 'A (2)', 'B': 'B (4)', 'C': 'C (8)',
                 'D': 'D (8)', 'E': 'E (6)', 'F': 'F (8)'}
nx.draw_networkx_labels(G, pos=pos, labels=custom_labels, font_size=10, font_color='black', font_weight='bold')

# Show the graph
plt.axis('off')
plt.show()
