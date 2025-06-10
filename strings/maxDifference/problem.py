class ProblemStatement:
    """Find the maximum difference between character frequencies in a string.
    
    Given a string s consisting of lowercase English letters, find the maximum difference
    diff = a1 - a2 between the frequency of characters a1 and a2 in the string where:
    - a1 has an odd frequency in the string
    - a2 has an even frequency in the string
    
    Examples:
        Input: s = "aaaaabbc"
        Output: 3
        Explanation: 'a' has odd frequency of 5, 'b' has even frequency of 2.
                    Maximum difference is 5 - 2 = 3.

        Input: s = "abcabcab"
        Output: 1
        Explanation: 'a' has odd frequency of 3, 'c' has even frequency of 2.
                    Maximum difference is 3 - 2 = 1.
    """


class Specifications:
    """Solution approach and requirements.
    
    Algorithm Steps:
    1. Handle edge case: return 0 if string is empty
    2. Count frequency of each character using Counter
    3. Initialize tracking variables:
       - max_odd_frequency = negative infinity
       - min_even_frequency = positive infinity
    4. Iterate through frequency counts:
       - For odd frequencies: update max_odd_frequency if current count is larger
       - For even frequencies: update min_even_frequency if current count is smaller
    5. Handle edge cases:
       - If no odd frequencies found, set max_odd_frequency to 0
       - If no even frequencies found, set min_even_frequency to 0
    6. Return the difference: max_odd_frequency - min_even_frequency
    """


class EfficiencyHandling:
    """Efficiency analysis of the solution.
    
    Time Complexity: O(n)
        - Counter creation: O(n) to count all characters
        - Frequency iteration: O(k) where k is number of unique characters
        - Since k ≤ n (at most n unique characters), total is O(n)
    
    Space Complexity: O(k)
        - Counter storage: O(k) where k is number of unique characters
        - Additional variables: O(1) for tracking max/min frequencies
        - Total space complexity is O(k) where k ≤ n
    
    Note: In worst case (all characters unique), k = n, making space complexity O(n)
    """


class Pseudocode:
    """Detailed pseudocode for the maximum difference solution.
    
    FUNCTION compute_diff(s: str) -> int:
        # Handle empty string case
        IF s is empty:
            RETURN 0
        
        # Count character frequencies
        frequencies = Counter(s)
        
        # Initialize tracking variables
        max_odd_frequency = float("-inf")
        min_even_frequency = float("inf")
        
        # Process each character's frequency
        FOR each (char, frequency) in frequencies.items():
            # Check for odd frequency
            IF frequency % 2 == 1:
                max_odd_frequency = max(max_odd_frequency, frequency)
            
            # Check for even frequency
            ELIF frequency % 2 == 0:
                min_even_frequency = min(min_even_frequency, frequency)
        
        # Handle cases where no odd/even frequencies found
        IF max_odd_frequency is float("-inf"):
            max_odd_frequency = 0
        
        IF min_even_frequency is float("inf"):
            min_even_frequency = 0
        
        # Return the maximum difference
        RETURN max_odd_frequency - min_even_frequency
    """
    