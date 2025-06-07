class ProblemStatement:
    """
    You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
    "1" -> 'A'
    "2" -> 'B'
    ...
    "25" -> 'Y'
    "26" -> 'Z'

    However, while decoding the message, you realize that there are many different ways you can decode the 
    message because some codes are contained in other codes ("2" and "5" vs "25").
    For example, "11106" can be decoded into:
    "AAJF" with the grouping (1, 1, 10, 6)
    "KJF" with the grouping (11, 10, 6)
    The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
    Note: there may be strings that are impossible to decode.
    Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.
    The test cases are generated so that the answer fits in a 32-bit integer.

    Example 1:
    Input: s = "12"
    Output: 2

    Explanation:
    "12" could be decoded as "AB" (1 2) or "L" (12).

    Example 2:
    Input: s = "226"
    Output: 3

    Explanation:
    "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

    Example 3:
    Input: s = "06"
    Output: 0

    Explanation:
    "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). 
    In this case, the string is not a valid encoding, so return 0.
    """


class Specifications:
    METHOD_A = """
    BOTTOM UP TABULATION APPROACH

    1. Initial Setup:
       - Create a 1D table of size equal to the input string length
       - Each position i in the table represents the number of ways to decode the string up to index i

    2. Base Cases:
       - If string is empty or starts with '0': return 0 (invalid encoding)
       - If string length is 1: return 1 (single digit is always valid)

    3. Handle Second Position (i=1):
       Case 1: Current digit is '0'
           - Check if previous digit is '1' or '2'
           - If yes: table[1] = 1 (valid combination)
           - If no: return 0 (invalid encoding)

       Case 2: Current digit is not '0'
           - If previous digit is '1': table[1] = 2 (can be decoded as single or double digit)
           - If previous digit is '2':
               - If current digit ≤ 6: table[1] = 2 (can be decoded as single or double digit)
               - If current digit > 6: table[1] = 1 (can only be decoded as single digit)
           - If previous digit is neither '1' nor '2': table[1] = 1 (can only be decoded as single digit)

    4. Fill Remaining Positions (i ≥ 2):
       For each position i:
           Case 1: Current digit is '0'
               - Check if previous digit is '1' or '2'
               - If yes: table[i] = table[i-2] (can only be decoded as part of previous digit)
               - If no: return 0 (invalid encoding)

           Case 2: Current digit is not '0'
               - Set table[i] = table[i-1] (can be decoded as single digit)
               - Check if two-digit number (previous + current) is between 10 and 26
               - If yes: add table[i-2] to table[i] (can also be decoded as double digit)

    5. Return Result:
       - Return the last value in the table (table[-1])
       - This represents the total number of ways to decode the entire string
    """


class EfficiencyHandling:
    METHOD_A = """
    Time Complexity: O(n)
        - We process each character in the string exactly once
        - Each operation at each step is O(1)
        - Where n is the length of the input string

    Space Complexity: O(n)
        - We maintain a 1D table of size n
        - Each cell stores the number of ways to decode up to that position
        - No additional space is needed
    """


class Pseudocode:
    METHOD_A = """
    FUNCTION numDecodings(s: str) -> int:
        # Handle invalid cases
        IF s is empty OR s starts with '0':
            RETURN 0

        # Handle single digit case
        IF length of s is 1:
            RETURN 1

        # Initialize table
        table = array of size length(s) filled with 0
        table[0] = 1  # First position always has 1 way

        # Handle second position
        prev = s[0]
        IF s[1] == "0":
            IF prev == '1' OR prev == '2':
                table[1] = 1
            ELSE:
                RETURN 0
        ELSE:
            IF prev == '1':
                table[1] = 2
            ELSE IF prev == '2':
                IF int(s[1]) <= 6:
                    table[1] = 2
                ELSE:
                    table[1] = 1
            ELSE:
                table[1] = 1

        # Fill the table
        FOR i from 2 to length(s)-1:
            prev = s[i-1]

            IF s[i] == "0":
                IF prev == "1" OR prev == "2":
                    table[i] = table[i-2]
                ELSE:
                    RETURN 0
            ELSE:
                table[i] = table[i-1]
                IF 10 <= int(s[i-1:i+1]) <= 26:
                    table[i] += table[i-2]

        RETURN table[-1]
    """
    