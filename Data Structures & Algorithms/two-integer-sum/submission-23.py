class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for pos, val in enumerate(nums):
            complement = target - val
            if complement in hashTable:
                return [hashTable[complement], pos]
            else:
                hashTable[val] = pos