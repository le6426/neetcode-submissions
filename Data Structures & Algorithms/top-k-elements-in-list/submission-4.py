class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashTable = {}
        for num in nums:
            if num in hashTable:
                hashTable[num] += 1
            else:
                hashTable[num] = 1
        sorted_hashTable = sorted(hashTable, key=lambda x: hashTable[x])
        return sorted_hashTable[-k:]