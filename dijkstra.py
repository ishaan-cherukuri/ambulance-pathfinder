import heapq

class Graph:
    def __init__(self, edges):
        """
        edges: list of tuples like [((x1, y1), (x2, y2), weight), ...]
        """
        self.graph = {}
        for src, dest, weight in edges:
            if src not in self.graph:
                self.graph[src] = {}
            if dest not in self.graph:
                self.graph[dest] = {}
            self.graph[src][dest] = weight
            self.graph[dest][src] = weight  # Assuming undirected graph

    def dijkstra(self, start, end):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        previous = {}

        heap = [(0, start)]

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(heap, (distance, neighbor))

        # Reconstruct path
        path = []
        current = end
        while current in previous:
            path.insert(0, current)
            current = previous[current]

        if current == start:
            path.insert(0, start)
            return path, distances[end]
        else:
            return [], float("inf")
