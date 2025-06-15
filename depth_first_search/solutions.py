"""Binary Search Tree implementation with mode finding functionality.

This module implements a Binary Search Tree with the ability to find the mode
(most frequent value) in the tree. It includes two different implementations
for finding the mode: one using DFS and another using inorder traversal.
"""

from typing import Any, Optional, List, Dict
from collections import defaultdict


class TreeNode:
    """A node in a binary search tree.

    Attributes:
        val: The value stored in the node
        left: Reference to the left child node
        right: Reference to the right child node
        count: Number of times this value appears in the tree
    """

    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, 
                 right: Optional['TreeNode'] = None) -> None:
        """Initialize a new tree node.

        Args:
            val: The value to store in the node
            left: Optional left child node
            right: Optional right child node
        """
        self.val = val
        self.left = left
        self.right = right
        self.count = 1

    def __repr__(self) -> str:
        """Return a string representation of the node."""
        return f"""
            node : {self.val} (count: {self.count})
            left : {self.left}
            right : {self.right}
            """


class Tree:
    """A binary search tree implementation."""

    def __init__(self) -> None:
        """Initialize an empty binary search tree."""
        self.root: Optional[TreeNode] = None

    @classmethod
    def insert(cls, node: Optional[TreeNode], key: int) -> TreeNode:
        """Insert a value into the tree.

        Args:
            node: The current node being processed
            key: The value to insert

        Returns:
            The updated node
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
        """Insert a value into the tree.

        Args:
            key: The value to insert
        """
        self.root = self.__class__.insert(self.root, key)


class FindModeInBST:
    """Find the mode in a BST using DFS approach."""

    def __init__(self, tree: Tree) -> None:
        """Initialize with a tree and find its mode.

        Args:
            tree: The binary search tree to analyze
        """
        self.mode = self.findMode(tree)

    def __call__(self) -> List[int]:
        """Return the mode(s) when the class is called.

        Returns:
            List of values that appear most frequently
        """
        return self.mode

    def findMode(self, tree: Tree) -> List[int]:
        """Find the mode(s) in the tree using DFS.

        Args:
            tree: The binary search tree to analyze

        Returns:
            List of values that appear most frequently
        """
        root = tree.root
        if not root:
            return []

        counter: Dict[int, int] = {}

        def dfs(node: Optional[TreeNode], count_dict: Dict[int, int]) -> None:
            if not node:
                return

            count_dict[node.val] = node.count
            dfs(node.left, count_dict)
            dfs(node.right, count_dict)

        dfs(root, counter)
        max_freq = counter[max(counter, key=lambda x: counter[x])]
        return [k for k, v in counter.items() if v == max_freq]


class FindModeBST2:
    """Find the mode in a BST using inorder traversal approach."""

    def __init__(self, tree: Tree) -> None:
        """Initialize with a tree and find its mode.

        Args:
            tree: The binary search tree to analyze
        """
        self.mode = self.findMode(tree)

    def __call__(self) -> List[int]:
        """Return the mode(s) when the class is called.

        Returns:
            List of values that appear most frequently
        """
        return self.mode

    def findMode(self, tree: Tree) -> List[int]:
        """Find the mode(s) in the tree using inorder traversal.

        Args:
            tree: The binary search tree to analyze

        Returns:
            List of values that appear most frequently
        """
        root = tree.root
        if not root:
            return []

        def list_all(node: Optional[TreeNode]) -> List[tuple[int, int]]:
            if not node:
                return []
            return list_all(node.left) + [(node.val, node.count)] + list_all(node.right)

        nodes = list_all(root)
        counter = defaultdict(int)

        for val, count in nodes:
            counter[val] = count

        max_freq = max(counter.values())
        return [node for node, freq in counter.items() if freq == max_freq]


def test_mode_finding() -> None:
    """Run test cases for mode finding functionality."""
    # Test case 1: Single mode
    tree1 = Tree()
    values1 = [1, 2, 2, 2, 3]
    for val in values1:
        tree1.insert_node(val)
    mode1 = FindModeInBST(tree1)
    assert mode1() == [2], "Test case 1 failed"

    # Test case 2: Multiple modes
    tree2 = Tree()
    values2 = [1, 1, 2, 2, 3]
    for val in values2:
        tree2.insert_node(val)
    mode2 = FindModeInBST(tree2)
    assert sorted(mode2()) == [1, 2], "Test case 2 failed"

    # Test case 3: Empty tree
    tree3 = Tree()
    mode3 = FindModeInBST(tree3)
    assert mode3() == [], "Test case 3 failed"

    # Test case 4: All unique values
    tree4 = Tree()
    values4 = [1, 2, 3, 4, 5]
    for val in values4:
        tree4.insert_node(val)
    mode4 = FindModeInBST(tree4)
    assert sorted(mode4()) == [1, 2, 3, 4, 5], "Test case 4 failed"

    print("All test cases passed!")


def main() -> None:
    """Main function to demonstrate the BST mode finding functionality."""
    # Example usage
    values = [6, 4, 4, 4, 5, 9, 4, 4, 5, 5, 5, 5, 5, 5]
    tree = Tree()

    for val in values:
        tree.insert_node(val)

    mode1 = FindModeInBST(tree)
    mode2 = FindModeBST2(tree)

    print("Mode using DFS approach:", mode1())
    print("Mode using inorder approach:", mode2())

    # Run test cases
    test_mode_finding()


if __name__ == "__main__":
    main()



