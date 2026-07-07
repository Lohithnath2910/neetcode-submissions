class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        c = 0

        for i in a:
            if (i-1 not in a):
                temp = 1
                curr = i

                while(curr + 1 in a):
                    curr += 1
                    temp += 1
                
                c = max(c,temp)
        return c

                
                
        