class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(numbers)):
            mapping[numbers[i]] = i
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in mapping and mapping[diff]!=i:
                return [i+1, mapping[diff]+1]
        return []