from typing import Any, List

class Solution:
    """
    Computes the total number of seconds Ashe is poisoned given the timeseries of attacks and poison duration.
    """
    def __init__(self, timeSeries: List[int], duration: int) -> None:
        self.result: int = self.find_poisoned_duration(timeSeries, duration)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        return self.result

    def find_poisoned_duration(self, time_series: List[int], duration: int) -> int:
        """
        Calculates the total poisoned duration.

        Args:
            time_series (List[int]): List of attack times (non-decreasing order).
            duration (int): Duration of poison effect per attack.

        Returns:
            int: Total seconds Ashe is poisoned.
        """
        poison_duration: int = 0
        n: int = len(time_series)
        for i in range(n - 1):
            current_attack: int = time_series[i]
            next_attack: int = time_series[i + 1]
            poison_clear_time: int = current_attack + duration
            if next_attack < poison_clear_time:
                poison_duration += next_attack - current_attack
            else:
                poison_duration += duration
        if n > 0:
            poison_duration += duration  # Add duration for the last attack
        return poison_duration


def main() -> None:
    test_cases: List[dict[str, Any]] = [
        {"timeSeries": [1, 2], "duration": 2, "expected": 3},
        {"timeSeries": [1, 4], "duration": 2, "expected": 4},
        # Additional test cases
        {"timeSeries": [1, 2, 3, 4, 5], "duration": 5, "expected": 9},
        {"timeSeries": [1, 10, 20], "duration": 2, "expected": 6},
        {"timeSeries": [1], "duration": 10, "expected": 10},
    ]
    for idx, case in enumerate(test_cases, 1):
        solution = Solution(case["timeSeries"], case["duration"])
        res: int = solution()
        print(f"Test case {idx}: timeSeries={case['timeSeries']}, duration={case['duration']} -> Result: {res} (Expected: {case['expected']}){' [PASS]' if res == case['expected'] else ' [FAIL]'}")

if __name__ == "__main__":
    main()