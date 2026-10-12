class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in hashTable:
                hashTable[sortedS].append(s)
            else:
                hashTable[sortedS] = [s]
        return list(hashTable.values())