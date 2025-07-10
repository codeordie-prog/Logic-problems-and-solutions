from typing import Any, List, Dict

class Recursion:
    """
    Recursively removes all occurrences of a substring 'part' from string 's'.
    """
    def __init__(self, s: str, part: str) -> None:
        self.result: str = self.remove(s, part)

    def __call__(self, *args: Any, **kwds: Any) -> str:
        return self.result
    
    def remove(self, s: str, part: str) -> str:
        """
        Recursively removes all occurrences of 'part' from 's'.
        """
        def helper(idx: int, curr: str) -> str:
            if idx >= len(curr):
                return curr
            if part not in curr:
                return curr
            seg: str = curr[idx:(idx + len(part))]
            if seg == part:
                curr = curr[:idx] + curr[idx + len(part):]
                idx = 0
                return helper(idx, curr)
            return helper(idx + 1, curr)
        return helper(0, s)


class Loop:
    """
    Iteratively removes all occurrences of a substring 'part' from string 's' using a stack-like approach.
    """
    def __init__(self, s: str, part: str) -> None:
        self.result: str = self.remove(s, part)

    def __call__(self, *args: Any, **kwds: Any) -> str:
        return self.result
    
    def remove(self, s: str, part: str) -> str:
        """
        Iteratively removes all occurrences of 'part' from 's'.
        """
        res: List[str] = []
        plen: int = len(part)
        for char in s:
            res.append(char)
            if len(res) >= plen and "".join(res[-plen:]) == part:
                del res[-plen:]
        return "".join(res)
    

def main() -> None:
    """
    Runs test cases for both Recursion and Loop classes to ensure correctness.
    """
    test_cases: List[Dict[str, str]] = [
        {"s": "daabcbaabcbc", "part": "abc"},
        {"s": "axxxxyyyyb", "part": "xy"},
        {"s": "aabbaabbaabbaa", "part": "aab"},
        {"s": "mississippi", "part": "iss"},
        {"s": "aaaaa", "part": "aa"},
        {"s": "hellohellohello", "part": "llo"}
    ]

    for test in test_cases:
        s: str = test["s"]
        part: str = test["part"]
        result_1: Recursion = Recursion(s, part)
        result_2: Loop = Loop(s, part)
        assert result_1() == result_2()
        print(f"Input: s='{s}', part='{part}' => Output: '{result_2()}'")


if __name__ == "__main__":
    main()