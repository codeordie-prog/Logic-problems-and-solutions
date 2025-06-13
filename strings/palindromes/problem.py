class ProblemStatement:
    """Given an integer x, return true if x is a palindrome, and false otherwise.
    
    A palindrome number reads the same backward as forward.
    
    Examples:
        Input: x = 121
        Output: true
        Explanation: 121 reads as 121 from left to right and from right to left.
       
        Input: x = -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
        Therefore it is not a palindrome.
        
        Input: x = 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    """


class Specifications:
    """Solution approaches and implementation details.
    
    Approach 1: String Comparison
    ----------------
    1. Convert the integer to a string
    2. Create a reversed copy of the string
    3. Compare the original and reversed strings
    4. Return true if they match, false otherwise
    
    Approach 2: Integer Reversal
    ----------------
    1. Handle edge cases:
       - Negative numbers are not palindromes
       - Zero is a palindrome
    2. Initialize a variable to store the reversed number
    3. While the original number is greater than 0:
       - Extract the last digit using modulo 10
       - Build the reversed number by multiplying current reversed by 10 and adding the digit
       - Remove the last digit from the original number using integer division
    4. Compare the reversed number with the original
    """


class EfficiencyHandling:
    """Detailed analysis of time and space complexity.
    
    Approach 1 - String Comparison:
    Time Complexity: O(n)
        - Converting integer to string: O(n)
        - String reversal: O(n)
        - String comparison: O(n)
        where n is the number of digits in the input number
    
    Space Complexity: O(n)
        - Additional space needed for string conversion and storage
    
    Approach 2 - Integer Reversal:
    Time Complexity: O(log n)
        - We process each digit of the number once
        - Number of digits in a number n is log₁₀(n)
    
    Space Complexity: O(1)
        - Constant extra space regardless of input size
    """


class Pseudocode:
    """Detailed implementation steps for the solution.
    
    Approach 1 - String Comparison
    -----------------------------
    FUNCTION is_palindrome(x: int) -> bool:
        # Convert to string and compare with its reverse
        x_str = str(x)
        x_reversed = x_str[::-1]
        RETURN x_reversed == x_str


    Approach 2 - Integer Reversal
    -----------------------------
    FUNCTION is_palindrome(x: int) -> bool:
        # Handle edge cases
        IF x < 0:
            RETURN False
        IF x == 0:
            RETURN True

        # Initialize variables
        original = x
        reversed_num = 0

        # Reverse the number
        WHILE original > 0:
            digit = original % 10
            reversed_num = (reversed_num * 10) + digit
            original = original // 10

        # Compare original and reversed numbers
        RETURN reversed_num == x
    """
    