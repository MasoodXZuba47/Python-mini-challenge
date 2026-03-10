"""
Challenge 2: Group Anagrams (LeetCode #49 - Medium)

Problem:
    Given an array of strings, group the anagrams together.
    An anagram is a word formed by rearranging the letters of another word,
    using all the original letters exactly once.

Approach:
    - Use a hash map where the key is the sorted version of each word.
    - Words that are anagrams will produce the same sorted key.
    - Time Complexity : O(n * k log k) where n = number of strings, k = max string length
    - Space Complexity: O(n * k)

Author : Masood
Date   : 2026-03-10
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Groups a list of strings into sublists of anagrams.

    Args:
        strs: List of lowercase English strings.

    Returns:
        A list of lists, where each inner list contains words
        that are anagrams of each other.
    """
    anagram_map: dict[str, list[str]] = defaultdict(list)

    for word in strs:
        # Sort the word to create a canonical key
        key = "".join(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())


# ───────────────────────── Test Cases ─────────────────────────

if __name__ == "__main__":
    # Test 1 – Standard mixed input
    test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = group_anagrams(test1)
    print("Test 1 ─ Standard input")
    print(f"  Input : {test1}")
    print(f"  Output: {result1}")
    # Expected groups: ["eat","tea","ate"], ["tan","nat"], ["bat"]

    # Test 2 – Single empty string
    test2 = [""]
    result2 = group_anagrams(test2)
    print("\nTest 2 ─ Single empty string")
    print(f"  Input : {test2}")
    print(f"  Output: {result2}")
    # Expected: [[""]]

    # Test 3 – Single character, no anagrams
    test3 = ["a"]
    result3 = group_anagrams(test3)
    print("\nTest 3 ─ Single character")
    print(f"  Input : {test3}")
    print(f"  Output: {result3}")
    # Expected: [["a"]]

    # Test 4 – All identical strings
    test4 = ["abc", "bca", "cab", "abc"]
    result4 = group_anagrams(test4)
    print("\nTest 4 ─ All anagrams of each other")
    print(f"  Input : {test4}")
    print(f"  Output: {result4}")
    # Expected: [["abc","bca","cab","abc"]]

    # Test 5 – No anagrams at all
    test5 = ["hello", "world", "python"]
    result5 = group_anagrams(test5)
    print("\nTest 5 ─ No anagrams")
    print(f"  Input : {test5}")
    print(f"  Output: {result5}")
    # Expected: [["hello"], ["world"], ["python"]]

    print("\n✅ All tests executed successfully!")
