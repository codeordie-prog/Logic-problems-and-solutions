class ProblemStatement:
    """
    Design a HashMap without using any built-in hash table libraries.

    Implement the MyHashMap class:

    - MyHashMap() initializes the object with an empty map.
    - void put(int key, int value): Inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    - int get(int key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    - void remove(key): Removes the key and its corresponding value if the map contains the mapping for the key.

    Example 1:

        Input:
        ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
        [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
        Output:
        [null, null, null, 1, -1, null, 1, null, -1]

        Explanation:
        MyHashMap myHashMap = new MyHashMap();
        myHashMap.put(1, 1); // The map is now [[1,1]]
        myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
        myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
        myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
        myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
        myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
        myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
        myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
    """


class Specifications:
    """
    1. Methods to implement:
        - Hashing function: Returns a unique index for a given key.
        - put: Adds or updates a value for a given key.
        - get: Retrieves the value for a given key.
        - remove: Removes a key and its value.
        - Dunder methods: __setitem__, __getitem__, __delitem__ for Pythonic access.

    2. Hashing: Use Knuth's multiplier for the hash function.
    3. Size: Use a large prime number for the underlying array size.
    4. Collision handling: Use linear probing to resolve collisions.
    """


class EfficiencyHandling:
    """
    Time Complexity:
        - Average case: O(1) for put, get, and remove operations with a good hash function.
        - Worst case: O(N) if many collisions occur (bad hash function or high load factor).

    Space Complexity:
        - O(N), where N is the number of key-value pairs stored.
    """


class Pseudocode:
    """
    FUNCTION hash(key):
        PRIME_MULTIPLIER = Knuth's multiplier
        SIZE = large prime number
        INDEX = (key * PRIME_MULTIPLIER) % SIZE
        RETURN INDEX

    FUNCTION put(key, value):
        index = hash(key)
        WHILE slot at index is occupied and slot's key != key:
            index = (index + 1) % SIZE
        store key and value at index

    FUNCTION get(key):
        index = hash(key)
        WHILE slot at index is occupied:
            IF slot's key == key:
                RETURN slot's value
            index = (index + 1) % SIZE
        RETURN -1

    FUNCTION remove(key):
        index = hash(key)
        WHILE slot at index is occupied:
            IF slot's key == key:
                remove key and value at index
                RETURN
            index = (index + 1) % SIZE
    """
