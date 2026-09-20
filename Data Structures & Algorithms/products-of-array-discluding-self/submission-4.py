class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        prefix = 1
        for pos in range(len(nums)):
            result[pos] = prefix
            prefix *= nums[pos]
        
        postfix = 1
        for pos in range(len(nums) - 1, -1, -1):
            result[pos] *= postfix
            postfix *= nums[pos]

        return result
