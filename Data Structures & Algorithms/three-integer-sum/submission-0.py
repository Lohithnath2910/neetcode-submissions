class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = sorted(nums)
        n = len(nums)
        l = []
        for i in range(n):
            if i > 0 and a[i] == a[i-1]:
                continue
            j = i + 1
            k = n - 1

            while(j < k):
                sum = a[i] + a[j] + a[k]
                if(sum > 0):
                    k -= 1
                elif(sum < 0):
                    j += 1
                else:
                    l.append([a[i],a[j],a[k]])
                    j += 1
                    k -= 1
                    while(j < k and a[j] == a[j-1]):
                        j += 1
                    while(j < k and a[k] == a[k+1]):
                        k -= 1
        return l
        