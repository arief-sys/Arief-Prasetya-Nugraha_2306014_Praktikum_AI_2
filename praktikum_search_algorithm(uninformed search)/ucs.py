import networkx as nx

def uniform_cost_search_nx(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]  # (cost, node, path)

    while queue:
        queue.sort()  # Sorting berdasarkan cost terkecil
        cost, node, path = queue.pop(0)  # Ambil elemen dengan cost terkecil
        
        if node in visited:
            continue
        
        path = path + [node]  # Perbarui jalur saat ini
        visited.add(node)

        # Jika mencapai node tujuan, kembalikan hasil
        if node == goal:
            return cost, path

        # Menelusuri tetangga
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                edge_cost = graph[node][neighbor]['weight']
                queue.append((cost + edge_cost, neighbor, path))

    return float('inf'), []

# Membuat graph
graph = nx.Graph()
graph.add_edge(0, 1, weight=2)
graph.add_edge(0, 3, weight=5)
graph.add_edge(3, 1, weight=5)
graph.add_edge(3, 6, weight=6)
graph.add_edge(3, 4, weight=2)
graph.add_edge(1, 6, weight=1)
graph.add_edge(4, 2, weight=4)
graph.add_edge(4, 5, weight=3)
graph.add_edge(2, 1, weight=4)
graph.add_edge(5, 2, weight=6)
graph.add_edge(5, 6, weight=3)
graph.add_edge(6, 4, weight=7)

# Menjalankan UCS
start_node = 0
goal_node = 6
min_cost, path = uniform_cost_search_nx(graph, start_node, goal_node)

# Menampilkan hasil
if min_cost == float('inf'):
    print("Goal node is unreachable.")
else:
    print("Minimum cost from 0 to 6 is =",min_cost)
