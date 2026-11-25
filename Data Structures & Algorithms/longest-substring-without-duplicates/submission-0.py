class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        final = 0
        left = 0
        for right in range(len(s)):
            if s[right] in mp:
                left = max(left, mp[s[right]]+1)
            mp[s[right]] = right
            final = max(final, right - left + 1)
        return final