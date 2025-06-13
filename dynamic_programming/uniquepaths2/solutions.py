from typing import Any, Callable, Dict, List, Tuple


class RecursionPlusMemoization:
    """Solution using recursion with memoization approach.
    
    This approach uses a dictionary to cache results of previously
    calculated paths, significantly improving the time complexity
    from exponential to O(m*n).
    """
    
    def __init__(self, grid: List[List[int]]) -> None:
        """Initialize with input grid and compute result.
        
        Args:
            grid: 2D list representing the grid with obstacles (1) and spaces (0)
        """
        self.paths: int = self.unique_paths(grid)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """Return the computed result.
        
        Returns:
            int: Number of unique paths from top-left to bottom-right
        """
        return self.paths
    
    def unique_paths(self, grid: List[List[int]]) -> int:
        """Calculate number of unique paths avoiding obstacles.
        
        Args:
            grid: 2D list representing the grid with obstacles (1) and spaces (0)
            
        Returns:
            int: Number of unique paths from top-left to bottom-right
        """
        if grid[-1][-1] == 1:
            return 0
        
        rows: int = len(grid)
        cols: int = len(grid[0])
        memo: Dict[Tuple[int, int], int] = {}

        def move(i: int, j: int) -> int:
            """Recursive function to calculate paths from current position.
            
            Args:
                i: Current row index
                j: Current column index
                
            Returns:
                int: Number of paths from current position to destination
            """
            if i >= rows - 1 and j >= cols - 1:
                return 1
            
            if i >= rows or j >= cols:
                return 0
                
            if grid[i][j] == 1:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            right_paths: int = move(i, j + 1)
            down_paths: int = move(i + 1, j)
            memo[(i, j)] = right_paths + down_paths

            return memo[(i, j)]
        
        return move(0, 0)


def test_unique_paths(grid: List[List[int]], solution: Callable[[], int]) -> None:
    """Test a unique paths solution with given input.
    
    Args:
        grid: 2D list representing the grid with obstacles
        solution: The solution function to test
    """
    result: int = solution()
    print(f"Input grid:")
    for row in grid:
        print(f"    {row}")
    print(f"Number of unique paths: {result}")
    print("-" * 30)


def main() -> None:
    """Main function to demonstrate and test unique paths solutions."""
    test_cases: List[List[List[int]]] = [
        [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]],  # Expected: 2
        
        [[0, 1],
         [0, 0]],     # Expected: 1
        
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],  # Expected: 6
        
        [[1, 0]],     # Expected: 0
    ]
    
    for i, grid in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        solution = RecursionPlusMemoization(grid)
        test_unique_paths(grid, solution)


if __name__ == "__main__":
    main()