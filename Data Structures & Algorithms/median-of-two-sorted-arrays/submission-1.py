class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        l, r = 0, m

        while l <= r:
            i = (l + r) // 2
            j = half - i

            leftA = float("-inf") if i == 0 else nums1[i - 1]
            rightA = float("inf") if i == m else nums1[i]

            leftB = float("-inf") if j == 0 else nums2[j - 1]
            rightB = float("inf") if j == n else nums2[j]

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                else:
                    return float(max(leftA, leftB))

            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1