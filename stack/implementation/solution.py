from typing import List, Optional

class MyStack:
    """
    Implements a stack (LIFO) using a Python list to simulate stack operations.
    """
    def __init__(self) -> None:
        """
        Initialize an empty stack.
        """
        self.stack: List[int] = []

    def push(self, x: int) -> None:
        """
        Push element x onto the stack.
        Args:
            x (int): The element to push.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Remove and return the element on the top of the stack.
        Returns:
            int: The top element.
        """
        return self.stack.pop()

    def top(self) -> int:
        """
        Get the top element of the stack without removing it.
        Returns:
            int: The top element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Check whether the stack is empty.
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return not self.stack


def main() -> None:
    """
    Run a set of test cases to validate the MyStack implementation.
    """
    stack = MyStack()
    print("Push 1")
    stack.push(1)
    print("Push 2")
    stack.push(2)
    print(f"Top: {stack.top()} (Expected: 2)")
    print(f"Pop: {stack.pop()} (Expected: 2)")
    print(f"Empty: {stack.empty()} (Expected: False)")
    print(f"Pop: {stack.pop()} (Expected: 1)")
    print(f"Empty: {stack.empty()} (Expected: True)")
    # Additional test
    stack.push(10)
    stack.push(20)
    print(f"Top: {stack.top()} (Expected: 20)")
    print(f"Pop: {stack.pop()} (Expected: 20)")
    print(f"Top: {stack.top()} (Expected: 10)")

if __name__ == "__main__":
    main()
    

