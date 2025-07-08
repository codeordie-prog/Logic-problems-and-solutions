from typing import Any, Dict, List, Tuple

class RecursionPlusMemoization:
    """
    Implements the stock buy-sell with cooldown problem using recursion with memoization (top-down DP).
    Computes the maximum profit that can be achieved given the price list and cooldown restriction.
    """
    def __init__(self, prices: List[int]) -> None:
        """
        Initialize the solution and compute the result.
        Args:
            prices (List[int]): List of stock prices by day.
        """
        self.result: int = self.max_profit(prices)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """
        Callable interface to return the computed result.
        Returns:
            int: Maximum profit achievable.
        """
        return self.result
    
    def max_profit(self, prices: List[int]) -> int:
        """
        Compute the maximum profit with cooldown using recursion and memoization.
        Args:
            prices (List[int]): List of stock prices by day.
        Returns:
            int: Maximum profit achievable.
        """
        if len(prices) <= 1:
            return 0
        
        memo: Dict[Tuple[int, bool], int] = {}

        def helper(idx: int, buy: bool) -> int:
            """
            Recursive helper function to compute max profit from a given day and state.
            Args:
                idx (int): Current day index.
                buy (bool): True if allowed to buy, False if holding a stock.
            Returns:
                int: Maximum profit from this state.
            """
            if idx >= len(prices):
                return 0
            
            if (idx, buy) in memo:
                return memo[(idx, buy)]
            
            if buy:
                buy_now: int = -prices[idx] + helper(idx + 1, False)
                skip: int = helper(idx + 1, True)
                memo[(idx, buy)] = max(buy_now, skip)
            else:
                sell_now: int = prices[idx] + helper(idx + 2, True)
                skip: int = helper(idx + 1, False)
                memo[(idx, buy)] = max(sell_now, skip)
            return memo[(idx, buy)]

        return helper(0, True)
    
def main() -> None:
    """
    Run a set of test cases to validate the RecursionPlusMemoization solution.
    """
    test_cases: List[Dict[str, Any]] = [
        {"prices": [2, 1, 4], "expected": 3},
        {"prices": [1, 2, 3, 0, 2], "expected": 3},
        {"prices": [1], "expected": 0},
        {"prices": [1, 2, 4, 2, 5, 7, 2, 4, 9, 0], "expected": 13},
        {"prices": [6, 1, 3, 2, 4, 7], "expected": 6},
    ]
    for idx, case in enumerate(test_cases, 1):
        result: RecursionPlusMemoization = RecursionPlusMemoization(case["prices"])
        res: int = result()
        print(f"Test case {idx}: prices={case['prices']} -> Result: {res} (Expected: {case['expected']}){' [PASS]' if res == case['expected'] else ' [FAIL]'}")

if __name__ == "__main__":
    main()
    