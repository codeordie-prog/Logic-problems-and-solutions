from typing import Any, Optional, List


class TreeNode:
    """
    Represents a node in a binary search tree.

    Attributes:
        val (int): The value stored in the node.
        left (Optional[TreeNode]): Reference to the left child node.
        right (Optional[TreeNode]): Reference to the right child node.
        count (int): Number of times this value appears in the tree.
    """
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None) -> None:
        """
        Initialize a new tree node.

        Args:
            val (int): The value to store in the node.
            left (Optional[TreeNode]): Optional left child node.
            right (Optional[TreeNode]): Optional right child node.
        """
        self.val: int = val
        self.left: Optional['TreeNode'] = left
        self.right: Optional['TreeNode'] = right
        self.count: int = 1

    def __repr__(self) -> str:
        """
        Return a string representation of the node.
        """
        return (f"node: {self.val} (count: {self.count})\n"
                f"left: {self.left}\n"
                f"right: {self.right}")


class Tree:
    """
    A binary search tree implementation.
    """
    def __init__(self) -> None:
        """
        Initialize an empty binary search tree.
        """
        self.root: Optional[TreeNode] = None

    @classmethod
    def insert(cls, node: Optional[TreeNode], key: int) -> TreeNode:
        """
        Insert a value into the tree.

        Args:
            node (Optional[TreeNode]): The current node being processed.
            key (int): The value to insert.

        Returns:
            TreeNode: The updated node.
        """
        if not node:
            return TreeNode(key)
        if key > node.val:
            node.right = cls.insert(node.right, key)
        elif key < node.val:
            node.left = cls.insert(node.left, key)
        else:  # key == node.val
            node.count += 1
        return node

    def insert_node(self, key: int) -> None:
        """
        Insert a value into the tree.

        Args:
            key (int): The value to insert.
        """
        self.root = self.__class__.insert(self.root, key)


class DepthFirstSearch:
    """
    Finds the k-th smallest element in a BST using recursive inorder traversal (DFS).
    """
    def __init__(self, root: Optional[TreeNode], k: int) -> None:
        self.result: int = self.kth_smallest(root, k)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        return self.result

    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Returns the k-th smallest value in the BST using inorder traversal.

        Args:
            root (Optional[TreeNode]): The root of the BST.
            k (int): The k-th position to find (1-indexed).

        Returns:
            int: The k-th smallest value.
        """
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        nodes: List[int] = dfs(root)
        return nodes[k - 1]


class StackSolution:
    """
    Finds the k-th smallest element in a BST using an iterative stack-based inorder traversal.
    """
    def __init__(self, root: Optional[TreeNode], k: int) -> None:
        self.result: int = self.kth_smallest(root, k)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        return self.result

    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Returns the k-th smallest value in the BST using an iterative stack-based inorder traversal.

        Args:
            root (Optional[TreeNode]): The root of the BST.
            k (int): The k-th position to find (1-indexed).

        Returns:
            int: The k-th smallest value.
        """
        stack: List[TreeNode] = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node: TreeNode = stack.pop(-1)
            k -= 1
            if k == 0:
                return node.val
            right: Optional[TreeNode] = node.right
            while right:
                stack.append(right)
                right = right.left
        raise ValueError("k is larger than the number of nodes in the tree.")


def main() -> None:
    """
    Test cases for both DepthFirstSearch and StackSolution.
    """
    # Test case 1
    values1 = [5, 3, 4, 2, 1]
    tree1 = Tree()
    for val in values1:
        tree1.insert_node(val)
    solution_0 = DepthFirstSearch(tree1.root, 4)
    solution_1 = StackSolution(tree1.root, 4)
    assert solution_0() == solution_1() == 4
    print(f"Test 1: {solution_0()} {solution_1()}")

    # Test case 2: left-skewed tree
    values2 = [5, 4, 3, 2, 1]
    tree2 = Tree()
    for val in values2:
        tree2.insert_node(val)
    solution_0 = DepthFirstSearch(tree2.root, 2)
    solution_1 = StackSolution(tree2.root, 2)
    assert solution_0() == solution_1() == 2
    print(f"Test 2: {solution_0()} {solution_1()}")

    # Test case 3: right-skewed tree
    values3 = [1, 2, 3, 4, 5]
    tree3 = Tree()
    for val in values3:
        tree3.insert_node(val)
    solution_0 = DepthFirstSearch(tree3.root, 5)
    solution_1 = StackSolution(tree3.root, 5)
    assert solution_0() == solution_1() == 5
    print(f"Test 3: {solution_0()} {solution_1()}")



if __name__ == "__main__":
    main()


