class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        count = {}
        ans = 0
        mf = 0
        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            mf = max(mf,count[s[j]])

            if((j - i + 1) - mf > k):
                count[s[i]] -= 1
                i += 1
            ans = max(ans,j - i + 1)
        return ans

        
        