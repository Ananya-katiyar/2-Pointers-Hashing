class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map1 = {}
        if not nums:
            return 
        for i in range(len(nums)):
            if nums[i] in map1:
                map1[nums[i]] += 1
                return nums[i]
            else:
                map1[nums[i]] = 1
        return 