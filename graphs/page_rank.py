import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.DiGraph()  # Створення спрямованого графа

# Додавання вершин та ребер до графа
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "A"), ("D", "C")]
G.add_edges_from(edges)

# Застосування алгоритму PageRank
pagerank = nx.pagerank(G, alpha=0.85)  # alpha - це фактор згладжування

# Виведення результатів PageRank
for node, rank in pagerank.items():
    print(f"{node}: {rank}")

# Візуалізація графа:
plt.figure(figsize=(6, 6))
nx.draw_networkx(G, with_labels=True)
plt.show()
