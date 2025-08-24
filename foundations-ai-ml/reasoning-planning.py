from queue import PriorityQueue

def a_star(start, goal, graph, h):
    """
        A* pathfinding algorithm implementation.
    """
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: h[start]}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            path.insert(0, start)  # Add the start node
            return path

        for neighbor in graph[current]:
            tentative_g = g_score[current] + graph[current][neighbor]
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h[neighbor]
                open_set.put((f_score[neighbor], neighbor))
    
    return None

# Example usage
if __name__ == "__main__":
    # Example graph representation
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    # Heuristic values (estimated distance to goal)
    heuristic = {
        'A': 3,
        'B': 2,
        'C': 1,
        'D': 0
    }
    
    # Find path from A to D
    path = a_star('A', 'D', graph, heuristic)
    if path:
        print(f"Path found: {' -> '.join(path)}")
        print(f"Total cost: {len(path) - 1}")
    else:
        print("No path found")