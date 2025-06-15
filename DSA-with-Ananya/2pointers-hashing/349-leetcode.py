class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping1 = {}
        mapping2 = {}
        res = []
        if not nums1:
            return []
        if not nums2:
            return []
        if nums1 == nums2:
            return nums1
        for i in range(len(nums1)):
            mapping1[nums1[i]] = i
        for i in range(len(nums2)):
            mapping2[nums2[i]] = i
        for i in mapping1:
            if i in mapping2:
                res.append(i)
        return res