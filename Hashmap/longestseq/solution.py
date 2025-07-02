from typing import Any, List, Dict, Set

class Memoization:
    """
    Finds the length of the longest consecutive elements sequence in an unsorted list of integers.
    Uses memoization to cache results for efficiency.
    """
    def __init__(self, nums: List[int]) -> None:
        """
        Initialize the Memoization class and compute the longest consecutive sequence.

        Args:
            nums (List[int]): The list of integers to process.
        """
        self.result: int = self.longest_sequence(nums)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """
        Return the result of the longest consecutive sequence computation.

        Returns:
            int: The length of the longest consecutive sequence.
        """
        return self.result

    def longest_sequence(self, nums: List[int]) -> int:
        """
        Compute the length of the longest consecutive elements sequence.

        Args:
            nums (List[int]): The list of integers to process.

        Returns:
            int: The length of the longest consecutive sequence.
        """
        if not nums:
            return 0
        numbers_set: Set[int] = set(nums)
        memo: Dict[int, int] = dict()

        def count(num: int) -> int:
            if num not in numbers_set:
                return 0
            if num in memo:
                return memo[num]
            result: int = 1 + count(num + 1)
            memo[num] = result
            return result

        max_length: int = float("-inf")
        for num in numbers_set:
            max_length = max(max_length, count(num))
        return max_length


def main() -> None:
    """
    Runs several test cases to verify the Memoization class for longest consecutive sequence.
    """
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
        ([10, 5, 12, 3, 55, 30, 4, 11, 2], 4),
        ([], 0),
        ([1], 1),
    ]
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = Memoization(nums)
        output = result()
        print(f"Test case {i}: nums={nums} => {output} (expected: {expected})")
        assert output == expected, f"Test case {i} failed!"
    print("All test cases passed.")


if __name__ == "__main__":
    main()