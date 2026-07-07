class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        a = set()
        ans = 0
        for j in range(len(s)):
            while s[j] in a:
                a.remove(s[i])
                i += 1
            a.add(s[j])
            ans = max(ans,j - i + 1)
        return ans
        