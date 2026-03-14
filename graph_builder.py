def visualize_graph(G):
    
    net = Network(height="600px", width="100%")

    for node in G.nodes:
        net.add_node(node, label=node)

    for edge in G.edges:
        net.add_edge(edge[0], edge[1])

    net.write_html("research_graph.html")