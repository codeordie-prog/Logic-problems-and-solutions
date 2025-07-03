class ProblemStatement:
    """
    Teemo is attacking an enemy, Ashe, with poison attacks! When Teemo attacks, Ashe is poisoned for exactly 'duration' seconds. More formally, an attack at second t means Ashe is poisoned during the inclusive interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer resets, and the poison effect will end 'duration' seconds after the new attack.

    You are given a non-decreasing integer array 'timeSeries', where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer 'duration'.
    Return the total number of seconds that Ashe is poisoned.

    Example 1:
        Input: timeSeries = [1, 4], duration = 2
        Output: 4
        Explanation: Teemo's attacks on Ashe occur as follows:
            - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
            - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
        Ashe is poisoned for seconds 1, 2, 4, and 5, totaling 4 seconds.

    Example 2:
        Input: timeSeries = [1, 2], duration = 2
        Output: 3
        Explanation: Teemo's attacks on Ashe occur as follows:
            - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
            - At second 2, Teemo attacks again, resetting the poison timer. Ashe is poisoned for seconds 2 and 3.
        Ashe is poisoned for seconds 1, 2, and 3, totaling 3 seconds.
    """

class Specifications:
    """
    1. Initialize a variable to keep track of the total poisoned duration (poison_duration = 0).
    2. Iterate through the timeSeries array, except for the last element.
    3. For each attack, calculate the time when the poison would clear (current attack time + duration).
    4. Compare the next attack time with the poison clear time:
        a. If the next attack occurs before the poison clears, add the difference between the next and current attack times to poison_duration.
        b. Otherwise, add the full duration to poison_duration.
    5. After the loop, add the duration for the last attack (since it always contributes its full duration).
    6. Return the total poison_duration.
    """

class EfficiencyHandling:
    """
    Time Complexity:
        - O(N), where N is the length of the timeSeries array. Each attack is processed once.
    Space Complexity:
        - O(1), as only a constant amount of extra space is used regardless of input size.
    """

class Pseudocode:
    """
    FUNCTION find_poison_duration(time_series, duration):
        poison_duration = 0
        FOR i FROM 0 TO LENGTH(time_series) - 1:
            current_attack = time_series[i]
            next_attack = time_series[i + 1]
            poison_clear_time = current_attack + duration
            IF next_attack < poison_clear_time:
                poison_duration += next_attack - current_attack
            ELSE:
                poison_duration += duration
        poison_duration += duration  # Add duration for the last attack
        RETURN poison_duration
    """