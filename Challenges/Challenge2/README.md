# Challenge 2 – Group Anagrams

> **Difficulty:** Medium (High Intermediate)  
> **Platform:** [LeetCode #49](https://leetcode.com/problems/group-anagrams/)  
> **Language:** Python 3

---

## 📋 Problem Statement

Given an array of strings `strs`, group the **anagrams** together. You can return the answer in **any order**.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

### Example

```
Input  : ["eat","tea","tan","ate","nat","bat"]
Output : [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

---

## 💡 Approach

| Step | Description |
|------|-------------|
| 1 | Iterate through each word in the input list. |
| 2 | Sort the characters of the word to create a **canonical key**. |
| 3 | Use a **hash map** (`defaultdict(list)`) to group words sharing the same key. |
| 4 | Return all groups as a list of lists. |

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | `O(n · k log k)` — *n* strings, each of max length *k* |
| **Space** | `O(n · k)` — storing all strings in the map |

---

## 🚀 How to Run

```bash
python chellenge2.py
```

### Sample Output

```
Test 1 ─ Standard input
  Input : ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
  Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

Test 2 ─ Single empty string
  Input : ['']
  Output: [['']]

Test 3 ─ Single character
  Input : ['a']
  Output: [['a']]

Test 4 ─ All anagrams of each other
  Input : ['abc', 'bca', 'cab', 'abc']
  Output: [['abc', 'bca', 'cab', 'abc']]

Test 5 ─ No anagrams
  Input : ['hello', 'world', 'python']
  Output: [['hello'], ['world'], ['python']]

✅ All tests executed successfully!
```

---

## 📂 File Structure

```
Python/
├── chellenge2.py   # Solution + test cases
└── README.md       # This file
```

---

## 🧠 Key Concepts

- **Hash Maps** — grouping elements by a computed key
- **Sorting** — creating canonical representations of strings
- **`defaultdict`** — auto-initialising dictionary from Python's `collections` module

---

## 👤 Author

**Masood**  
Date: 2026-03-10
