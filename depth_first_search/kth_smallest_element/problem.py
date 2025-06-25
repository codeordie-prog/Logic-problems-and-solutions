class ProblemStatement:
    """
    Given the root of a binary search tree and an integer k, return the k-th smallest value (1-indexed)
    among all the values of the nodes in the tree.
    """


class Specifications:
    """
    Approach 1: DFS (Inorder Traversal)

    1. Perform an inorder traversal to obtain a sorted list of node values.
    2. Return the (k-1)-th element from the sorted list (since list indices are 0-based).

    Approach 2: Iterative Stack-Based Inorder Traversal

    1. Use a stack to perform an inorder traversal, visiting nodes in ascending order.
    2. Stop after visiting k nodes and return the value of the k-th node visited.
    """


class EfficiencyHandling:
    """
    Time Complexity:
    - Both approaches have O(N) time complexity, where N is the number of nodes in the tree.
    - However, the stack-based approach is more efficient in practice, as it only traverses up to k nodes.

    Space Complexity:
    - O(N) for the DFS approach (due to the list of all node values).
    - O(H) for the stack approach, where H is the height of the tree (due to the stack).
    """


class Pseudocode:
    """
    Approach 1 - DFS (Recursive Inorder Traversal)

    FUNCTION kth_smallest(root, k):
        FUNCTION dfs(node):
            IF node IS None:
                RETURN []
            RETURN dfs(node.left) + [node.val] + dfs(node.right)
        nodes = dfs(root)
        RETURN nodes[k-1]

    Approach 2 - Iterative Stack-Based Inorder Traversal

    FUNCTION kth_smallest(root, k):
        stack = []
        WHILE root IS NOT None:
            stack.append(root)
            root = root.left
        WHILE stack IS NOT EMPTY:
            node = stack.pop()
            k -= 1
            IF k == 0:
                RETURN node.val
            right = node.right
            WHILE right IS NOT None:
                stack.append(right)
                right = right.left
    """