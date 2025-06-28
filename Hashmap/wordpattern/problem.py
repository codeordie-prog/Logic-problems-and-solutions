class ProblemStatement:
    """
    Given a pattern and a string s, find if s follows the same pattern.
    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
    Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.

    Example 1:
        Input: pattern = "abba", s = "dog cat cat dog"
        Output: true
        Explanation: The bijection can be established as:
            'a' maps to "dog".
            'b' maps to "cat".

    Example 2:
        Input: pattern = "abba", s = "dog cat cat fish"
        Output: false

    Example 3:
        Input: pattern = "aaaa", s = "dog cat cat dog"
        Output: false
    """

class Specifications:
    """
    1. Initialize a character store mapping indices to pattern characters.
    2. Initialize a patterns map where each character in the pattern maps to a single word.
    3. Initialize a seen set to track previously encountered words.
    4. Split the string s by spaces to create a list of words.
    5. Iterate through the word list with enumeration:
        Edge Cases:
            A. If the current index exceeds the length of the pattern, return False (unmapped unique words).
            B. If the current word is already seen and the pattern character doesn't map to that word, return False (duplicates).
            C. If the current pattern character is already mapped to a different word, return False (pattern violation).
            D. If the pattern is followed correctly, continue with the loop.
    6. Add the word to the seen set and map it to the pattern character if no violations occur.
    7. Return True if the index equals the length of the pattern character store, indicating all pattern characters and unique words are mapped.
    """

class EfficiencyHandling:
    """
    Time Complexity:
        - O(N + M), where N is the length of the pattern and M is the length of the string s.

    Space Complexity:
        - O(N), as the patterns dictionary, seen set, and character store grow linearly with the pattern length.
    """

class Pseudocode:
    """
    FUNCTION follows_pattern(pattern, s):
        character_store = defaultdict(str)
        patterns_map = defaultdict(str)
        seen = set()
        words = s.split(" ")
        
        FOR EACH INDEX AND CHAR IN pattern:
            character_store[INDEX] = CHAR
        
        FOR EACH INDEX AND WORD IN words:
            IF INDEX >= LENGTH OF character_store:
                RETURN False  # unmapped unique words
            
            current_pattern = character_store[INDEX]
            
            IF WORD IN seen AND patterns_map[current_pattern] != WORD:
                RETURN False  # duplicates
            
            IF current_pattern IN patterns_map AND patterns_map[current_pattern] != WORD:
                RETURN False  # string doesn't follow the pattern
            
            IF current_pattern IN patterns_map AND patterns_map[current_pattern] == WORD:
                CONTINUE  # no violations, move forward
            
            # Otherwise, add word to seen and map it to the pattern
            seen.add(WORD)
            patterns_map[current_pattern] = WORD
        
        RETURN INDEX == LENGTH OF character_store
    """