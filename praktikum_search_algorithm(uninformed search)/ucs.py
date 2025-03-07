import networkx as nx

def uniform_cost_search_nx(graph, start, goal):
  visited = []
  queue = [[0, [start]]]

  while queue:
    cost, node, path = min(queue, key=lambda item: item[0])
    queue.remove((cost, node, path))

    if node == goal:
      return cost, path + [cost]

    visited.add(node)

    for neighbor in graph.neighbors(node):
      if neighbor not in visited :
        edge_cost = graph[node][neighbor]['weight']
        queue.append((cost + edge_cost, neighbor, path + [node]))

  return float('inf'), []

  graph = nx.Graph()
  graph.add_edge(0, 1, weight=2)
  graph.add_edge(0, 3, weight=5)
  graph.add_edge(3, 1, weight=5)
  graph.add_edge(3, 6, weight=6)
  graph.add_edge(3, 4, weight=2)
  graph.add_edge(1, 6, weight=1)
  graph.add_edge(4, 5, weight=3)
  graph.add_edge(2, 5, weight=5)
  graph.add_edge(5, 6, weight=3)
  graph.add_edge(6, 4, weight=7)

  start_node = 0
  goal_node = 5

  min_cost, path = uniform_cost_search_nx(graph, start, goal_node)

  if min_cost == float('inf'):
    print("Goal node is unreachable.")
  else:
    print(f"Minimum cost : ",min_cost)
    print("Path : ", path)
