class ProblemStatement:
    """Determine if you can reach the last index of an array using jumps.
    
    You are given an integer array nums. You are initially positioned at the array's first index,
    and each element in the array represents your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.

    Examples:
        Input: nums = [2, 3, 1, 1, 4]
        Output: true
        Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

        Input: nums = [3, 2, 1, 0, 4]
        Output: false
        Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
        which makes it impossible to reach the last index.
    """


class Specifications:
    """Solution approach and implementation details.
    
    Approach: Recursion with Memoization
    
    Steps:
    1. Handle edge cases:
       - If nums is None or empty: return False
       - If nums has only one element: return True
       - If first element is 0: return False (can't move)

    2. Initialize memoization dictionary to cache results

    3. For each position:
       - Try all possible jumps from current position
       - Start with maximum jump length
       - If maximum jump doesn't work, try decreasing lengths
       - Cache results to avoid redundant calculations

    4. Base cases:
       - If current position + jump length >= array length: return True
       - If current position has jump length 0: return False
       - If position is already in memo: return cached result
    """


class EfficiencyHandling:
    """Detailed analysis of time and space complexity.
    
    Time Complexity: O(n²)
        - In worst case, we need to check all possible jumps from each position
        - For each position i, we might need to check up to nums[i] positions
        - With memoization, we avoid recalculating the same positions
        - However, in worst case (e.g., [n, n-1, n-2, ..., 1]), we still need O(n²) time
    
    Space Complexity: O(n)
        - Memoization dictionary stores at most n positions
        - Recursion stack depth is at most n
        - Total space complexity is O(n)
    
    Note: This is a significant improvement over the basic recursive approach
    which would have exponential time complexity.
    """


class Pseudocode:
    """Detailed implementation steps for the solution.
    
    FUNCTION can_jump(nums: List[int]) -> bool:
        # Handle edge cases
        IF nums is None OR len(nums) == 0:
            RETURN False
        IF len(nums) == 1:
            RETURN True
        IF nums[0] == 0:
            RETURN False
        
        # Initialize memoization
        memo = {}
        
        FUNCTION jump_from_position(idx: int) -> bool:
            # Base cases
            IF idx + nums[idx] >= len(nums):
                RETURN True
            IF nums[idx] == 0:
                RETURN False
            IF idx in memo:
                RETURN memo[idx]
            
            # Try all possible jumps from current position
            current_jump = idx + nums[idx]
            WHILE current_jump > idx:
                IF jump_from_position(current_jump):
                    memo[idx] = True
                    RETURN True
                current_jump -= 1
            
            # If no valid jump found
            memo[idx] = False
            RETURN False
        
        # Start from first position
        RETURN jump_from_position(0)
    """
    