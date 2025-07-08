class ProblemStatement:
    """
    You are given an array 'prices' where prices[i] is the price of a given stock on the i-th day.
    Find the maximum profit you can achieve. You may complete as many transactions as you like
    (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    Example 1:
        Input: prices = [1, 2, 3, 0, 2]
        Output: 3
        Explanation: transactions = [buy, sell, cooldown, buy, sell]

    Example 2:
        Input: prices = [1]
        Output: 0
    """

class Specifications:
    """
    Approach: Recursion with memoization (top-down dynamic programming)

    1. At each day, decide whether to buy, sell, or do nothing:
        - If allowed to buy: choose to buy now or skip to a later day.
        - If holding a stock: choose to sell now (and trigger cooldown) or skip to a later day.
    2. Respect the restrictions:
        - After selling, you must cooldown for one day before buying again.
        - No simultaneous transactions: you must sell before buying again.
    3. Use a memoization cache to store the result of each (day, holding) state to avoid redundant calculations.
    4. At each state, cache and return the maximum profit achievable from that point onward.
    """

class EfficiencyHandling:
    """
    Time Complexity:
        - O(N), where N is the number of days. Each state (day, holding) is computed at most once due to memoization.
    Space Complexity:
        - O(N), for the memoization cache and recursion stack.
    """

class Pseudocode:
    """
    FUNCTION maxProfit(prices):
        IF len(prices) < 1:
            RETURN 0

        memo = {}

        FUNCTION helper(idx, can_buy):
            IF idx >= LENGTH(prices):
                RETURN 0

            IF (idx, can_buy) IN memo:
                RETURN memo[(idx, can_buy)]

            IF can_buy:
                buy_now = -prices[idx] + helper(idx + 1, False)
                skip = helper(idx + 1, True)
                memo[(idx, can_buy)] = MAX(buy_now, skip)
            ELSE:
                sell_now = prices[idx] + helper(idx + 2, True)  # cooldown after selling
                skip = helper(idx + 1, False)
                memo[(idx, can_buy)] = MAX(sell_now, skip)

            RETURN memo[(idx, can_buy)]

        RETURN helper(0, True)
    """

