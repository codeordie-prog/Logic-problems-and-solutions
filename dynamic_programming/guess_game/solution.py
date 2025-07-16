from typing import Any, Dict, Tuple, Optional

class Solution:
    """
    Solution class to determine the minimum amount of money required to guarantee a win
    in the Guessing Game for a given n.
    """
    def __init__(self, n: int) -> None:
        """
        Initializes the Solution with the given n and computes the result.
        Args:
            n (int): The upper bound of the guessing range (1 to n).
        """
        self.result: int = self.get_amount_of_money(n)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """
        Returns the computed minimum amount of money required to guarantee a win.
        Returns:
            int: The minimum guaranteed cost.
        """
        return self.result
    
    def get_amount_of_money(self, n: int) -> int:
        """
        Computes the minimum amount of money required to guarantee a win for numbers 1 to n.
        Args:
            n (int): The upper bound of the guessing range.
        Returns:
            int: The minimum guaranteed cost.
        """
        memo: Dict[Tuple[int, int], int] = {}

        def guess(start: int, stop: int) -> int:
            if start >= stop:
                return 0
            if (start, stop) in memo:
                return memo[(start, stop)]
            min_cost: float = float("inf")
            for i in range(start, stop + 1):
                left_cost: int = guess(start, i - 1)
                right_cost: int = guess(i + 1, stop)
                worst_case_cost: int = i + max(left_cost, right_cost)
                min_cost = min(min_cost, worst_case_cost)
            memo[(start, stop)] = int(min_cost)
            return int(min_cost)
        return guess(1, n)


def main() -> None:
    """
    Main function to run test cases for the Solution class.
    """
    test_cases: list[int] = [10, 1, 5, 15]
    for idx, n in enumerate(test_cases):
        result: int = Solution(n)()
        print(f"Test case {idx + 1}: n = {n}\n  Output: {result}\n")

if __name__ == "__main__":
    main()
    