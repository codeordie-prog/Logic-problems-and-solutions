from typing import Dict, Tuple, Final


class RecursionPlusMemoization:
    """
    This class implements the solution for the Unique Paths problem using recursion with memoization.
    It calculates the number of unique paths from top-left to bottom-right of an m x n grid,
    where the robot can only move right or down.

    Time Complexity:
        - Without memoization: O(2^(m*n)) - Exponential
            * At each cell, we make 2 recursive calls (right and down)
            * This leads to a binary tree of height (m+n)
            * Total nodes in the tree = 2^(m+n)
        - With memoization: O(m*n)
            * Each cell is visited exactly once
            * Total number of cells = m*n
            * Each cell's result is stored in memo for O(1) lookup

    Space Complexity:
        - O(m*n) for the memoization dictionary
            * In worst case, we store results for all cells
        - O(m+n) for the recursion call stack
            * Maximum depth of recursion = m+n (path from start to end)
        - Total: O(m*n) (dominated by memoization storage)

    Attributes:
        result (int): The number of unique paths calculated for the given grid dimensions.
    """

    def __init__(self, m: int, n: int) -> None:
        """
        Initialize the solution with grid dimensions and calculate the result.

        Args:
            m (int): Number of rows in the grid
            n (int): Number of columns in the grid
        """
        self.result: int = self.unique_paths(m, n)

    def __call__(self) -> int:
        """
        Return the calculated result when the class instance is called.

        Returns:
            int: The number of unique paths
        """
        return self.result

    def unique_paths(self, m: int, n: int) -> int:
        """
        Calculate the number of unique paths using recursion with memoization.

        Args:
            m (int): Number of rows in the grid
            n (int): Number of columns in the grid

        Returns:
            int: Number of unique paths from top-left to bottom-right
        """
        # Initialize memo
        memo: Dict[Tuple[int, int], int] = {}

        def find_paths(i: int, j: int) -> int:
            """
            Helper function to find unique paths using recursion and memoization.

            Args:
                i (int): Current row position
                j (int): Current column position

            Returns:
                int: Number of unique paths from current position to destination
            """
            # Define base case
            if i == m - 1 and j == n - 1:
                return 1

            # Handle invalid paths - out of bounds
            if i > m - 1 or j > n - 1:
                return 0

            # Check if explored before
            if (i, j) in memo:
                return memo[(i, j)]

            # Explore both paths
            path_1: int = find_paths(i + 1, j)  # Move down
            path_2: int = find_paths(i, j + 1)  # Move right

            # Capture their results
            memo[(i, j)] = path_1 + path_2

            return memo[(i, j)]

        return find_paths(0, 0)


def main() -> None:
    """
    Main function to demonstrate the solution with example inputs.
    """
    m: Final[int] = 3
    n: Final[int] = 7
    results_with_recursion = RecursionPlusMemoization(m, n)
    print(f"Number of unique paths for {m}x{n} grid: {results_with_recursion()}")


if __name__ == "__main__":
    main()
