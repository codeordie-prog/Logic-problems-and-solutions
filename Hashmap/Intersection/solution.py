from collections import defaultdict
from typing import Any, List, Dict

class Intersections:
    """
    Computes the intersection of two integer arrays, returning unique elements present in both.
    """
    def __init__(self, nums1: List[int], nums2: List[int]) -> None:
        self.result: List[int] = self.intersection(nums1, nums2)

    def __call__(self, *args: Any, **kwds: Any) -> List[int]:
        return self.result

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Returns the unique intersection of two integer arrays.

        Args:
            nums1 (List[int]): First integer array.
            nums2 (List[int]): Second integer array.

        Returns:
            List[int]: List of unique elements present in both arrays.
        """
        result: List[int] = []
        store: Dict[int, bool] = defaultdict(bool)
        if len(nums1) > len(nums2):
            max_array: List[int] = nums1
            min_array: List[int] = nums2
        else:
            max_array = nums2
            min_array = nums1
        for num in max_array:
            store[num] = True
        for num in min_array:
            if store[num]:
                result.append(num)
                store[num] = False
        return result

def main() -> None:
    """
    Test cases for the Intersections class.
    """
    # Test case 1: Example from problem statement
    nums1 = [2, 2, 9, 4, 5]
    nums2 = [1, 3, 5, 9]
    result = Intersections(nums1, nums2)
    print(f"Test 1: {result()}")  # Expected: [5, 9]

    # Test case 2: Both arrays have duplicates
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = Intersections(nums1, nums2)
    print(f"Test 2: {result()}")  # Expected: [2]

    # Test case 3: No intersection
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    result = Intersections(nums1, nums2)
    print(f"Test 3: {result()}")  # Expected: []

    # Test case 4: All elements intersect
    nums1 = [1, 2, 3]
    nums2 = [3, 2, 1]
    result = Intersections(nums1, nums2)
    print(f"Test 4: {result()}")  # Expected: [1, 2, 3] or any permutation

    # Test case 5: One array is empty
    nums1 = []
    nums2 = [1, 2, 3]
    result = Intersections(nums1, nums2)
    print(f"Test 5: {result()}")  # Expected: []

if __name__ == "__main__":
    main()