# This script defines the network topology using a directed graph and adds nodes and edges to represent the devices and their connections. 
# It then uses the Graphviz layout engine to calculate the positions of the nodes in the graph. 
# The script also sets the color and size of the nodes based on their type, such as routers, switches, servers, and database servers. Finally, the script displays the graph with a title and axis labels using Matplotlib.

import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt

# Define network topology
G = nx.DiGraph()
G.add_nodes_from(['Router 1', 'Switch 1', 'Switch 2', 'Server 1', 'Server 2', 'Server 3', 'Server 4', 'Database Server'])
G.add_edges_from([
    ('Router 1', 'Switch 1'),
    ('Router 1', 'Switch 2'),
    ('Switch 1', 'Server 1'),
    ('Switch 1', 'Server 2'),
    ('Switch 2', 'Server 3'),
    ('Switch 2', 'Server 4'),
    ('Server 1', 'Database Server'),
    ('Server 2', 'Database Server'),
    ('Server 3', 'Database Server'),
    ('Server 4', 'Database Server')
])

# Calculate layout using Graphviz
pos = graphviz_layout(G, prog='dot')

# Set node colors and sizes
node_colors = {'Router 1': 'red', 'Switch 1': 'blue', 'Switch 2': 'blue', 'Server 1': 'green', 'Server 2': 'green', 'Server 3': 'green', 'Server 4': 'green', 'Database Server': 'orange'}
node_sizes = {'Router 1': 800, 'Switch 1': 600, 'Switch 2': 600, 'Server 1': 400, 'Server 2': 400, 'Server 3': 400, 'Server 4': 400, 'Database Server': 800}

# Draw the network topology
nx.draw_networkx_nodes(G, pos, node_size=[node_sizes[n]*10 for n in G.nodes()], node_color=[node_colors[n] for n in G.nodes()])
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
nx.draw_networkx_edges(G, pos, arrowsize=10)

# Set plot title and axis labels
plt.title('Network Topology')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show the network topology
plt.show()
