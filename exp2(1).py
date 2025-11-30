def input_graph():
    graph = {}
    num_nodes = int(input("Enter number of nodes in the graph: "))
    for i in range(num_nodes):
        node = input(f"Enter name of node {i+1}: ").strip()
        neighbors = input(f"Enter neighbors of {node} (comma-separated): ").strip()
        graph[node] = [n.strip() for n in neighbors.split(",")] if neighbors else []
    return graph

def dfs(graph, start, goal):
    visited = []
    stack = [[start]]
    while stack:
        path = stack.pop()
        node = path[-1]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited, path
            # Reverse neighbors to maintain correct DFS order when using stack
            for neighbor in reversed(graph.get(node, [])):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return visited, []

graph = input_graph()
start_node = input("Enter start node: ").strip()
goal_node = input("Enter goal node: ").strip()

visited_order, dfs_path = dfs(graph, start_node, goal_node)

print("\n=== DFS ===")
print("Visited Order:", visited_order)
print("Path to Goal:", " -> ".join(dfs_path) if dfs_path else "No path found")
