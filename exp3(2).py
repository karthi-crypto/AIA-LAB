def a_star(graph, h, start, goal):
    open_list = [(start, [start], 0)]
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: x[2] + h[x[0]])  # f = g + h
        current, path, cost = open_list.pop(0)

        if current == goal:
            return path, cost

        visited.add(current)

        for neighbor, edge_cost in graph.get(current, []):
            if neighbor not in visited:
                open_list.append((neighbor, path + [neighbor], cost + edge_cost))
    return None, None

def greedy_best_first_search(graph, h, start, goal):
    open_list = [(start, [start])]
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: h[x[0]])  # Sort by heuristic only
        current, path = open_list.pop(0)

        if current == goal:
            # Calculate path cost
            cost = 0
            for i in range(len(path) - 1):
                for neighbor, edge_cost in graph[path[i]]:
                    if neighbor == path[i + 1]:
                        cost += edge_cost
                        break
            return path, cost

        visited.add(current)

        for neighbor, edge_cost in graph.get(current, []):
            if neighbor not in visited:
                open_list.append((neighbor, path + [neighbor]))
    return None, None

# Input reading (same as before)
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

path_a_star, cost_a_star = a_star(graph, h, start, goal)
path_greedy, cost_greedy = greedy_best_first_search(graph, h, start, goal)

print("\nFinal Output")
print("Algorithm: A* Search")
if path_a_star:
    print("Path:", " -> ".join(path_a_star))
    print("Total Cost:", cost_a_star)
else:
    print("No valid path found by A*.")

print("\nAlgorithm: Greedy Best-First Search")
if path_greedy:
    print("Path:", " -> ".join(path_greedy))
    print("Total Cost:", cost_greedy)
else:
    print("No valid path found by Greedy Best-First Search.")
