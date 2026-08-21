import heapq

def best_first_search(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    visited = set()
    parent = {start: None}

    while open_list:
        h, current = heapq.heappop(open_list)

        if current in visited:
            continue

        print("Visiting:", current)
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Goal reached!")
            print("Path:", path)

            return path

        visited.add(current)

        for neighbour in graph[current]:

            if neighbour not in visited:

                parent[neighbour] = current

                heapq.heappush(
                    open_list,
                    (heuristic[neighbour], neighbour)
                )

    print("Goal not found")
    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J'],
    'G': ['K'],
    'H': ['P'],
    'I': ['P'],
    'J': ['P'],
    'K': ['P'],
    'P': []
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 6,
    'D': 7,
    'E': 5,
    'F': 4,
    'G': 2,
    'H': 6,
    'I': 3,
    'J': 2,
    'K': 1,
    'P': 0
}
start = 'A'
goal = 'P'

best_first_search(graph, heuristic, start, goal)