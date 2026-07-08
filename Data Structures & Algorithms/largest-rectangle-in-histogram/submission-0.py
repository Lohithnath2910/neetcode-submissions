class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        area = 0

        for i,j in enumerate(heights):
            start = i
            while s and s[-1][1] > j:
                idx, h = s.pop()
                area = max(area,h*(i - idx))
                start = idx
            s.append((start,j))

        n = len(heights)

        while s:
            idx, h = s.pop()
            area = max(area,h*(n - idx)) 

        return area

        