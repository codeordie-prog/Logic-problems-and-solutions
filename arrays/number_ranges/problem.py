class ProblemStatement:
    """
    You are given a sorted unique integer array nums.
    A range [a,b] is the set of all integers from a to b (inclusive).
    Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
    That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

    Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b
    
    Example 1:
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: The ranges are:
    [0,2] --> "0->2"
    [4,5] --> "4->5"
    [7,7] --> "7"

    Example 2:
    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: The ranges are:
    [0,0] --> "0"
    [2,4] --> "2->4"
    [6,6] --> "6"
    [8,9] --> "8->9"
    
    """


class Specifications:
    METHOD_A = f"""
    1. Case array is empty - Return []
    2. Case length of array is 1 - Return [str(nums[0])]
    3. Initialize start pointer to 0 and empty output list
    4. Define res = [0,1] for checking consecutive numbers
    5. Iterate with pointer j from 1 to length of array - 1:
       - If abs(nums[j] - nums[j-1]) is in res (0 or 1): Continue
       - Else:
         * If start != j-1: Append "nums[start]->nums[j-1]"
         * If start == j-1: Append "nums[start]"
         * Update start = j
    6. After loop, handle remaining cases:
       - If start == j: Append "nums[start]"
       - If start == 0: Append "nums[0]->nums[-1]"
       - Else: Append "nums[start]->nums[j]"
    7. Return output list
    """

    


class EfficiencyHandling:
    METHOD_A = """
    Time complexity:
    - Single pass through array: O(n)
    - String operations and comparisons: O(1)
    - Overall time complexity: O(n)

    Space complexity:
    - Output list: O(n) in worst case
    - Constant extra space for variables
    - Overall space complexity: O(n)
    """

    

class Pseudocode:
    METHOD_A = """
    FUNCTION summaryRanges(nums):
        # Handle empty array
        IF nums is empty:
            RETURN []
            
        # Handle single element array
        IF length of nums is 1:
            RETURN [str(nums[0])]
            
        # Initialize variables
        start = 0
        output = []
        res = [0,1]
        
        # Process array
        FOR j from 1 to length(nums)-1:
            IF abs(nums[j] - nums[j-1]) is in res:
                CONTINUE
            ELSE:
                IF start != j-1:
                    output.append(str(nums[start]) + "->" + str(nums[j-1]))
                ELSE:
                    output.append(str(nums[start]))
                start = j
                
        # Handle remaining cases
        IF start == j:
            output.append(str(nums[start]))
        ELIF start == 0:
            output.append(str(nums[0]) + "->" + str(nums[-1]))
        ELSE:
            output.append(str(nums[start]) + "->" + str(nums[j]))
            
        RETURN output
    """

    
    