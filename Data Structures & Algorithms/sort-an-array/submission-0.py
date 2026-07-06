class Solution:
    def ms(self,nums,l,h,m):
        i = 0
        j = 0
        n1 = [nums[x] for x in range(l,m+1)]
        n2 = [nums[x] for x in range(m+1,h+1)]

        k = l
        while(i < len(n1) and j < len(n2)):
            if(n1[i] < n2[j]):
                nums[k] = n1[i]
                i += 1
            else:
                nums[k] = n2[j]
                j+= 1
            k += 1
        
        while(i < len(n1)):
            nums[k] = n1[i]
            i += 1
            k += 1

        while(j < len(n2)):
            nums[k] = n2[j]
            j += 1
            k += 1


    def m(self,nums,l,h):
        if(l < h):
            mid = (l+h)//2
            self.m(nums,l,mid)
            self.m(nums,mid+1,h)
            self.ms(nums,l,h,mid)



    def sortArray(self, nums: List[int]) -> List[int]:
        self.m(nums,0,len(nums)-1)
        return nums

        