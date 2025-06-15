class ProblemStatement:
    """Problem: Find Mode in Binary Search Tree with Duplicates.

    Given the root of a binary search tree (BST) with duplicates, return all the mode(s) 
    (i.e., the most frequently occurred element) in it.
    If the tree has more than one mode, return them in any order.

    BST Definition:
    - The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    - The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    - Both the left and right subtrees must also be binary search trees.
    """


class Specifications:
    """Solution Specifications.

    Approach 1 - Depth First Search (DFS):
    1. Perform a DFS traversal of the BST
    2. Use a counter (defaultdict) to track frequency of each value
    3. Find the maximum frequency among all values
    4. Collect all values that have the maximum frequency

    Approach 2 - Inorder Traversal:
    1. Perform an inorder traversal to get sorted list of (value, count) pairs
    2. Use a counter to track frequency of each value
    3. Find the maximum frequency
    4. Collect all values with maximum frequency

    Edge Cases:
    - Empty tree
    - Single node tree
    - All unique values
    - Multiple modes
    - All same values
    """


class EfficiencyAnalysis:
    """Time and Space Complexity Analysis.

    Time Complexity: O(n)
    - We visit each node exactly once in both approaches
    - DFS traversal: O(n)
    - Inorder traversal: O(n)
    - Finding max frequency: O(n)
    - Collecting modes: O(n)

    Space Complexity: O(n)
    - Recursion stack: O(h) where h is height of tree
    - Counter storage: O(n) in worst case (all unique values)
    - Result list: O(n) in worst case (all values are modes)

    Note: For a balanced BST, space complexity would be O(log n) for recursion stack
    """


class Pseudocode:
    """Pseudocode for Solution Approaches.

    Approach 1 - DFS:
    FUNCTION findMode(root):
        counter = defaultdict(int)
        
        FUNCTION dfs(node, counter):
            IF node is None:
                RETURN
            
            counter[node.val] += 1
            dfs(node.left, counter)
            dfs(node.right, counter)
        
        dfs(root, counter)
        max_freq = max(counter.values())
        result = [val for val, freq in counter.items() if freq == max_freq]
        RETURN result

    Approach 2 - Inorder:
    FUNCTION findMode(root):
        FUNCTION inorder(node):
            IF node is None:
                RETURN []
            RETURN inorder(node.left) + [(node.val, node.count)] + inorder(node.right)
        
        nodes = inorder(root)
        counter = defaultdict(int)
        FOR val, count IN nodes:
            counter[val] = count
        
        max_freq = max(counter.values())
        result = [val for val, freq in counter.items() if freq == max_freq]
        RETURN result
    """