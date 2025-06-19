from typing import Optional, List, Tuple

class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

    def __repr__(self) -> str:
        return (
            f"\n        node  : {self.val}\n"
            f"        left  : {self.left}\n"
            f"        right : {self.right}\n       "
        )


class Tree:
    def __init__(self, leaf_vals: List[int]) -> None:
        self.root: Node = self.build_special_min_tree(leaf_vals)

    def build_special_min_tree(self, leaf_vals: List[int]) -> Node:
        if len(leaf_vals) == 0 or (len(leaf_vals) & (len(leaf_vals) - 1)) != 0:
            raise ValueError("Number of leaves must be a power of 2")

        nodes: List[Node] = [Node(val) for val in leaf_vals]

        while len(nodes) > 1:
            next_level: List[Node] = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i + 1]
                parent_val = min(left.val, right.val)
                parent = Node(parent_val)
                parent.left = left
                parent.right = right
                next_level.append(parent)
            nodes = next_level

        return nodes[0]  # root


class Solution:
    def __init__(self, root: Node) -> None:
        self.result: int = self.find_second_minimum(root)

    def find_second_minimum(self, root: Node) -> int:
        if not root.left and not root.right:
            return -1

        def breadth_first_search(node: Optional[Node]) -> Tuple[int, List]:
            def list_all(node: Optional[Node]) -> List[int]:
                if not node:
                    return []
                return [node.val] + list_all(node.left) + list_all(node.right)

            nodes = list_all(node)
            return min(nodes), nodes

        true_minimum, nodes = breadth_first_search(root)
        second_minimum = float("inf")

        for node_val in nodes:
            if node_val != true_minimum:
                second_minimum = min(second_minimum, node_val)

        if second_minimum == float("inf"):
            return -1

        return int(second_minimum)


def main() -> None:
    leaf_vals: List[int] = [2, 5, 5, 7]
    tree = Tree(leaf_vals)
    solution = Solution(tree.root)
    second_minimum = solution.result
    print(f"Second minimum value: {second_minimum}")


if __name__ == "__main__":
    main()
