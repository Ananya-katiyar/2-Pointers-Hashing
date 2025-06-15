class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = {}
        n = len(nums) 
        res = []
        if n == k == 1:
            return [nums[0]]
        for i in range(n):
            if nums[i] not in map1:
                map1[nums[i]] = 1
            else:
                map1[nums[i]] += 1
        sortitems = sorted(map1.items(), key = lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(sortitems[i][0])
        return res