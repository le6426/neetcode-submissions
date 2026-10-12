class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for pos, val in enumerate(nums):
            comp = target - val
            if comp in hashTable:
                return [hashTable[comp], pos]
            else:
                hashTable[val] = pos