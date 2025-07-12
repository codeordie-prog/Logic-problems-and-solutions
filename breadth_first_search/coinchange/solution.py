from typing import Any, List, Dict, Optional

class Recursion:
    """
    Solves the coin change problem using recursion with memoization.
    Given a list of coin denominations and a target amount, returns the minimum number of coins needed to make up that amount.
    If it is not possible, returns -1.
    """
    def __init__(self, coins: List[int], amount: int) -> None:
        """
        Initializes the Recursion class and computes the result.
        :param coins: List of coin denominations.
        :param amount: Target amount to make up.
        """
        self.result = self.coin_change(coins, amount)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        Returns the computed result when the instance is called.
        """
        return self.result
    
    def coin_change(self, coins: List[int], amount: int) -> int:
        """
        Computes the minimum number of coins needed to make up the given amount using recursion and memoization.
        :param coins: List of coin denominations.
        :param amount: Target amount to make up.
        :return: Minimum number of coins needed, or -1 if not possible.
        """
        if amount == 0:
            return 0
        
        min_value: int = min(coins)
        memo: Dict[int, Optional[int]] = {}

        def helper(remainder: int) -> int:
            """
            Helper function for recursion and memoization.
            :param remainder: Remaining amount to make up.
            :return: Minimum number of coins needed for the remainder.
            """
            if remainder == 0:
                return 0
            
            if remainder in memo:
                return memo[remainder]
            
            if remainder < min_value:
                return float('inf')
            
            min_count: float = float('inf')
            for value in coins:
                rem: int = remainder - value
                count = 1 + helper(rem)
                min_count = min(min_count, count)
            memo[remainder] = min_count
            return min_count

        min_count: float = helper(amount)
        if min_count == float('inf'):
            return -1
        return int(min_count)
    
def main() -> None:
    """
    Runs multiple test cases for the Recursion solution and prints the results.
    """
    test_cases = [
        ([186, 419, 83, 408], 6249),
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0),
        ([1, 3, 4], 6),
        ([2, 5, 10, 1], 27),
        ([2], 1),
        ([1, 2, 5], 100),
    ]

    for coins, amount in test_cases:
        res = Recursion(coins, amount)()
        print(f"Coins: {coins}, Amount: {amount} => Min coins: {res}")

if __name__ == "__main__":
    main()