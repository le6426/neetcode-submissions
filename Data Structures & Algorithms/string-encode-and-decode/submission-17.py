class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            j = i
            # get the length (it can be multiple digits)
            # j is the pos of where the # is
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1: j + length + 1])
            i = j + length + 1
        return result

    

            
