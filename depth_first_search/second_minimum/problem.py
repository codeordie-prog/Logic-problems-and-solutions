class ProblemStatement:
    """
    Given a non-empty special binary tree consisting of nodes with non-negative values,
    where each node in this tree has exactly two or zero sub-nodes. If the node has two sub-nodes,
    then this node's value is the smaller value among its two sub-nodes. More formally,
    the property root.val = min(root.left.val, root.right.val) always holds.

    Given such a binary tree, output the second minimum value among all the nodes' values
    in the entire tree. If no such second minimum value exists, output -1 instead.
    """


class Specifications:
    """
    Breadth-First Search / Depth-First Search

    Algorithmic Steps:

    1. The second minimum must be the smallest value greater than the true minimum.
    2. List all node values using DFS or BFS and determine the true minimum.
    3. Set the second minimum to infinity.
    4. Iterate through the list and skip values equal to the true minimum.
    5. Update the second minimum by comparing it with the current value.
    6. At the end, return the second minimum if it is not infinity; otherwise, return -1.
    """


class EfficiencyHandling:
    """
    Time Complexity:
        - O(n): Every node is visited once.

    Space Complexity:
        - O(n): Linear space is required to store the list of node values.
    """


class Pseudocode:
    """
    FUNCTION findSecondMinimumValue(root):
        IF NOT root.left AND NOT root.right:
            RETURN -1

        FUNCTION DFS(node):
            FUNCTION LIST_ALL(node):
                IF NOT node:
                    RETURN []
                RETURN [node.val] + LIST_ALL(node.left) + LIST_ALL(node.right)

            NODES = LIST_ALL(node)
            RETURN MIN(NODES), NODES

        TRUE_MIN, NODES = DFS(root)
        SECOND_MINIMUM = INFINITY
        FOR NODE IN NODES:
            IF NODE != TRUE_MIN:
                SECOND_MINIMUM = MIN(SECOND_MINIMUM, NODE)

        IF SECOND_MINIMUM == INFINITY:
            RETURN -1

        RETURN SECOND_MINIMUM
    """