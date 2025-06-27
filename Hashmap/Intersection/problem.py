class ProblemStatement:
    """
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must be unique, and you may return the result in any order.

    Example 1:
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2]

    Example 2:
        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [9,4] (or [4,9])
    """


class Specifications:
    """
    1. Initialize a defaultdict of bool as STORE.
    2. Initialize a result array.
    3. Iterate through the longer array and set each element's value in STORE to True.
    4. Iterate through the shorter array. For each element, if STORE[element] is True, append it to the result and set STORE[element] to False.
    5. Return the result array.
    """


class EfficiencyHandling:
    """
    Time Complexity:
        - O(N + M), where N = len(nums1) and M = len(nums2).

    Space Complexity:
        - O(N + M), due to the storage used for the hash map and the result array.
    """


class Pseudocode:
    """
    FUNCTION intersection(nums1, nums2):
        STORE = defaultdict(bool)
        IF len(nums1) > len(nums2):
            max_array = nums1
            min_array = nums2
        ELSE:
            max_array = nums2
            min_array = nums1
        RESULT = []
        FOR EACH ELEMENT IN max_array:
            STORE[ELEMENT] = True
        FOR EACH ELEMENT IN min_array:
            IF STORE[ELEMENT]:
                RESULT.APPEND(ELEMENT)
                STORE[ELEMENT] = False
        RETURN RESULT
    """