import networkx as nx


def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float("infinity"):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\\n")


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

        # Вивід таблиці після кожного кроку
        print_table(distances, visited)

    return distances


# Приклад графа у вигляді словника
graph = {
    "A": {"B": 5, "C": 10},
    "B": {"A": 5, "D": 3},
    "C": {"A": 10, "D": 2},
    "D": {"B": 3, "C": 2, "E": 4},
    "E": {"D": 4},
}

# Виклик функції для вершини A
dijkstra(graph, "A")


# Створення графа
G = nx.Graph()

# Додавання міст і доріг
G.add_edge("A", "B", weight=5)
G.add_edge("A", "C", weight=10)
G.add_edge("B", "D", weight=3)
G.add_edge("C", "D", weight=2)
G.add_edge("D", "E", weight=4)

# Застосування алгоритму Дейкстри
shortest_paths = nx.single_source_dijkstra_path(G, source="A")
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source="A")
print()
print(shortest_paths)  # виведе найкоротші шляхи від вузла 'A' до всіх інших вузлів
print(
    shortest_path_lengths
)  # виведе довжини найкоротших шляхів від вузла 'A' до всіх інших вузлів
