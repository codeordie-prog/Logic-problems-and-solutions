from typing import Any, List, Dict, Tuple


class Solution:
    """
    Solution class to find the largest divisible subset in a list of distinct positive integers.
    """
    def __init__(self, nums: List[int]) -> None:
        """
        Initializes the Solution with the given list of numbers and computes the largest subset.
        Args:
            nums (List[int]): List of distinct positive integers.
        """
        self.result: List[int] = self.largest_subset(nums)

    def __call__(self, *args: Any, **kwds: Any) -> List[int]:
        """
        Returns the computed largest divisible subset.
        Returns:
            List[int]: The largest divisible subset found.
        """
        return self.result
    
    def largest_subset(self, nums: List[int]) -> List[int]:
        """
        Finds the largest subset such that for every pair (a, b) in the subset,
        either a % b == 0 or b % a == 0.
        Args:
            nums (List[int]): List of distinct positive integers.
        Returns:
            List[int]: The largest divisible subset found.
        """
        nums.sort()

        memo: Dict[Tuple[int, int], List[int]] = {}

        def helper(start: int, idx: int) -> List[int]:
            if (start, idx) in memo:
                return memo[(start, idx)]
            
            subset: List[int] = []
            for i in range(idx, len(nums)):
                if nums[i] % start == 0:
                    candidate: List[int] = helper(nums[i], i + 1)
                    if len(candidate) > len(subset):
                        subset = candidate

            memo[(start, idx)] = [start] + subset
            return memo[(start, idx)]

        max_subset: List[int] = []
        for i in range(len(nums)):
            candidate: List[int] = helper(nums[i], i + 1)
            if len(candidate) > len(max_subset):
                max_subset = candidate

        return max_subset


def main() -> None:
    """
    Main function to run test cases for the Solution class.
    """
    test_cases: List[List[int]] = [
        [1, 2, 3, 27, 9],
        [1, 2, 3],
        [1, 2, 4, 8],
        [2, 3, 5, 7, 11],  # No divisible pairs except single elements
        [1, 16, 8, 4, 2],  # All powers of 2
        [5, 10, 20, 25, 50],  # Multiple valid chains
    ]

    for idx, nums in enumerate(test_cases):
        result: List[int] = Solution(nums)()
        print(f"Test case {idx + 1}: Input: {nums}\n  Output: {result}\n")

if __name__ == "__main__":
    main()