from typing import Any, List, Dict

class RecursionPlusMemoization:
    """
    A solution class that uses recursion with memoization to solve the house robber problem.
    This approach avoids redundant calculations by caching results for each house index.
    """
    
    def __init__(self, nums: List[int]) -> None:
        """
        Initialize the solution with the given array of house values.
        
        Args:
            nums (List[int]): Array representing money in each house.
        """
        self.result: int = self.rob(nums)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """
        Callable interface to return the computed result.
        
        Returns:
            int: Maximum amount of money that can be robbed.
        """
        return self.result
    
    def rob(self, nums: List[int]) -> int:
        """
        Calculate the maximum amount of money that can be robbed without alerting the police.
        
        Args:
            nums (List[int]): Array representing money in each house.
            
        Returns:
            int: Maximum amount of money that can be robbed.
        """
        memo: Dict[int, int] = {}

        def helper(idx: int) -> int:
            """
            Recursive helper function with memoization.
            
            Args:
                idx (int): Current house index to consider.
                
            Returns:
                int: Maximum money that can be robbed starting from this index.
            """
            if idx >= len(nums):
                return 0
            
            if idx in memo:
                return memo[idx]
            
            rob_current: int = nums[idx] + helper(idx + 2)
            skip_current: int = helper(idx + 1)

            result: int = max(rob_current, skip_current)
            memo[idx] = result
            return memo[idx]
        
        return helper(0)
    

def main() -> None:
    """
    Main function to test the house robber solution with multiple test cases.
    """
    test_cases: List[Dict[str, Any]] = [
        {"nums": [2, 3, 7, 9, 6], "expected": 15},
        {"nums": [1, 2, 3, 1], "expected": 4},
        {"nums": [2, 7, 9, 3, 1], "expected": 12},
        # Additional test cases
        {"nums": [1, 3, 1], "expected": 3},
        {"nums": [2, 1, 1, 2], "expected": 4},
        {"nums": [1], "expected": 1},
    ]
    
    for idx, case in enumerate(test_cases, 1):
        result: RecursionPlusMemoization = RecursionPlusMemoization(case["nums"])
        res: int = result()
        print(f"Test case {idx}: nums={case['nums']} -> Result: {res} (Expected: {case['expected']}){' [PASS]' if res == case['expected'] else ' [FAIL]'}")

if __name__ == "__main__":
    main()