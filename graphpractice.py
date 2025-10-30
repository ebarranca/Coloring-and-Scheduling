import networkx as nx
import pygraphviz as pgv
A = nx.nx_agraph.to_agraph(G)
A.layout(prog='dot') # Use 'dot', 'neato', 'fdp', 'sfdp', 'circo', or 'twopi' for different layouts
A.draw('graph_pygraphviz.png') # Save to a PNG file