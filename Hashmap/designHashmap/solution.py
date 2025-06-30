from typing import List, Optional, Any, Iterator, Tuple
from sympy import isprime


class HashMap:
    """
    A simple hash map implementation using separate chaining for collision resolution.
    Supports put, get, and remove operations, as well as Pythonic dunder methods.
    """
    def __init__(self, size: int = 1009) -> None:
        """
        Initializes the hash map with a given size (default is a prime number for better distribution).
        """
        self.size: int = size
        self.table: List[List[Tuple[int, int]]] = [[] for _ in range(self.size)]
        self.PRIME_MULTIPLIER: int = 2654435761

    def __repr__(self) -> str:
        items = ", ".join(f"{k}: {v}" for k, v in self.items())
        return "{" + items + "}"

    def __setitem__(self, key: int, value: int) -> None:
        self.put(key, value)

    def __getitem__(self, key: int) -> int:
        result = self.get(key)
        if result == -1:
            raise KeyError(f"Key {key} not found in HashMap.")
        return result

    def __delitem__(self, key: int) -> None:
        self.remove(key)

    def items(self) -> Iterator[Tuple[int, int]]:
        for bucket in self.table:
            for k, v in bucket:
                yield (k, v)

    def __iter__(self) -> Iterator[int]:
        for bucket in self.table:
            for k, _ in bucket:
                yield k

    def hash_key(self, key: int) -> int:
        """
        Hashes the key using Knuth's multiplicative method.
        """
        index: int = (key * self.PRIME_MULTIPLIER) % self.size
        return index

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates the (key, value) pair in the hash map.
        """
        index: int = self.hash_key(key)
        bucket: List[Tuple[int, int]] = self.table[index]
        for idx, (k, _) in enumerate(bucket):
            if key == k:
                bucket[idx] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        """
        Retrieves the value for the given key, or -1 if not found.
        """
        index: int = self.hash_key(key)
        bucket: List[Tuple[int, int]] = self.table[index]
        for k, v in bucket:
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the key and its value from the hash map if present.
        """
        index: int = self.hash_key(key)
        bucket: List[Tuple[int, int]] = self.table[index]
        self.table[index] = [(k, v) for (k, v) in bucket if k != key]


def main() -> None:
    """
    Test cases for the HashMap class covering all required behaviors.
    """
    my_hash_map = HashMap()

    # Test 1: Basic put and get
    print("Test 1: Key = 1, Value = 1")
    my_hash_map.put(1, 1)
    assert my_hash_map[1] == 1
    print("Test 1 passed!\n" + "_" * 50)

    # Test 2: Put and get another key
    print("Test 2: Key = 2, Value = 2")
    my_hash_map.put(2, 2)
    assert my_hash_map[2] == 2
    print("Test 2 passed!\n" + "_" * 50)

    # Test 3: Get existing and non-existing keys
    print("Test 3: Get existing and non-existing keys")
    assert my_hash_map.get(1) == 1
    assert my_hash_map.get(3) == -1
    print("Test 3 passed!\n" + "_" * 50)

    # Test 4: Update value for existing key
    print("Test 4: Update value for existing key")
    my_hash_map.put(2, 1)
    assert my_hash_map[2] == 1
    print("Test 4 passed!\n" + "_" * 50)

    # Test 5: Remove a key and check
    print("Test 5: Remove a key and check")
    my_hash_map.remove(2)
    assert my_hash_map.get(2) == -1
    print("Test 5 passed!\n" + "_" * 50)

    # Test 6: Dunder methods
    print("Test 6: Dunder methods")
    my_hash_map[10] = 100
    assert my_hash_map[10] == 100
    del my_hash_map[10]
    try:
        _ = my_hash_map[10]
        assert False, "KeyError not raised for deleted key"
    except KeyError:
        print("KeyError correctly raised for deleted key.")
    print("Test 6 passed!\n" + "_" * 50)

    # Test 7: Iteration and items
    print("Test 7: Iteration and items")
    my_hash_map.put(20, 200)
    my_hash_map.put(30, 300)
    keys = set(iter(my_hash_map))
    items = set(my_hash_map.items())
    assert 20 in keys and 30 in keys
    assert (20, 200) in items and (30, 300) in items
    print("Test 7 passed!\n" + "_" * 50)

    print("All tests passed!")


if __name__ == "__main__":
    main()