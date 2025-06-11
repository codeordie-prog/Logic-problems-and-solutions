from typing import Any, Dict, List


class RecursionPlusMemoization:
    """Solution for the Jump Game problem using recursion with memoization.
    
    This approach uses a recursive strategy with memoization to determine if it's possible
    to reach the last index of the array. The solution caches intermediate results to
    avoid redundant calculations.
    """

    def __init__(self, nums: List[int]) -> None:
        """Initialize the solution with input array.
        
        Args:
            nums: List of integers representing maximum jump lengths at each position
        """
        self.result: bool = self.jump_game(nums)

    def __call__(self, *args: Any, **kwds: Any) -> bool:
        """Return the result when the class instance is called.
        
        Returns:
            bool: True if last index is reachable, False otherwise
        """
        return self.result
    
    def jump_game(self, nums: List[int]) -> bool:
        """Determine if the last index is reachable using the given jump lengths.
        
        Args:
            nums: List of integers representing maximum jump lengths at each position
            
        Returns:
            bool: True if last index is reachable, False otherwise
        """
        if len(nums) == 1:
            return True
        if not nums or nums[0] == 0:
            return False
        
        memo: Dict[int, bool] = {}
        
        def jump(idx: int) -> bool:
            """Helper function to check if last index is reachable from current position.
            
            Args:
                idx: Current position in the array
                
            Returns:
                bool: True if last index is reachable from current position
            """
            if idx + nums[idx] >= len(nums):
                return True
            if nums[idx] == 0:
                return False
            
            if idx in memo:
                return memo[idx]
            
            current_jump = idx + nums[idx]
            while current_jump > idx:
                if jump(current_jump):
                    memo[idx] = True
                    return True
                
                current_jump -= 1

            memo[idx] = False
            return False
        
        return jump(0)


def main() -> None:
    """Main function to demonstrate the solution with example cases."""
    # Test cases with different scenarios
    test_cases: Dict[str, List[int]] = {
        "Simple case": [2, 3, 1, 1, 4],
        "Impossible case": [3, 2, 1, 0, 4],
        "Single element": [0],
        "Complex case": [
            2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2,
            1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2,
            0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 
            8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2,
            2, 7, 5, 1, 7, 9, 6
        ]
    }
    
    # Run all test cases
    for case_name, nums in test_cases.items():
        result: RecursionPlusMemoization = RecursionPlusMemoization(nums)
        print(f"\nTest Case: {case_name}")
        print(f"Input array: {nums}")
        print(f"Can reach last index: {result()}")
        print("-" * 80)


if __name__ == "__main__":
    main()
