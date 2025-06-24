class ProblemStatement:
    """
    There is a bidirectional graph with n vertices, labeled from 0 to n - 1 (inclusive).
    The edges are represented as a 2D integer array, where each edges[i] = [ui, vi] denotes
    a bidirectional edge between vertex ui and vertex vi. Each vertex pair is connected by at most one edge,
    and no vertex has an edge to itself.
    Determine if there is a valid path from the source vertex to the destination vertex.
    Given edges and the integers n, source, and destination, return True if a valid path exists from source to destination,
    otherwise return False.
    """


class Specifications:
    """
    Solution Specifications

    Approach 1 - Breadth-First Search (BFS):
    1. If the source is the destination, return True.
    2. Create a bidirectional adjacency list for the graph.
    3. If the source is a direct neighbor of the destination (or vice versa), return True.
    4. Initialize a set called 'visited' to keep track of visited vertices.
    5. Initialize a queue and enqueue the source vertex.
    6. Use an index pointer to track the next vertex in the queue.
    7. While the queue is not empty, dequeue the current vertex and mark it as visited.
    8. Visit all neighbors of the current vertex:
        a. If a neighbor is the destination, return True.
        b. If a neighbor has not been visited, mark it as visited and enqueue it.
    9. If the destination has not been reached after exploring all possible paths, return False.
    """


class EfficiencyAnalysis:
    """
    Time and Space Complexity Analysis

    Time Complexity: O(V + E)
        - V is the number of vertices.
        - E is the number of edges.

    Space Complexity: O(N)
        - The queue grows linearly in the worst case: O(N).
        - The visited set grows linearly in the worst case: O(N).
    """


class Pseudocode:
    """
    Pseudocode for Solution Approach

    def validPath(n, edges, source, destination):
        if source == destination:
            return True

        adjacency_list = defaultdict(list)
        for v1, v2 in edges:
            adjacency_list[v1].append(v2)
            adjacency_list[v2].append(v1)

        if source in adjacency_list[destination] or destination in adjacency_list[source]:
            return True

        queue = [source]
        idx = 0
        visited = set()

        while idx < len(queue):
            current = queue[idx]
            idx += 1
            visited.add(current)

            for neighbour in adjacency_list[current]:
                if neighbour == destination:
                    return True
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return False
    """