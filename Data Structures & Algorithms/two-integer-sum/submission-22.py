class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for pos, val in enumerate(nums):
            comp = target - val
            if comp in hashmap:
                return [hashmap[comp], pos]
            hashmap[val] = pos

        