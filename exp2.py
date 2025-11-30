from collections import deque

def input_graph():
    graph = {}
    num_nodes = int(input("Enter number of nodes in the graph: "))
    for i in range(num_nodes):
        node = input(f"Enter name of node {i+1}: ").strip()
        neighbors = input(f"Enter neighbors of {node} (comma-separated): ").strip()
        graph[node] = [n.strip() for n in neighbors.split(",")] if neighbors else []
    return graph

def bfs(graph, start, goal):
    visited = []
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited, path
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return visited, []

graph = input_graph()
start_node = input("Enter start node: ").strip()
goal_node = input("Enter goal node: ").strip()

visited_order, bfs_path = bfs(graph, start_node, goal_node)

print("\n=== BFS ===")
print("Visited Order:", visited_order)
print("Path to Goal:", " -> ".join(bfs_path) if bfs_path else "No path found")
