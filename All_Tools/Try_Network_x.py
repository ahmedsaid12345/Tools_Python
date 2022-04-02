import networkx as nx
from pyvis.network import Network
G=nx.Graph()

Net=Network(notebook=True)
#G.add_nodes_from([
 #   (4, {"color": "red"}),
 #   (5, {"color": "green"}),
#])
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')


print(G.number_of_nodes())
print(G.nodes)
print(G.edges)
Net.from_nx(G)
#print(nx.draw_networkx(G))
#nx.draw_networkx(G)
Net.show("C:/Try.html")



