class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashTable = {}
        for n in nums:
            if n in hashTable:
                hashTable[n] += 1
            else:
                hashTable[n] = 1
        sorted_table = sorted(hashTable, key=lambda x: hashTable[x])
        return sorted_table[-k:]