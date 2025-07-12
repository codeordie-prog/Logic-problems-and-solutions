from typing import Any, Dict, DefaultDict, List, Optional
from collections import defaultdict


class SolutionA:
    """
    Finds the maximum sum of two numbers in the list whose digits sum to the same value (using a grouping and sorting approach).
    """
    def __init__(self, nums: List[int]) -> None:
        self.result: int = self.max_sum(nums)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        return self.result
    
    def max_sum(self, nums: List[int]) -> int:
        """
        Groups numbers by their digit sum, sorts each group, and finds the maximum sum of any two numbers in the same group.
        """
        store: DefaultDict[int, List[int]] = defaultdict(list)
        max_sum: int = -1

        def get_sum(num: int) -> int:
            total: int = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total
        
        for num in nums:
            total: int = get_sum(num)
            store[total].append(num)

        for val in store.values():
            if len(val) > 1:
                val.sort(reverse=True)
                max_sum = max(max_sum, val[0] + val[1])

        return max_sum
    

class SolutionB:
    """
    Optimized solution that tracks only the largest number for each digit sum, yielding O(N) time and O(1) space.
    """
    def __init__(self, nums: List[int]) -> None:
        self.result: int = self.max_sum(nums)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        return self.result
    
    def max_sum(self, nums: List[int]) -> int:
        """
        Tracks the largest number for each digit sum and computes the maximum sum of any two numbers with the same digit sum.
        """
        store: Dict[int, int] = {}
        max_sum: int = -1

        def get_sum(num: int) -> int:
            total: int = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total
        
        for num in nums:
            total: int = get_sum(num)
            if total in store:
                max_sum = max(max_sum, num + store[total])
                store[total] = max(num, store[total])
            else:
                store[total] = num

        return max_sum
    

class SolutionC:
    """
    Finds the maximum sum by grouping numbers and then finding the two largest in each group without sorting.
    """
    def __init__(self, nums: List[int]) -> None:
        self.result: int = self.max_sum(nums)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        return self.result

    def max_sum(self, nums: List[int]) -> int:
        """
        Groups numbers by digit sum and finds the two largest in each group to compute the max sum.
        """
        store: DefaultDict[int, List[int]] = defaultdict(list)
        max_sum: int = -1

        def get_sum(num: int) -> int:
            total: int = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total
        
        for num in nums:
            total: int = get_sum(num)
            store[total].append(num)

        for group in store.values():
            if len(group) > 1:
                largest = -1
                second_largest = -1
                for num in group:
                    if num > largest:
                        second_largest = largest
                        largest = num
                    elif num > second_largest:
                        second_largest = num
                
                if second_largest != -1:
                    max_sum = max(max_sum, largest + second_largest)

        return max_sum


def main() -> None:
    """
    Runs multiple test cases for all solutions and checks for consistency.
    """
    test_cases: List[List[int]] = [
        [368, 369, 307, 304, 384, 138, 90, 279, 35, 396, 114, 328, 251, 364, 300, 191, 438, 467, 183],
        [18, 43, 36, 13, 7],
        [10, 12, 19, 14],
        [99, 81, 27, 72, 18],
        [123, 321, 213, 132, 231, 312]
    ]

    for nums in test_cases:
        solution_a: int = SolutionA(nums)()
        solution_b: int = SolutionB(nums)()
        solution_c: int = SolutionC(nums)()
        assert solution_a == solution_b == solution_c, f"Mismatch: A={solution_a}, B={solution_b}, C={solution_c} for input {nums}"
        print(f"Input: {nums}\nMax sum: {solution_a}\n")


if __name__ == "__main__":
    main()
