class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lis = [[] for _ in range(len(nums) + 1)]
        
        dic = {}

        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for i,j in dic.items():
            lis[j].append(i) 

        f = []
        c = 0
        for i in range(len(lis)-1, 0 , -1):
            for j in lis[i]:
                f.append(j)
                if(len(f) == k):
                    return f
       
                    
        return f

        