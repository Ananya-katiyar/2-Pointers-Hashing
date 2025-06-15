from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x=Counter(nums)
        flag=False
        for i in x.values():
            if i>1:
                flag= True
                break
        return flag