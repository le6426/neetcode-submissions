class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0
        length = 0
        
        for n in nums:
            if (n - 1) not in hashSet:
                length = 1
                current = n

                while (current + 1) in hashSet:
                    current += 1
                    length += 1

            longest = max(length, longest)
        
        return longest
                