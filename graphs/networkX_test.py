import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")
G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

num_nodes = G.number_of_nodes()  # 4
num_edges = G.number_of_edges()  # 4
is_connected = nx.is_connected(G)  # True


degree_centrality = nx.degree_centrality(
    G
)  # {'A': 0.6666666666666666, 'B': 1.0, 'C': 0.6666666666666666, 'D': 0.3333333333333333}
closeness_centrality = nx.closeness_centrality(
    G
)  # {'A': 0.75, 'B': 1.0, 'C': 0.75, 'D': 0.6}
betweenness_centrality = nx.betweenness_centrality(
    G
)  # {'A': 0.0, 'B': 0.6666666666666666, 'C': 0.0, 'D': 0.0}

path = nx.shortest_path(G, source="A", target="D")  # ['A', 'B', 'D']
avg_path_length = nx.average_shortest_path_length(G)  # 1.3333333333333333


# # G = nx.complete_graph(8)
# options = {
#     "node_color": "yellow",
#     "edge_color": "lightblue",
#     "node_size": 500,
#     "width": 3,
#     "with_labels": True,
# }
# # pos = nx.circular_layout(G)
# pos = nx.random_layout(G)
# # pos = [[0, 1, 2], [3, 4], [5, 6, 7]]  # Вказує камери для розташування вершин
# # pos = nx.shell_layout(G, pos)
# nx.draw(G, pos, **options)
# plt.show()


# # Створення орієнтованого графа
# G = nx.DiGraph()

# # Додавання ребер
# G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 3), (4, 1)])

# # Малювання графа
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, arrows=True)

# plt.show()


# Створення графа
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

G = nx.Graph(graph)

# DFS
dfs_tree = nx.dfs_tree(G, source="A")
print(list(dfs_tree.edges()))  # виведе ребра DFS-дерева з коренем у вузлі A

# BFS
bfs_tree = nx.bfs_tree(G, source="A")
print(list(bfs_tree.edges()))  # виведе ребра BFS-дерева з коренем у вузлі A


# Створення графа
G = nx.Graph()

# Додавання міст і доріг
G.add_edge("A", "B", weight=5)
G.add_edge("A", "C", weight=10)
G.add_edge("B", "D", weight=3)
G.add_edge("C", "D", weight=2)
G.add_edge("D", "E", weight=4)

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(
    G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2
)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
