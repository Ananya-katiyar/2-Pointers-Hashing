class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        totalsum = sum(nums)
        target = totalsum - x
        if x > totalsum:
            return -1
        if x == totalsum:
            return n 
        left = 0 
        maxlen = -1
        cs = 0
        for right in range(n):
            cs += nums[right]
            while cs > target and left < right:
                cs -= nums[left]
                left += 1
            if cs == target:
                maxlen = max(maxlen, right - left + 1)
        if maxlen != -1:
            return len(nums) - maxlen
        else:
            return -1