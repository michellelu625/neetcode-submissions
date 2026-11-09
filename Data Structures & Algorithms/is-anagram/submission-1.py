class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}
        for letter in s:
            seen_s[letter] = seen_s.get(letter, 0) + 1
        for letter in t:
            seen_t[letter] = seen_t.get(letter, 0) + 1
        if seen_s == seen_t:
            return True
        else:
            return False