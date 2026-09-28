class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}
        for s in strs:
            sorted_string = str(sorted(s))
            if sorted_string in hashTable:
                hashTable[sorted_string].append(s)
            else:
                hashTable[sorted_string] = [s]
        return list(hashTable.values())