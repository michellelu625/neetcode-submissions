class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        dictionary = {}
        for word in strs:
            sort_word = sorted(word)
            new_word = "".join(sort_word)
            if new_word not in dictionary:
                dictionary[new_word] = [word]
            else:
                dictionary[new_word].append(word)
        for key, value in dictionary.items():
            output.append(value)
        return output

