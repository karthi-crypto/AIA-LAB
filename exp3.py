def a_star(graph, h, start, goal):
    print("\nA* Algorithm")
    # open_list holds tuples: (node, path_to_node, cost_so_far)
    open_list = [(start, [start], 0)]
    visited = set()

    while open_list:
        # Sort open list by f = g + h (cost + heuristic)
        open_list.sort(key=lambda x: x[2] + h[x[0]])
        current, path, cost = open_list.pop(0)
        print("Visiting:", current)

        if current == goal:
            print("\nGoal Reached!")
            return path

        visited.add(current)

        for neighbor, edge_cost in graph.get(current, []):
            if neighbor not in visited:
                total_cost = cost + edge_cost  # g(neighbor) = g(current) + edge_cost
                open_list.append((neighbor, path + [neighbor], total_cost))

    print("\nNo Path Found.")
    return None


graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ").strip()
    neighbors = input(f"Enter neighbors of {node} as (name cost), separated by commas: ").strip()
    neighbor_list = []
    if neighbors:
        for pair in neighbors.split(','):
            name, cost = pair.strip().split()
            neighbor_list.append((name, int(cost)))
    graph[node] = neighbor_list

h = {}
print("Enter heuristic values:")
for node in graph:
    h[node] = int(input(f"Heuristic for {node}: "))

start = input("Enter start node: ").strip()
goal = input("Enter goal node: ").strip()

result = a_star(graph, h, start, goal)

print("\nFinal Output")
print("Algorithm: A* Search")
if result:
    print("Path:", " -> ".join(result))
else:
    print("No valid path.")
