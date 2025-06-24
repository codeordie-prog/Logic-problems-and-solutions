from collections import defaultdict
from typing import Any, List


class BreadthFirstSearch:
    def __init__(self, n: int, edges: List[List[int]], source: int, destination: int) -> None:
        self.result: bool = self.valid_path(n, edges, source, destination)

    def __call__(self, *args: Any, **kwargs: Any) -> bool:
        return self.result

    def valid_path(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int
    ) -> bool:
        if source == destination:
            return True
        adjacency_list: defaultdict[int, List[int]] = defaultdict(list)
        for v1, v2 in edges:
            adjacency_list[v1].append(v2)
            adjacency_list[v2].append(v1)

        if source in adjacency_list[destination] or destination in adjacency_list[source]:
            return True

        queue: List[int] = [source]
        idx: int = 0
        visited: set[int] = set()

        while idx < len(queue):
            current: int = queue[idx]
            idx += 1
            visited.add(current)

            for neighbour in adjacency_list[current]:
                if neighbour == destination:
                    return True
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return False

def main() -> None:
    # Test case 1: Cycle
    n1 = 3
    edges1 = [[0, 1], [1, 2], [2, 0]]
    source1 = 0
    destination1 = 2
    result1 = BreadthFirstSearch(n1, edges1, source1, destination1)
    print(f"Test 1: {result1()} (Expected: True)")

    # Test case 2: Disconnected
    n2 = 6
    edges2 = [[0, 1], [2, 3], [4, 5]]
    source2 = 0
    destination2 = 5
    result2 = BreadthFirstSearch(n2, edges2, source2, destination2)
    print(f"Test 2: {result2()} (Expected: False)")

    # Test case 3: Direct connection
    n3 = 2
    edges3 = [[0, 1]]
    source3 = 0
    destination3 = 1
    result3 = BreadthFirstSearch(n3, edges3, source3, destination3)
    print(f"Test 3: {result3()} (Expected: True)")

    # Test case 4: Single node
    n4 = 1
    edges4: List[List[int]] = []
    source4 = 0
    destination4 = 0
    result4 = BreadthFirstSearch(n4, edges4, source4, destination4)
    print(f"Test 4: {result4()} (Expected: True)")

    # Test case 5: Path exists in a tree
    n5 = 5
    edges5 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    source5 = 0
    destination5 = 4
    result5 = BreadthFirstSearch(n5, edges5, source5, destination5)
    print(f"Test 5: {result5()} (Expected: True)")

    # Test case 6: No path exists
    n6 = 4
    edges6 = [[0, 1], [2, 3]]
    source6 = 0
    destination6 = 3
    result6 = BreadthFirstSearch(n6, edges6, source6, destination6)
    print(f"Test 6: {result6()} (Expected: False)")

if __name__ == "__main__":
    main()


