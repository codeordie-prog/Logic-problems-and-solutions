

from typing import Any, List


class Solution:
    """
    Solution class to compute the count of all numbers with unique digits for a given n.
    When called, returns the result for the initialized n.
    """
    def __init__(self, n: int) -> None:
        """
        Initialize the Solution with the given n and compute the result.
        :param n: The number of digits to consider (0 <= n <= 10)
        """
        self.result: int = self.count_unique_numbers(n)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """
        Return the computed result when the instance is called.
        :return: The count of numbers with unique digits for the given n
        """
        return self.result
    
    def count_unique_numbers(self, n: int) -> int:
        """
        Count all numbers with unique digits where 0 <= x < 10^n.
        :param n: The number of digits
        :return: The count of numbers with unique digits
        """
        if n == 0:
            return 1
        
        count: int = 10
        remaining_options: int = 9
        current: int = 9

        for _ in range(2, n + 1):
            current *= remaining_options
            count += current
            remaining_options -= 1

        return count
    

def main() -> None:
    """
    Test the Solution class with a set of test cases and print the results.
    """
    test_cases: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    for n in test_cases:
        result: int = Solution(n)()
        print(result)


if __name__ == "__main__":
    main()