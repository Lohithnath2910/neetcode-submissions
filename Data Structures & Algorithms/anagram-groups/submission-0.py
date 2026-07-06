from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for i in strs:
            c = [0]*26
            for s in i:
                c[ord(s) - ord('a')] += 1

            ans[tuple(c)].append(i)
        
        return list(ans.values())

