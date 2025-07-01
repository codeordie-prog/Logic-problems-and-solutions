from typing import Any, List, DefaultDict
from collections import defaultdict

class Anagrams:
    def __init__(self, strs: List[str]) -> None:
        self.result: List[List[str]] = self.group_anagrams(strs)

    def __call__(self, *args: Any, **kwds: Any) -> List[List[str]]:
        return self.result

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: DefaultDict[str, List[str]] = defaultdict(list)
        for word in strs:
            sorted_word: str = "".join(sorted(word))
            anagrams[sorted_word].append(word)
        return list(anagrams.values())


def main() -> None:
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc", "bca", "cab", "xyz", "zyx"], [["abc", "bca", "cab"], ["xyz", "zyx"]]),
        (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
    ]
    for i, (input_list, expected_groups) in enumerate(test_cases, 1):
        anagrams = Anagrams(input_list)
        result = anagrams()
        # For comparison, sort each group and the list of groups
        result_sorted = sorted([sorted(group) for group in result])
        expected_sorted = sorted([sorted(group) for group in expected_groups])
        print(f"Test case {i}: input={input_list}\n  Output: {result_sorted}\n  Expected: {expected_sorted}\n")
        assert result_sorted == expected_sorted, f"Test case {i} failed!"
    print("All test cases passed.")


if __name__ == "__main__":
    main()