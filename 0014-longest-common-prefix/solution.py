class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ''
        for i, char in enumerate(strs[0]):
            for str in strs:
                if i >= len(str) or str[i] != char:
                    return longest
            longest += char
        return longest
