from typing import Any, List, Dict


class StoreFlagging:
    """
    Sets matrix rows and columns to zero using additional storage space.
    This approach uses a dictionary to store coordinates of cells that need to be set to zero.
    """
    def __init__(self, grid: List[List[int]]) -> None:
        self.result: List[List[int]] = self.set_zeroes(grid)

    def __call__(self, *args: Any, **kwds: Any) -> List[List[int]]:
        return self.result

    def set_zeroes(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Sets entire rows and columns to zero where any element is zero.

        Args:
            grid (List[List[int]]): The input matrix to modify.

        Returns:
            List[List[int]]: The modified matrix with rows and columns set to zero.
        """
        rows: int = len(grid)
        cols: int = len(grid[0])
        store: Dict[tuple, int] = dict()

        def flag(i: int, j: int) -> None:
            """
            Marks all cells in the same row and column as the given position.

            Args:
                i (int): Row index.
                j (int): Column index.
            """
            temp_i: int = 0
            temp_j: int = 0

            while temp_i < rows:
                store[(temp_i, j)] = 0
                temp_i += 1

            while temp_j < cols:
                store[(i, temp_j)] = 0
                temp_j += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    flag(i, j)

        for k in store:
            i: int = k[0]
            j: int = k[1]
            grid[i][j] = 0

        return grid


class OptimizedSpace:
    """
    Sets matrix rows and columns to zero using in-place optimization.
    This approach uses the first row and column as markers to avoid additional storage.
    """
    def __init__(self, grid: List[List[int]]) -> None:
        self.result: List[List[int]] = self.set_zeroes(grid)

    def __call__(self, *args: Any, **kwds: Any) -> List[List[int]]:
        return self.result

    def set_zeroes(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Sets entire rows and columns to zero where any element is zero using in-place optimization.

        Args:
            grid (List[List[int]]): The input matrix to modify.

        Returns:
            List[List[int]]: The modified matrix with rows and columns set to zero.
        """
        rows: int = len(grid)
        cols: int = len(grid[0])

        first_row_has_zeroes: bool = any(grid[0][j] == 0 for j in range(cols))
        first_col_has_zeroes: bool = any(grid[i][0] == 0 for i in range(rows))

        for i in range(1, rows):
            for j in range(1, cols):
                if grid[i][j] == 0:
                    grid[0][j] = 0
                    grid[i][0] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if grid[i][0] == 0 or grid[0][j] == 0:
                    grid[i][j] = 0

        if first_row_has_zeroes:
            for j in range(cols):
                grid[0][j] = 0

        if first_col_has_zeroes:
            for i in range(rows):
                grid[i][0] = 0

        return grid


def main() -> None:
    """
    Test cases for both StoreFlagging and OptimizedSpace classes.
    """
    # Test case 1: Basic case with one zero
    grid1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    result1 = OptimizedSpace(grid1)
    print("Test 1:")
    for row in result1():
        print(row)

    # Test case 2: Multiple zeros
    grid2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    result2 = OptimizedSpace(grid2)
    print("\nTest 2:")
    for row in result2():
        print(row)

    # Test case 3: All zeros
    grid3 = [[0, 0], [0, 0]]
    result3 = OptimizedSpace(grid3)
    print("\nTest 3:")
    for row in result3():
        print(row)

    # Test case 4: No zeros
    grid4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result4 = OptimizedSpace(grid4)
    print("\nTest 4:")
    for row in result4():
        print(row)

    # Test case 5: Single row
    grid5 = [[1, 0, 3]]
    result5 = OptimizedSpace(grid5)
    print("\nTest 5:")
    for row in result5():
        print(row)

    # Test case 6: Single column
    grid6 = [[1], [0], [3]]
    result6 = OptimizedSpace(grid6)
    print("\nTest 6:")
    for row in result6():
        print(row)


if __name__ == "__main__":
    main()
