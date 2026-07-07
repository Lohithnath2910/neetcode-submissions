class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        im = height[0]
        jm = height[-1]

        water = 0
        while i < j:
            if height[i] < height[j]:
                if height[i] >= im:
                    im = height[i]
                else:
                    water += im - height[i]
                i += 1
            else:
                if height[j] >= jm:
                    jm = height[j]
                else:
                    water += jm - height[j]
                j -= 1
        return water
        