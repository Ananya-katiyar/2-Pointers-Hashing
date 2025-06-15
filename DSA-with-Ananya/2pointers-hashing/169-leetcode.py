class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map1 = {}
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        if not nums:
            return 
        for i in range (n):
            if nums[i] in map1:
                map1[nums[i]] += 1
                if map1[nums[i]] > n/2:
                    return nums[i]
            else:
                map1[nums[i]] = 1
        return   