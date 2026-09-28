class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0

        for num in nums:
            length = 0

            if (num - 1) not in hashSet:
                while (num + length) in hashSet:
                    length += 1
            longest = max(longest, length)
        
        return longest