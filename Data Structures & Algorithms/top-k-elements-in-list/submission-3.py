class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        sorted_hashmap = sorted(hashmap, key=lambda x: hashmap[x])
        return sorted_hashmap[-k:]