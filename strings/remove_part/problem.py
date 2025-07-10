
class ProblemStatement:
    """
    Given two strings s and part, perform the following operation on s until all occurrences of the substring part are
    removed:
    Find the leftmost occurrence of the substring part and remove it from s.
    Return s after removing all occurrences of part.
    A substring is a contiguous sequence of characters in a string.

    Example 1:
    Input: s = "daabcbaabcbc", part = "abc"
    Output: "dab"
    Explanation: The following operations are done:
    - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
    - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
    - s = "dababc", remove "abc" starting at index 3, so s = "dab".
    Now s has no occurrences of "abc".

    Example 2:
    Input: s = "axxxxyyyyb", part = "xy"
    Output: "ab"
    Explanation: The following operations are done:
    - s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
    - s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
    - s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
    - s = "axyb", remove "xy" starting at index 1 so s = "ab".
    Now s has no occurrences of "xy".
    
    """

class Specifications:
    """
    Specifications for solving the problem:

    1. Recursion Approach:
        - Start with index = 0.
        - Scan the string to check if the substring from index to index + len(part) matches 'part'.
        - If a match is found, remove that segment from the string, reset index to 0, and repeat the process.
        - If the segment does not match, increment the index by 1 and continue scanning.
        - The process terminates when the index exceeds the length of the current string or when 'part' is no longer found in the string.

    2. Iterative (Loop) Approach:
        - Iterate through each character in the string, appending it to a result list.
        - After each append, check if the last len(part) characters in the result list form the substring 'part'.
        - If so, remove those characters from the result list.
        - After processing all characters, join the result list into a string and return it.
    """

class EfficiencyHandling:
    """
    Efficiency Analysis:

    1. Recursion Approach:
        - Time Complexity: O(N * M), where N is the length of the string and M is the number of times 'part' occurs. The index is reset to 0 after each removal, potentially leading to repeated scans.
        - Space Complexity: O(N), due to the recursion stack and string slicing.

    2. Iterative (Loop) Approach:
        - Time Complexity: O(N), where N is the length of the string. Each character is processed once, and substring checks are efficient.
        - Space Complexity: O(N), for storing the result list.
    """

class Pseudocode:
    """
    Recursion Approach:

        FUNCTION remove_with_recursion(s, part):
            FUNCTION helper(idx, curr):
                IF idx >= LENGTH(curr):
                    RETURN curr
                IF part NOT IN curr:
                    RETURN curr
                segment = curr[idx : idx + LENGTH(part)]
                IF segment == part:
                    curr = curr[:idx] + curr[idx + LENGTH(part):]
                    idx = 0
                    RETURN helper(idx, curr)
                RETURN helper(idx + 1, curr)
            RETURN helper(0, s)

    Iterative (Loop) Approach:

        FUNCTION remove_with_loop(s, part):
            result = []
            plen = LENGTH(part)
            FOR char IN s:
                result.APPEND(char)
                IF LENGTH(result) >= plen AND JOIN(result[-plen:]) == part:
                    DELETE result[-plen:]
            RETURN JOIN(result)
    """