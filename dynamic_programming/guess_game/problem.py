
class ProblemStatement:
    """
    We are playing the Guessing Game. The game works as follows:
    I pick a number between 1 and n.
    You guess a number.
    If you guess the right number, you win the game.
    If you guess the wrong number, I will tell you whether the number I picked is higher or lower,
    and you will continue guessing.
    Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
    Given a particular n, return the minimum amount of money you need to guarantee a win regardless of
    what number I pick.
    """


class Specifications:
    """
    1. The task is to find the minimum amount of money required to guarantee a win, regardless of the correct guess.
    2. In other words, we need to minimize the maximum cost incurred in the worst-case scenario.
    3. Simulate guesses within a given range [start, stop].
    4. The range changes dynamically based on whether the guess was too high or too low.
    5. The worst-case scenario represents the path to the correct guess that leads to the highest cost.
    6. The total minimum amount is the minimum among all possible worst-case costs for each guess.
    7. Return this minimum total cost.
    """


class EfficiencyHandling:
    """
    Time Complexity:
        - O(N^3) in the naive recursive solution.
        - With memoization (DP), it can be reduced to O(N^2).

    Space Complexity:
        - O(N^2) for the memoization table.
        - O(N) for the recursion stack.
    """


class Pseudocode:
    """
    FUNCTION get_money_amount(n):
        INITIALIZE cache = {}

        FUNCTION guess(start, stop):
            IF start >= stop:
                RETURN 0

            IF (start, stop) IN cache:
                RETURN cache[(start, stop)]

            min_cost = INFINITY
            FOR each g IN RANGE(start, stop + 1):
                left_cost = guess(start, g - 1)
                right_cost = guess(g + 1, stop)
                worst_case = g + MAX(left_cost, right_cost)
                min_cost = MIN(min_cost, worst_case)

            cache[(start, stop)] = min_cost
            RETURN min_cost

        RETURN guess(1, n)
    """