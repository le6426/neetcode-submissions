class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for string in s:
            if string.isalnum():
                newStr += string.lower()
        
        return newStr == newStr[::-1]